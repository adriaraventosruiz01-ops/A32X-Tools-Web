"""Builds the Simplified Chinese pages under /zh/ from the English pages.

Usage (from the repo root):  python3 i18n/build_zh.py

1. Translates the English page with zh_strings.PAIRS and points links at /zh/.
2. Serves the site locally and lets headless Chrome run the page scripts, then
   writes the rendered content (features, screenshots, videos, reviews…) into
   the static HTML, so Baidu and AI crawlers that do not run JavaScript still
   see all the Chinese text.

Re-run it whenever the English pages change.
"""

import functools
import html
import json
import http.server
import re
import subprocess
import sys
import threading
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from zh_strings import FAQ, HEAD, KEYWORDS, PAIRS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.a32xtools.com"
# Bilibili account banned on 2026-10-25 for 365 days; set SHOW_BILIBILI back to True when it is lifted.
SHOW_BILIBILI = False
BILIBILI = "https://space.bilibili.com/3747575152774840"
# Bilibili videos listed under each page's demos (page key -> [(title, BV id)]).
_A32X_VIDEOS = [
    ("A320 ECAM 复位：一分钟找到程序和跳开关", "BV1KJH56GEo2"),
    ("A320 常用件号速查：带真实照片", "BV1h3H56mEPx"),
    ("雷击检查后用手机几分钟出结构损伤报告 PDF", "BV1u3H56mEUS"),
]
BILIBILI_VIDEOS = {
    "hub": _A32X_VIDEOS,
    "a32x": _A32X_VIDEOS,
    "a330": [("A330 ECAM 复位：ELEC TR 1 FAULT 程序与跳开关位置", "BV1u5H561EVT")],
    "b737": [("737NG A/P 告警灯：程序、跳开关和 FCC 位置", "BV1uVH56jEZL")],
}
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 8799

# (English source, key in HEAD, English path, Chinese path)
PAGES = [
    ("index.html", "hub", "/", "/zh/"),
    ("a32x-tools/index.html", "a32x", "/a32x-tools/", "/zh/a32x-tools/"),
    ("a330-tools/index.html", "a330", "/a330-tools/", "/zh/a330-tools/"),
    ("737-tools/index.html", "b737", "/737-tools/", "/zh/737-tools/"),
]
PRODUCT_PATHS = {"/a32x-tools/": "/zh/a32x-tools/", "/a330-tools/": "/zh/a330-tools/", "/737-tools/": "/zh/737-tools/"}

# Elements whose content the page script renders; copied from the rendered DOM.
RENDERED_INNER = [
    "productTitle", "productSubtitle", "productDescription", "pillGroup",
    "featuresGrid", "tourSubtitle", "screensGrid", "desktopVideoGrid",
    "mobileVideoGrid", "reviewsTrack", "disclaimerText", "footerText",
]
# Elements whose hidden/visible state the page script sets.
RENDERED_START_TAG = ["reviewsSection", "videosHeading", "tourEmpty", "heroPhoto"]

ZH_HEAD_EXTRA = """  <meta name="applicable-device" content="pc,mobile" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <style>
    /* Google Play is not available in mainland China. */
    .store-badge-wrap:has(#googlePlayLink) { display: none; }
    body { font-family: "IBM Plex Sans", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", system-ui, sans-serif; }
    .faq-list { display: grid; gap: 10px; }
    .faq-list details { background: var(--panel); border: var(--edge-soft); border-radius: var(--r-md); padding: 14px 16px; }
    .faq-list summary { cursor: pointer; font-weight: 700; line-height: 1.5; }
    .faq-list p { margin: 10px 0 0; color: var(--muted); line-height: 1.7; }
    .bili-link { display: inline-flex; align-items: center; gap: 8px; margin-top: 16px; padding: 10px 18px; border-radius: 999px; border: 1px solid #fb7299; color: #fff; background: rgba(251, 114, 153, 0.16); font-weight: 700; text-decoration: none; }
    .bili-link:hover { background: rgba(251, 114, 153, 0.28); }
    .bili-list { margin: 12px 0 0; padding-left: 20px; line-height: 1.9; }
    .bili-list a { color: inherit; }
  </style>
"""

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class _Locator(HTMLParser):
    """Finds the source span of the element with a given id."""

    def __init__(self, text, target):
        super().__init__(convert_charrefs=False)
        self.text, self.target = text, target
        self.line_starts = [0]
        for m in re.finditer("\n", text):
            self.line_starts.append(m.end())
        self.depth = None
        self.span = None

    def _offset(self):
        line, col = self.getpos()
        return self.line_starts[line - 1] + col

    def handle_starttag(self, tag, attrs):
        if self.span is not None:
            return
        if self.depth is None:
            if dict(attrs).get("id") == self.target:
                start = self._offset()
                self.open_tag_end = start + len(self.get_starttag_text())
                self.open_start, self.tag = start, tag
                self.depth = 0 if tag in VOID else 1
                if tag in VOID:
                    self.span = (start, self.open_tag_end, self.open_tag_end, self.open_tag_end)
        elif tag not in VOID:
            self.depth += 1

    def handle_endtag(self, tag):
        if self.depth is None or self.span is not None or tag in VOID:
            return
        self.depth -= 1
        if self.depth == 0:
            close = self._offset()
            end = self.text.index(">", close) + 1
            self.span = (self.open_start, self.open_tag_end, close, end)


def locate(text, element_id):
    p = _Locator(text, element_id)
    p.feed(text)
    if p.span is None:
        raise KeyError(element_id)
    return p.span  # (start, end of start tag, start of end tag, end)


def translate(src, head_key, en_path, zh_path):
    s = src
    for en in sorted(PAIRS, key=len, reverse=True):
        s = s.replace(en, PAIRS[en])

    s = s.replace('<html lang="en">', '<html lang="zh-Hans">', 1)
    s = s.replace('content="en_US"', 'content="zh_CN"')

    # Head: title, descriptions, canonical and og:url.
    h = HEAD[head_key]
    s = re.sub(r"<title>.*?</title>", f"<title>{h['title']}</title>", s, count=1, flags=re.S)
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(rf'(<meta {attr} content=")[^"]*(")', rf"\g<1>{h['description']}\2", s, count=1)
    for attr in ('property="og:title"', 'name="twitter:title"'):
        s = re.sub(rf'(<meta {attr} content=")[^"]*(")', rf"\g<1>{h['title']}\2", s, count=1)
    s = s.replace(f'<link rel="canonical" href="{SITE}{en_path}" />', f'<link rel="canonical" href="{SITE}{zh_path}" />')
    s = s.replace(f'<meta property="og:url" content="{SITE}{en_path}" />', f'<meta property="og:url" content="{SITE}{zh_path}" />')
    s = s.replace('<meta name="viewport"', ZH_HEAD_EXTRA + '  <meta name="viewport"', 1)
    s = re.sub(r'(<meta name="description" content="[^"]*" />\n)',
               rf'\1  <meta name="keywords" content="{KEYWORDS[head_key]}" />\n', s, count=1)

    # FAQ: visible section plus FAQPage structured data, both static.
    faq = FAQ[head_key]
    items = "\n".join(
        f"        <details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faq
    )
    section = (
        '    <section class="section" id="faq">\n'
        '      <h2 class="section-title">常见问题</h2>\n'
        f'      <div class="faq-list">\n{items}\n      </div>\n'
        '    </section>\n\n'
    )
    anchor = '    <section class="section">\n      <h2 class="section-title">免责声明</h2>'
    if anchor not in s:
        raise SystemExit(f"disclaimer section not found in {en_path}")
    s = s.replace(anchor, section + anchor, 1)
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": "zh-Hans",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
        ],
    }
    s = s.replace("</head>", '  <script type="application/ld+json">\n'
                  + json.dumps(faq_ld, ensure_ascii=False, indent=2) + "\n  </script>\n</head>", 1)

    # Product page URLs inside structured data and the page script.
    for en, zh in PRODUCT_PATHS.items():
        s = s.replace(f'"url": "{SITE}{en}"', f'"url": "{SITE}{zh}"')
        s = s.replace(f'"@id": "{SITE}{en}#', f'"@id": "{SITE}{zh}#')
        s = s.replace(f'<a href="{en}"', f'<a href="{zh}"')
        s = s.replace(f'canonicalPath: "{en}"', f'canonicalPath: "{zh}"')
    s = s.replace('canonicalPath: "/",', 'canonicalPath: "/zh/",')
    s = s.replace('id="brandHomeLink" href="/"', 'id="brandHomeLink" href="/zh/"')

    # The TechlogMRO jobs and training links are not shown in the Chinese version.
    s, removed = re.subn(
        r'\n\s*<div class="footerResources">.*?\n      </div>(?=\n\s*<div class="footer" id="footerText">)',
        "", s, count=1, flags=re.S,
    )
    if not removed:
        raise SystemExit(f"TechlogMRO block not found in {en_path}")

    # Link to the Bilibili channel under the demo videos.
    grid = '<div class="mobile-video-grid" id="mobileVideoGrid" aria-label="演示视频"></div>'
    if SHOW_BILIBILI and grid not in s:
        raise SystemExit(f"video grid not found in {en_path}")
    videos = "".join(
        f'\n          <li><a href="https://www.bilibili.com/video/{bv}/" target="_blank" rel="noopener">{html.escape(t)}</a></li>'
        for t, bv in BILIBILI_VIDEOS.get(head_key, [])
    )
    video_list = f'\n        <ul class="bili-list">{videos}\n        </ul>' if videos else ""
    if SHOW_BILIBILI:
        s = s.replace(grid, grid + f'\n        <a class="bili-link" href="{BILIBILI}" target="_blank" rel="noopener">在 Bilibili 观看更多演示视频 →</a>' + video_list, 1)

    # Chinese App Store storefront.
    s = s.replace("https://apps.apple.com/es/app/", "https://apps.apple.com/cn/app/")

    # Language link and redirect script come from the English page.
    s = re.sub(r"\s*<!-- lang-redirect -->.*?<!-- /lang-redirect -->", "", s, flags=re.S)
    s = re.sub(
        r'<a class="link langLink" href="[^"]*" hreflang="zh-Hans" lang="zh-Hans" onclick="[^"]*">中文版</a>',
        f'<a class="link langLink" href="{en_path}?lang=en" hreflang="en" lang="en" '
        """onclick="try{localStorage.setItem('lang','en')}catch(e){}">English version</a>""",
        s,
    )
    return s


def render(url):
    out = subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=6000",
         "--window-size=1300,4000", "--dump-dom", url],
        capture_output=True, text=True, timeout=120, check=True,
    )
    return out.stdout


def prerender(page_html, rendered):
    for element_id in RENDERED_INNER:
        if f'id="{element_id}"' not in page_html:
            continue
        a, b, c, d = locate(rendered, element_id)
        inner = rendered[b:c]
        a, b, c, d = locate(page_html, element_id)
        page_html = page_html[:b] + inner + page_html[c:]
    for element_id in RENDERED_START_TAG:
        if f'id="{element_id}"' not in page_html:
            continue
        a, b, _, _ = locate(rendered, element_id)
        start_tag = rendered[a:b]
        a, b, _, _ = locate(page_html, element_id)
        page_html = page_html[:a] + start_tag + page_html[b:]
    return page_html


def main():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = functools.partial(Quiet, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    used = set()
    try:
        for src, head_key, en_path, zh_path in PAGES:
            english = (ROOT / src).read_text(encoding="utf-8-sig")
            used |= {k for k in PAIRS if k in english}
            page = translate(english, head_key, en_path, zh_path)
            out = ROOT / zh_path.strip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(page, encoding="utf-8")
            rendered = render(f"http://127.0.0.1:{PORT}{zh_path}")
            out.write_text(prerender(page, rendered), encoding="utf-8")
            print(f"wrote {out.relative_to(ROOT)}")
    finally:
        server.shutdown()

    unused = [k for k in PAIRS if k not in used]
    if unused:
        print("strings not found in any English page:")
        for k in unused:
            print("  ", k[:100])


if __name__ == "__main__":
    main()

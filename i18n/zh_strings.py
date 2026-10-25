# English -> Simplified Chinese strings for the /zh/ pages.
# Each key is an exact substring of the English pages (quotes or tags included
# where the bare word would be ambiguous). build_zh.py applies them longest first.
# Terms follow the App Store listings: 复位 (reset), 跳开关 (CB), 件号 (part number),
# 告警灯 (annunciator light), 电子设备舱 (E/E bay), 航线维修 (line maintenance).

PAIRS = {
    # ── Static markup ───────────────────────────────────────────────────────
    'aria-label="Product selector"': 'aria-label="选择机型"',
    '>Choose aircraft:<': '>选择机型：<',
    '>One-time purchase<': '>一次性购买<',
    '>Offline-first. No network required.<': '>离线优先，无需网络。<',
    '>Download now<': '>立即下载<',
    'aria-label="Google Play Store"': 'aria-label="Google Play 商店"',
    'alt="Get it on Google Play"': 'alt="在 Google Play 下载"',
    '>Coming soon<': '>即将推出<',
    'aria-label="Apple Store"': 'aria-label="App Store"',
    'alt="Download on the App Store"': 'alt="在 App Store 下载"',
    'alt="A32X Tools on the ramp at night"': 'alt="夜间停机坪上的 A32X Tools"',
    'alt="A330 Tools on the ramp at night"': 'alt="夜间停机坪上的 A330 Tools"',
    'alt="737 Tools running inside a 737 E/E compartment"': 'alt="在 737 电子设备舱内使用 737 Tools"',
    'alt="A32X Tools icon"': 'alt="A32X Tools 图标"',
    'alt="A330 Tools icon"': 'alt="A330 Tools 图标"',
    'alt="737 Tools icon"': 'alt="737 Tools 图标"',
    ">What's inside<": '>功能一览<',
    '>App tour<': '>应用导览<',
    '>Screenshots coming soon<': '>截图即将推出<',
    '>Demos<': '>演示视频<',
    'aria-label="Video demos"': 'aria-label="演示视频"',
    '>What professionals say<': '>专业人士的评价<',
    '>Verified reviews from aviation maintenance engineers.<': '>来自航空维修工程师的真实评价。<',
    'aria-label="Previous review"': 'aria-label="上一条评价"',
    'aria-label="Next review"': 'aria-label="下一条评价"',
    '>Privacy Policy<': '>隐私政策（英文）<',
    '>Support / FAQ<': '>支持 / 常见问题（英文）<',
    '>Need help? Email us<': '>需要帮助？给我们发邮件<',
    '>Disclaimer<': '>免责声明<',
    '. All rights reserved.': ' 版权所有。',
    '>Download</a>': '>下载</a>',
    '>Tap anywhere to close<': '>点击任意位置关闭<',
    'aria-label="Previous image"': 'aria-label="上一张"',
    'aria-label="Next image"': 'aria-label="下一张"',
    'aria-label="Close preview"': 'aria-label="关闭预览"',
    'alt="Screenshot preview"': 'alt="截图预览"',
    'content:"Tap to zoom"': 'content:"点击放大"',
    'aria-label="Play video"': 'aria-label="播放视频"',
    '"Pause video" : "Play video"': '"暂停视频" : "播放视频"',

    # ── Hub page ────────────────────────────────────────────────────────────
    '"A32X Tools | Airbus & Boeing Maintenance Reference Apps"': '"A32X Tools | 空客与波音飞机维修参考应用"',
    '"A32X Tools, A330 Tools and 737 Tools are professional maintenance reference apps for ECAM resets, annunciator lights, structural damage reports, electrical contacts, alpha callups, and common part numbers."':
        '"A32X Tools、A330 Tools 和 737 Tools 是专业的飞机维修参考应用，涵盖 ECAM 复位、告警灯、结构损伤报告、电气触点、Alpha Callups 和常用件号。"',

    # ── A32X Tools ──────────────────────────────────────────────────────────
    '"A32X Tools — A320 ECAM Resets"': '"A32X Tools — A320 ECAM 复位"',
    '"A32X Tools | Airbus A320 ECAM Resets App"': '"A32X Tools | 空客 A320 ECAM 复位应用"',
    '"ECAM resets, damage reports, electrical contacts & part numbers. Offline."':
        '"ECAM 复位、损伤报告、电气触点与件号，离线可用。"',
    '"Professional reference app for A318/A319/A320/A321 technicians covering ECAM resets, structural damage reports, electrical contacts, alpha callups, and most common part numbers in one fast toolkit."':
        '"面向 A318/A319/A320/A321 维修技术人员的专业参考应用：ECAM 复位、结构损伤报告、电气触点、Alpha Callups 和最常用件号，一个应用快速搞定。"',
    '"Airbus A320 family maintenance app: ECAM troubleshooting and resets, structural damage reports, electrical contacts, alpha callups and common part numbers."':
        '"空客 A320 系列维修应用：ECAM 排故与复位、结构损伤报告、电气触点、Alpha Callups 和常用件号。"',
    '"Seven key screens with quick summaries, plus 3 videos showcasing the most important features."':
        '"七个核心界面及简要说明，另有 3 段视频演示最重要的功能。"',
    '"A32X Tools is designed for training and reference use only. It does not replace official Airbus documentation. ECAM messages, reset procedures, structural damage reports, and AMM/MEL/ESPM references are provided as learning aids. Always consult the latest official Airbus manuals before performing any maintenance or operational task. Airbus and A320 are trademarks of their respective owners and are not affiliated with this app."':
        '"A32X Tools 仅供培训和参考使用，不能替代空客官方文件。ECAM 信息、复位程序、结构损伤报告以及 AMM/MEL/ESPM 参考仅作为学习辅助资料。在执行任何维修或运行工作前，请务必查阅最新的空客官方手册。Airbus 和 A320 是其各自所有者的商标，与本应用无关联。"',
    '"Central hub for Airbus A320 family maintenance."': '"空客 A320 系列维修的一站式入口。"',
    'title: "HOME"': 'title: "首页"',
    '"ECAM RESETS DETAIL"': '"ECAM 复位详情"',
    '"Guided resets with exact CBs, clear steps, and a live timer."': '"分步引导复位：精确的跳开关、清晰的步骤和实时计时器。"',
    'title: "DAMAGE REPORTS"': 'title: "损伤报告"',
    '"Lightning strike damage? Log multiple findings in one report with photos, clear summaries, and PDF/ZIP share."':
        '"雷击损伤？在一份报告中记录多处发现，附照片和清晰摘要，并以 PDF/ZIP 分享。"',
    '"CONTACTS, SPLICES & TERMINALS"': '"触点、接线管与端子"',
    '"Find the right P/N fast with exact ESPM references."': '"借助精确的 ESPM 参考，快速找到正确件号。"',
    '"ALPHA CALLUPS & AMM REFERENCES"': '"ALPHA CALLUPS 与 AMM 参考"',
    '"Alpha callups and AMM references with instant search."': '"Alpha Callups 和 AMM 参考，即时搜索。"',
    '"COMMONLY USED PART NUMBERS"': '"常用件号"',
    '"Live catalog with real photos, organized by zone and category."': '"附真实照片的件号目录，按区域和类别整理。"',
    '"CREATE YOUR OWN ITEMS"': '"创建自定义项目"',
    '"Add and share your own items to grow the database faster."': '"添加并分享你自己的项目，让数据库更快丰富。"',
    '"ECAM MESSAGE SEARCH & RESET"': '"ECAM 信息搜索与复位"',
    '"Find an ECAM message and follow the complete reset procedure step by step."': '"找到 ECAM 信息，逐步完成完整的复位程序。"',
    '"PART SEARCH & PHOTO CHECK"': '"件号搜索与照片核对"',
    '"Locate a part quickly and review its photo to verify the item before action."': '"快速定位零件，并在操作前通过照片核对。"',
    '"DAMAGE REPORT PDF WORKFLOW"': '"损伤报告 PDF 流程"',
    '"Create a damage report and preview the generated PDF instantly inside the app."': '"创建损伤报告，并在应用内即时预览生成的 PDF。"',
    'title: "ECAM Resets"': 'title: "ECAM 复位"',
    '"Search any ECAM message and get the full reset: step-by-step procedure, circuit breakers with panel location and photos, and a built-in live timer."':
        '"搜索任意 ECAM 信息即可获得完整复位方案：分步程序、跳开关及其面板位置和照片，并内置实时计时器。"',
    'title: "Structural Damage Reports"': 'title: "结构损伤报告"',
    '"Log multiple damage findings with photos and generate a ready-to-share PDF or ZIP report directly from your phone, in seconds."':
        '"用手机记录多处带照片的损伤发现，几秒钟内生成可直接分享的 PDF 或 ZIP 报告。"',
    'title: "Electrical References"': 'title: "电气参考"',
    '"Find the right crimping reference for any connector, splice or terminal instantly — with exact ESPM part numbers."':
        '"即时找到任意连接器、接线管或端子的压接参考，并附精确的 ESPM 件号。"',
    'title: "AMM & Alpha Callups"': 'title: "AMM 与 Alpha Callups"',
    '"Every AMM reference and alpha callup at your fingertips — searchable instantly, from task numbers to chapter references."':
        '"所有 AMM 参考和 Alpha Callups 触手可及：从工卡号到章节参考，即时可搜。"',
    'title: "Part Numbers"': 'title: "件号"',
    '"Your most-used parts with real photos, organized by zone and category. Find what you need before you reach the shelf."':
        '"最常用的零件附真实照片，按区域和类别整理。走到货架前就已找到所需件号。"',
    'title: "Custom Items"': 'title: "自定义项目"',
    '"Missing a part in the catalog? Add it yourself with photos and references. Your entries are saved and ready for next time."':
        '"目录里缺少某个零件？自己添加照片和参考即可。你的条目会被保存，下次随时可用。"',

    # Reviews: the original stays; the English line under it becomes Chinese.
    'textEn: "As an A320 certifier, this app is essential in my daily work. The best part are the ECAM resets: precise procedures with real CB panel photos and a countdown that works brilliantly. It also makes it easy to find AMM/MEL references and the most used P/Ns. You can tell it was designed by someone who truly understands line maintenance. Very intuitive interface — 100% recommended!"':
        'textEn: "作为 A320 放行人员，这款应用是我日常工作中必不可少的。最好用的是 ECAM 复位：程序精确，配有真实的跳开关面板照片，倒计时也非常好用。查找 AMM/MEL 参考和最常用件号也很方便。看得出是真正懂航线维修的人设计的。界面非常直观——100% 推荐！"',
    'textEn: "After trying several apps, without doubt the most complete one — with features and characteristics that make it indispensable for the daily work of an AME."':
        'textEn: "试过好几款应用后，这无疑是功能最全面的一款，它的功能和特点让它成为维修工程师日常工作中不可或缺的工具。"',
    'textEn: "Works perfectly. It has everything you need for line maintenance when you need quick access to the A320 manual. Resolves ECAM warnings with the reset/test or MEL chapter. Download it without hesitation if you work in line maintenance."':
        'textEn: "运行完美。需要快速查阅 A320 手册时，航线维修所需的一切都在这里。可通过复位/测试或 MEL 章节处理 ECAM 警告。如果你从事航线维修，请毫不犹豫地下载。"',
    # Written in English: keep it and add the Chinese line under it.
    'Totally worthy for aircraft maintenance engineers.", source':
        'Totally worthy for aircraft maintenance engineers.", textEn: "非常好用的 A320 航线维修工具，可快速查看常见的跳开关复位和常用件号。对飞机维修工程师来说完全值得。", source',
    'textEn: "Very complete app for A320 system resets and other key functions, including the most common P/Ns, AMM references, and much more. Intuitive, fast and practical — much better and more complete than anything I\'ve used before."':
        'textEn: "非常全面的 A320 系统复位应用，还包含最常用件号、AMM 参考等众多关键功能。直观、快速、实用——比我以前用过的任何应用都更好、更全面。"',
    'textEn: "It really surprised me — it has more ECAM message resets than other apps I\'ve used. Having a P/N database with photos is really handy. Recommended!"':
        'textEn: "真的让我很惊喜——它的 ECAM 信息复位比我用过的其他应用都多。带照片的件号数据库非常方便。推荐！"',
    'textEn: "This app is very well structured and designed for all professionals in the sector. It was created by a maintenance technician, so it is without any doubt very functional — 100% recommended."':
        'textEn: "这款应用结构清晰，为业内所有专业人员而设计。它由一名维修技术人员开发，因此毫无疑问非常实用——100% 推荐。"',
    'textEn: "Very good app, more complete than other more expensive and popular ones — definitely recommended for AMEs."':
        'textEn: "非常好的应用，比其他更贵、更热门的应用还要全面——强烈推荐给维修工程师。"',
    'textEn: "Indispensable for working on Airbus aircraft. I\'ve tried several and this one is without doubt the most complete and effective."':
        'textEn: "维修空客飞机必备。我试过好几款，这款无疑是最全面、最高效的。"',
    'textEn: "Very useful for night shifts and line maintenance. Excellent app. Lets you work quickly and precisely."':
        'textEn: "夜班和航线维修时非常有用。出色的应用，让工作又快又准。"',
    'textEn: "Fantastic tool — it guides you quickly to the necessary manuals, greatly streamlining daily work."':
        'textEn: "很棒的工具——能快速引导你找到所需手册，大大简化日常工作。"',
    'textEn: "An essential app if you work with Airbus aircraft. The best I\'ve tried, without doubt."':
        'textEn: "如果你维修空客飞机，这是一款必备应用。毫无疑问是我用过最好的。"',
    'textEn: "Much more complete than other current apps — clean interface, intuitive and very practical. I recommend it."':
        'textEn: "比现有的其他应用全面得多——界面简洁、直观，非常实用。推荐。"',
    'textEn: "Good tool, a solid base platform. It needs improvements, but I believe the development team will keep making the app better."':
        'textEn: "不错的工具，基础扎实。还需要改进，但我相信开发团队会不断完善这款应用。"',
    'textEn: "The best tool focused on the A32X so far. Simply brilliant."':
        'textEn: "目前专注于 A32X 的最佳工具。简直太棒了。"',
    'textEn: "Amazing and extremely useful app for line maintenance!!! The best for the A320!!!"':
        'textEn: "对航线维修来说超棒、极其实用的应用！！！A320 最佳！！！"',

    # ── A330 Tools ──────────────────────────────────────────────────────────
    '"A330 Tools — A330 ECAM Resets"': '"A330 Tools — A330 ECAM 复位"',
    '"A330 Tools | Airbus A330 ECAM Resets App"': '"A330 Tools | 空客 A330 ECAM 复位应用"',
    '"ECAM resets, damage reports, AMM alpha callups & part numbers. Offline."':
        '"ECAM 复位、损伤报告、AMM Alpha Callups 与件号，离线可用。"',
    '"Professional reference app for A330 technicians covering ECAM resets, structural damage reports, electrical contacts, alpha callups, and most common part numbers in one fast toolkit."':
        '"面向 A330 维修技术人员的专业参考应用：ECAM 复位、结构损伤报告、电气触点、Alpha Callups 和最常用件号，一个应用快速搞定。"',
    '"Airbus A330 maintenance app: ECAM troubleshooting and resets, structural damage reports, electrical contacts, alpha callups and common part numbers."':
        '"空客 A330 维修应用：ECAM 排故与复位、结构损伤报告、电气触点、Alpha Callups 和常用件号。"',
    '"Seven key screens with quick summaries, plus a video demo of the ECAM search and reset."':
        '"七个核心界面及简要说明，另有 ECAM 搜索与复位的演示视频。"',
    '"A330 Tools is designed for training and reference use only. It does not replace official Airbus documentation. ECAM messages, reset procedures, structural damage reports, and AMM/MEL/ESPM references are provided as learning aids. Always consult the latest official Airbus manuals before performing any maintenance or operational task. Airbus and A330 are trademarks of their respective owners and are not affiliated with this app."':
        '"A330 Tools 仅供培训和参考使用，不能替代空客官方文件。ECAM 信息、复位程序、结构损伤报告以及 AMM/MEL/ESPM 参考仅作为学习辅助资料。在执行任何维修或运行工作前，请务必查阅最新的空客官方手册。Airbus 和 A330 是其各自所有者的商标，与本应用无关联。"',
    '"Central hub for Airbus A330 family maintenance."': '"空客 A330 系列维修的一站式入口。"',
    '"Search any A330 ECAM message and get the full reset: step-by-step procedure, circuit breakers with panel location and photos, and a built-in live timer."':
        '"搜索任意 A330 ECAM 信息即可获得完整复位方案：分步程序、跳开关及其面板位置和照片，并内置实时计时器。"',

    # ── 737 Tools ───────────────────────────────────────────────────────────
    '"737 Tools · Annunciator Lights | Boeing 737 NG Maintenance App"': '"737 Tools · 告警灯 | 波音 737 NG 维修应用"',
    'name: "737 Tools · Annunciator Lights"': 'name: "737 Tools · 告警灯"',
    '"Annunciator lights, E/E tour, circuit breakers & part numbers. Offline."':
        '"告警灯、电子设备舱导览、跳开关与件号，离线可用。"',
    '"On the ramp you don\'t have time to dig through binders. 737 Tools takes you from an annunciator light straight to the exact procedure, CB and LRU photo in seconds — built for gloved hands, working fully offline with no signal needed."':
        '"在机坪上，你没有时间翻手册。737 Tools 让你从一盏告警灯直接找到准确的程序、跳开关和 LRU 照片，只需几秒——专为戴手套操作设计，完全离线，无需信号。"',
    '"Boeing 737 NG maintenance app: annunciator lights by ATA chapter, MEL due-date calculator, E/E tour, circuit breakers and part numbers. Offline."':
        '"波音 737 NG 维修应用：按 ATA 章节整理的告警灯、MEL 到期日计算器、电子设备舱导览、跳开关和件号，离线可用。"',
    '"A look inside the app, module by module, plus video demos of the annunciator light search and the E/E tour."':
        '"逐个模块了解应用，另有告警灯搜索和电子设备舱导览的演示视频。"',
    '"For training and reference only. Designed for aircraft systems study and fault simulation. Information may not be current or fleet-specific. This independent app is not affiliated with any manufacturer and does not replace approved AMM, MEL, or official documentation."':
        '"仅供培训和参考。本应用用于飞机系统学习和故障模拟，信息可能不是最新的，也可能不适用于特定机队。本独立应用与任何制造商均无关联，不能替代批准的 AMM、MEL 或官方文件。"',
    '"737 NG maintenance training and quick reference, in one place."': '"737 NG 维修培训与快速参考，一站搞定。"',
    '"PROCEDURE, COMPUTERS & CBs"': '"程序、计算机与跳开关"',
    '"Check the procedure and find the computer and circuit breakers with real photos."': '"查看程序，并通过真实照片找到计算机和跳开关。"',
    '"Structural damage report form with PDF generator."': '"结构损伤报告表单，可生成 PDF。"',
    'title: "ANNUNCIATOR LIGHTS"': 'title: "告警灯"',
    '"Know what the light means, by ATA chapter."': '"按 ATA 章节了解每盏灯的含义。"',
    'title: "COMMON PN"': 'title: "常用件号"',
    '"Your part numbers, always at hand."': '"你的件号，随时在手。"',
    'title: "E/E TOUR"': 'title: "电子设备舱导览"',
    '"Locate the box with real aircraft images."': '"通过真实飞机照片找到设备位置。"',
    '"ANNUNCIATOR LIGHT SEARCH"': '"告警灯搜索"',
    '"Find an annunciator light and see its procedure, related circuit breakers with panel photos, and computers."':
        '"找到告警灯，查看其程序、相关跳开关的面板照片以及相关计算机。"',
    '"E/E COMPARTMENT TOUR"': '"电子设备舱导览"',
    '"Browse the E/E bay and cockpit CB panels by area and see exactly where each LRU sits on real aircraft photos."':
        '"按区域浏览电子设备舱和驾驶舱跳开关面板，在真实飞机照片上看清每个 LRU 的准确位置。"',
    'title: "Annunciator Lights"': 'title: "告警灯"',
    '"Every 737 NG annunciator light by ATA chapter: what it means, the associated procedure, fault modes, LRUs involved, related circuit breakers, linked MEL items with a NO DISPATCH warning, and your own notes. Includes an MEL due-date calculator that works in UTC."':
        '"按 ATA 章节收录每一盏 737 NG 告警灯：含义、相关程序、故障模式、涉及的 LRU、相关跳开关、带 NO DISPATCH（不可放行）警告的关联 MEL 项目，以及你自己的笔记。内置按 UTC 计算的 MEL 到期日计算器。"',
    'title: "E/E Tour"': 'title: "电子设备舱导览"',
    '"A photographic walkthrough of the electrical and electronic compartment. Real bay photos with each LRU position marked on top, plus the circuit breaker panels with the exact position of every CB."':
        '"电子电气设备舱的照片式导览。在真实的设备架照片上标出每个 LRU 的位置，跳开关面板上也标出了每个跳开关的准确位置。"',
    'title: "Circuit Breakers"': 'title: "跳开关"',
    '"Search any circuit breaker and open the panel viewer with its location pinpointed."': '"搜索任意跳开关，打开面板视图即可精确定位。"',
    'title: "Common PN"': 'title: "常用件号"',
    '"Frequently used part numbers organised by aircraft zone and category, each with a photo. Create your own entries with photos and notes, and import or export your collection to share it with colleagues."':
        '"常用件号按飞机区域和类别整理，每个都附照片。可添加带照片和备注的自定义条目，并导入或导出你的清单与同事分享。"',
    'title: "Damage Reports"': 'title: "损伤报告"',
    '"Build damage reports on the spot: camera photos, annotations, measurements and damage location. Export to PDF or ZIP to send by email."':
        '"现场编制损伤报告：相机照片、标注、测量数据和损伤位置。导出为 PDF 或 ZIP，通过邮件发送。"',
    'title: "Global Search"': 'title: "全局搜索"',
    '"One search box across annunciator lights, LRUs, circuit breakers and part numbers at once. Everything is embedded in the app, so it works with no signal on the ramp or in the hangar."':
        '"一个搜索框同时搜索告警灯、LRU、跳开关和件号。所有数据都内置在应用中，在机坪或机库没有信号也能使用。"',

    # Structured data feature lists in <head>
    '"ECAM Troubleshooting, ECAM Resets, Structural Damage Reports, Electrical Contacts, Alpha Callups, Common Part Numbers"':
        '"ECAM 排故, ECAM 复位, 结构损伤报告, 电气触点, Alpha Callups, 常用件号"',
    '"Annunciator Lights by ATA Chapter, MEL Due Date Calculator, E/E Compartment Photo Tour, Circuit Breaker Panels, Common Part Numbers, Damage Reports, Offline Global Search"':
        '"按 ATA 章节的告警灯, MEL 到期日计算器, 电子设备舱照片导览, 跳开关面板, 常用件号, 损伤报告, 离线全局搜索"',
}

# <head> of each Chinese page (crawlers read these before any script runs).
HEAD = {
    "hub": {
        "title": "A32X Tools | 空客 A320、A330 与波音 737 维修应用",
        "description": "面向空客 A320、A330 和波音 737 NG 的专业维修应用：ECAM 复位、告警灯、结构损伤报告和件号，支持 iOS 和 Android。",
    },
    "a32x": {
        "title": "A32X Tools | 空客 A320 ECAM 复位应用",
        "description": "空客 A320 系列维修应用：ECAM 排故与复位、结构损伤报告、电气触点、Alpha Callups 和常用件号。",
    },
    "a330": {
        "title": "A330 Tools | 空客 A330 ECAM 复位应用",
        "description": "空客 A330 维修应用：ECAM 排故与复位、结构损伤报告、电气触点、Alpha Callups 和常用件号。",
    },
    "b737": {
        "title": "737 Tools · 告警灯 | 波音 737 NG 维修应用",
        "description": "波音 737 NG 维修应用：按 ATA 章节整理的告警灯、MEL 到期日计算器、电子设备舱导览、跳开关和件号，离线可用。",
    },
}

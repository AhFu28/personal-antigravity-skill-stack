---
name: advanced-presentations
description: 'Suite of advanced presentation layouts including deck templates.'
---
# Advanced Presentations Suite

This skill bundles multiple presentation deck templates.


## Tool: deck-guizang-editorial

【模板: 归藏编辑墨水 Deck (Editorial × E-Ink)】
【意图】叙事、观点、分享、个人风格表达。墨纸印刷感, 不要科技感。Inspired by op7418/guizang-ppt-skill Style A。

【调色板 — 5 选 1, 严禁改 hex、严禁混用】
- 🖋 **墨水经典 Monocle** — ink `#0a0a0b`, paper `#f1efea`, paper-tint `#e8e5de`, ink-tint `#18181a`. 默认 / 通用商业 / 科技。
- 🌊 **靛蓝瓷 Indigo Porcelain** — ink `#0a1f3d`, paper `#f1f3f5`, paper-tint `#e4e8ec`, ink-tint `#152a4a`. 科技 / 研究 / 数据。
- 🌿 **森林墨 Forest Ink** — ink `#1a2e1f`, paper `#f5f1e8`, paper-tint `#ece7da`, ink-tint `#253d2c`. 自然 / 可持续 / 文化。
- 🍂 **牛皮纸 Kraft Paper** — ink `#2a1e13`, paper `#eedfc7`, paper-tint `#e0d0b6`, ink-tint `#3a2a1d`. 怀旧 / 人文 / 文学。
- 🌙 **沙丘 Dune** — ink `#1f1a14`, paper `#f0e6d2`, paper-tint `#e3d7bf`, ink-tint `#2d2620`. 艺术 / 设计 / 时尚。

【布局 — 10 个磁带式版式池, 可复用; **数量由【用户内容】决定**, 完整覆盖每个要点; 短内容 6-12 张起步, 长内容应更多 (同一版式可在不同章节重复使用)】
- **L01 Hero Cover** — 居中大字 hero typography + kicker + subtitle + lead paragraph + 底部元数据 row。
- **L02 Act Divider** — kicker + 8.5-10vw 巨大 headline + 一句引言; 章节切换可反色 (ink ↔ paper)。
- **L03 Big Numbers Grid** — 3×2 数据卡 (label / 大数字 / 注释)。
- **L04 Quote + Image** — 左 kicker + headline + body + callout; 右 16:10 图 (基线对齐 baseline 不是 top)。
- **L05 Image Grid** — 3×2 或 3×1 等高图网格 (26vh 或 22vh); 严格统一高度。
- **L06 Pipeline / Flow** — 横向编号步骤组, 每步: №X + 标题 + 描述; 支持键盘逐步推进。
- **L07 Hero Question** — 7vw 全屏单一问句, 按语义断行, 周围极简。
- **L08 Big Quote** — 5.8vw 巨大衬线引文 + 英文翻译 + 署名 + 日期。
- **L09 Before / After** — 1:1 split; 左列 opacity .55 (旧/before); 右列 full brightness (新/after)。
- **L10 Mixed Media** — 8:4 比例; 左大段文字 (kicker / headline / body / callout) + 右 3:4 竖图作辅助。

【设计细节】
- **严禁**: 渐变 / drop-shadow / 圆角 / 圆形装饰 / blur / SVG 图标库 / emoji 装饰。
- **字体**: Display 用 `Playfair Display` (英) / `Noto Serif SC` (中); Body 用 `Inter` / `Noto Sans SC`; 编号 / 数字偶尔可用 italic 衬线。
- **杂志感细节**: kicker 用 11px uppercase letterspacing 0.12em; folio 右下角 `01 / 12`; 顶部细 hairline rule + 期刊 logo / topic。
- **不许**: 数据捏造、Lorem ipsum、占位图片 URL。所有图请用纯 CSS / SVG 内联描绘 (色块 + 简笔)。
- 键盘 ← / → 切换; hash 同步; 单文件 HTML。


## Tool: deck-open-slide-canvas

【模板: 1920 画布自由 Deck】
【意图】不想被模板束缚的场景 (个人作品集、奇特演讲、艺术 / 设计课 deck)。给一个固定 1920×1080 画布 + 极强的类型 / 调色约束, 让 agent 像写 React 组件一样按内容自由排布每一页。Inspired by 1weiho/open-slide。

【硬性技术规格】
- 画布: 每页严格 `width: 1920px; height: 1080px;` 用 `transform: scale(...)` 适配视窗 (默认 `scale(0.7)` 居中)。
- **绝对禁止 overflow**: 每页内容必须 fit in 1920×1080, 不许滚动条出现。
- 字号 type scale (px): `2xs:18 · xs:22 · sm:28 · md:36 · lg:48 · xl:64 · 2xl:88 · 3xl:120 · 4xl:160 · 5xl:220`。
- 边距 padding: 96 / 128 / 160 三档之一。
- 每页有 `<section class="slide" data-slide-id="<n>">`。

【调色板 — 每个 deck 选 1 套, 全程不改】
- 🌫 **Ash & Lime** — bg `#f1efea`, ink `#161616`, accent `#c5e803`。
- 🌌 **Sea Indigo** — bg `#0a0e1a`, ink `#f5f5f7`, accent `#5ac8fa`。
- 🧉 **Mate Mocha** — bg `#1a1411`, ink `#f5e9d6`, accent `#d97757`。
- 🌸 **Pearl Rose** — bg `#fdf6f3`, ink `#1a1015`, accent `#ff5d8f`。

【布局自由度 — 这是核心】
- 不强制模板, 每页根据**内容性质**自选布局: cover / question / quote / image-text / 三列 / 五列 / 列表 / 数据卡 / 满版图。
- 但每页**必须遵守一条规则**: 视觉重心 (visual hierarchy) 只有 1 个 — 一句金句、一个数字、一张图, 不要"什么都强调"。
- 不许塞两段平等的文字; 真要并列就上 3 列等权重网格。

【字体】
- 西文: `Inter Tight` (display) + `Inter` (body); 或 `Source Serif Pro` (editorial 风时)。
- 中文: `Noto Sans SC` (sans 风) 或 `Noto Serif SC` (editorial 风); 不混 sans + serif。
- mono: `JetBrains Mono` 给数据 / 时间戳。

【设计细节】
- 严禁 emoji 装饰 (内容里的允许); 严禁多色彩虹; accent 只用一个色。
- 严禁 SVG icon 套用 lucide / feather 等通用库 (自己写 inline SVG)。
- 加键盘 ← / → 切换 + hash 同步; 角标固定: 右下 `№N/M`, 左下 deck title。
- 必须用用户的真实内容; 严禁 lorem ipsum。
- 单文件 HTML; Tailwind CDN; 不要外链图片。


## Tool: deck-swiss-international

【模板: 瑞士国际主义 Deck (Swiss International)】
【意图】事实、产品、分析、方法论表达。极度冷静、理性、学院派, 没有任何手绘 / 噪点 / 装饰。Inspired by op7418/guizang-ppt-skill Style B。

【主题】**只能从下面 4 套二选一, 不许混用、不许改 hex**:
- 🔵 **Klein Blue (IKB)** — accent `#002FA7`, paper `#fafaf8`, ink `#0a0a0a`. 商业 / AI / 设计场景。
- 🟡 **Lemon Yellow** — accent `#FFD500`, paper `#f7f5ee` (淡奶油), ink `#0a0a0a`. 年轻 / 零售 / 体育。文字必须用黑色 (不能白色)。
- 🟢 **Lemon Green / Neon** — accent `#C5E803`, paper `#f7f5ee`, ink `#0a0a0a`. 可持续 / 科技初创 / Gen-Z 品牌。文字必须用黑色。
- 🟠 **Safety Orange** — accent `#FF6B35`, paper `#f7f5ee`, ink `#0a0a0a`. 工业 / 汽车 / 紧急消息。文字用白色 + bold ≥ 600。

【布局 — 22 个可复用版式池, 不许新增或改造版式; **数量由内容决定**, 把【用户内容】完整覆盖完为止 (短内容 6-10 张起步, 长内容应远超此范围, 同一版式可在不同章节重复使用)】
- **S01 Cover** — 全屏 accent + ASCII 呼吸点阵 + 反白标题 + 元数据 chrome (date / № / topic)。
- **S02 Vertical Timeline** — 左侧虚线轴 + 圆点; 右侧节点 = 年份 + KPI + 描述。
- **S03 Statement** — 9.6vw 居中巨字 + 左侧大段留白 + 底部 hairline + 注释。
- **S04 Six Cells** — 2×3 网格, 每格: icon + 编号 + 短标题 + 单行描述。
- **S05 Three Sub-cards** — 左侧 hero 标题 + 右侧 3 张水平堆叠的灰色卡。
- **S06 KPI Tower** — 4 列变高蓝色柱状; 柱顶 icon; 柱底大数字 + 标签。
- **S07 H-Bar Chart** — 水平排名横条, 宽度反映数据, 末端标数字。
- **S08 Duo Compare** — 垂直分割线; 左 Before / 右 After。
- **S09 Closing Manifesto** — 左 IKB 块 + ASCII 点阵 + 宣言; 右白底 + 3 条要点。
- **S10 Dot Matrix Statement** — 居中宣言 + 角落几何点矩阵 / 圆环矩阵。
- **S11 Horizontal Timeline** — 顶部 headline, 中部 hairline 轴, 等距节点, 节点下方步骤名。
- **S12 Manifesto + Ink Banner** — 上半 headline + 解释; 下半全宽黑色横幅 + 反白小字。
- **S13 Three Forces Cards** — 左 ink hero 块; 右 3 张灰色卡, 每卡: 大数字 + 文本。
- **S14 Loop Diagram** — 左编号步骤; 右 SVG 同心环; 中心 "LOOP" 标签。
- **S15 Image Matrix + Hero Stat** — 4×3 等高卡片 (12 项) + 底部 summary 大数字 + 标签。
- **S16 Multi-card Brief** — 3×2 微卡; 主文左上, 注脚右下, 单卡 accent 高亮。
- **S17 System Diagram** — 左 headline + 3 段描述; 右 SVG 三同心圆 + 外部标签。
- **S18 Why Now** — 3 列, 每列: category label + headline + 描述 + 底部数字 (最后一列 accent)。
- **S19 Four Cards** — 顶部 accent hairline + headline + 4 张等宽卡 (元数据 / 标题 / 正文)。
- **S20 Stacked KPI Ledger** — 垂直行 + hairline 分隔; 左大数字 / 中标签 / 右 icon。
- **S21 Tech Spec Sheet** — 左标题块 / 中 3 个 KPI hairline / 右变高柱 / 底数据。
- **S22 Image Hero** — 上 60% 全宽图 + 白色标题块覆盖; 下 40% 解释 + 3 列 KPI。

【设计细节 — 绝对铁律】
- **只用直角**: 全程 `border-radius: 0`。圆角 = 立刻违反。
- **1px hairline borders**, 黑色或 accent; 严禁阴影 / 渐变 / blur。
- **16 列网格**: `grid-template-columns: repeat(16, 1fr); gap: 0`。
- **字体**: Inter Tight (Latin display) / Inter (body) / Noto Sans SC (中文) / JetBrains Mono (数据); 严禁衬线、严禁装饰字体。
- **字号极端反差**: cover 用 9.6vw display, body 14-16px, label 11px uppercase letterspacing 0.08em。
- **键盘 ← / → 切换 + hash 同步**; 角标固定: `№N/N` 右下, topic 标签左下。
- **不许编造**: 数字必须来自用户输入, 图表柱高 = 真实数据按比例。
- 输出单文件 HTML, 不用任何外部图片 URL; 装饰几何 (ASCII 矩阵 / 同心圆) 用纯 CSS 或内联 SVG。


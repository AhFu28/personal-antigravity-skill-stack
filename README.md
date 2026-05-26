# 🚀 My Personal Agent Skills Repository

Welcome to my personal AI Agent Skills repository. This documentation outlines all my currently installed skills, their primary usages, and example triggers.

## 📊 Current Skill Capacity
- **Currently Installed:** 79 Skills
- **Pending Installation:** 14 Skills
- **Total Post-Install:** 93 Skills
- **System Limit:** The AI context window generally handles up to ~120-150 skills comfortably depending on description length. You are at **93**, which is well within the safe operational limit! No performance degradation will occur.

## 🗂️ Installed Skills Inventory

### 🛠️ backtest-expert
**Description / Usage:** Expert guidance for systematic backtesting of trading strategies. Use when developing, testing, stress-testing, or validating quantitative trading strategies. Covers "beating ideas to death" methodology, parameter robustness testing, slippage modeling, bias prevention, and interpreting backtest results. Applicable when user asks about backtesting, strategy validation, robustness testing, avoiding overfitting, or systematic trading development.

**Example Case:** 'Please use the backtest-expert skill to process my request.'

---

### 🛠️ breadth-chart-analyst
**Description / Usage:** This skill should be used when analyzing market breadth charts, specifically the S&P 500 Breadth Index (200-Day MA based) and the US Stock Market Uptrend Stock Ratio charts. Use this skill when the user provides breadth chart images for analysis, requests market breadth assessment, positioning strategy recommendations, or wants to understand medium-term strategic and short-term tactical market outlook based on breadth indicators. Also works WITHOUT chart images by fetching CSV data directly from public sources. All analysis and output are conducted in English.

**Example Case:** 'Please use the breadth-chart-analyst skill to process my request.'

---

### 🛠️ breakout-trade-planner
**Description / Usage:** Generate Minervini-style breakout trade plans from VCP screener output with worst-case risk calculation, portfolio heat management, and Alpaca-compatible order templates (stop-limit bracket for pre-placement, limit bracket for post-confirmation). Use when user has VCP screener results and wants actionable trade plans with entry/stop/target levels and position sizing.

**Example Case:** 'Please use the breakout-trade-planner skill to process my request.'

---

### 🛠️ canslim-screener
**Description / Usage:** Screen US stocks using William O'Neil's CANSLIM growth stock methodology. Use when user requests CANSLIM stock screening, growth stock analysis, momentum stock identification, or wants to find stocks with strong earnings and price momentum following O'Neil's investment system.

**Example Case:** 'Run the canslim-screener to find matching stocks.'

---

### 🛠️ company-valuation
**Description / Usage:** >

**Example Case:** 'Please use the company-valuation skill to process my request.'

---

### 🛠️ cs-content-creator
**Description / Usage:** AI-powered content creation specialist for brand voice consistency, SEO optimization, and multi-platform content strategy

**Example Case:** 'Please use the cs-content-creator skill to process my request.'

---

### 🛠️ cs-demand-gen-specialist
**Description / Usage:** Demand generation and customer acquisition specialist for lead generation, conversion optimization, and multi-channel acquisition campaigns

**Example Case:** 'Please use the cs-demand-gen-specialist skill to process my request.'

---

### 🛠️ data-quality-checker
**Description / Usage:** Validate data quality in market analysis documents and blog articles before publication. Use when checking for price scale inconsistencies (ETF vs futures), instrument notation errors, date/day-of-week mismatches, allocation total errors, and unit mismatches. Supports English and Japanese content. Advisory mode -- flags issues as warnings for human review, not as blockers.

**Example Case:** 'Please use the data-quality-checker skill to process my request.'

---

### 🛠️ dividend-growth-pullback-screener
**Description / Usage:** Use this skill to find high-quality dividend growth stocks (12%+ annual dividend growth, 1.5%+ yield) that are experiencing temporary pullbacks, identified by RSI oversold conditions (RSI â‰¤40). This skill combines fundamental dividend analysis with technical timing indicators to identify buying opportunities in strong dividend growers during short-term weakness.

**Example Case:** 'Run the dividend-growth-pullback-screener to find matching stocks.'

---

### 🛠️ docx
**Description / Usage:** Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

**Example Case:** 'Please use the docx skill to process my request.'

---

### 🛠️ downtrend-duration-analyzer
**Description / Usage:** Analyze historical downtrend durations and generate interactive HTML histograms showing typical correction lengths by sector and market cap.

**Example Case:** 'Analyze this data using downtrend-duration-analyzer.'

---

### 🛠️ dual-axis-skill-reviewer
**Description / Usage:** Review skills in any project using a dual-axis method: (1) deterministic code-based checks (structure, scripts, tests, execution safety) and (2) LLM deep review findings. Use when you need reproducible quality scoring for `skills/*/SKILL.md`, want to gate merges with a score threshold (for example 90+), or need concrete improvement items for low-scoring skills. Works across projects via --project-root.

**Example Case:** 'Please use the dual-axis-skill-reviewer skill to process my request.'

---

### 🛠️ earnings-calendar
**Description / Usage:** This skill retrieves upcoming earnings announcements for US stocks using the Financial Modeling Prep (FMP) API. Use this when the user requests earnings calendar data, wants to know which companies are reporting earnings in the upcoming week, or needs a weekly earnings review. The skill focuses on mid-cap and above companies (over $2B market cap) that have significant market impact, organizing the data by date and timing in a clean markdown table format. Supports multiple environments (CLI, Desktop, Web) with flexible API key management.

**Example Case:** 'Please use the earnings-calendar skill to process my request.'

---

### 🛠️ earnings-preview
**Description / Usage:** >

**Example Case:** 'Please use the earnings-preview skill to process my request.'

---

### 🛠️ earnings-recap
**Description / Usage:** >

**Example Case:** 'Please use the earnings-recap skill to process my request.'

---

### 🛠️ earnings-trade-analyzer
**Description / Usage:** Analyze recent post-earnings stocks using a 5-factor scoring system (Gap Size, Pre-Earnings Trend, Volume Trend, MA200 Position, MA50 Position). Scores each stock 0-100 and assigns A/B/C/D grades. Use when user asks about earnings trade analysis, post-earnings momentum screening, earnings gap scoring, or finding best recent earnings reactions.

**Example Case:** 'Analyze this data using earnings-trade-analyzer.'

---

### 🛠️ economic-calendar-fetcher
**Description / Usage:** Fetch upcoming economic events and data releases using FMP API. Retrieve scheduled central bank decisions, employment reports, inflation data, GDP releases, and other market-moving economic indicators for specified date ranges (default: next 7 days). The script outputs raw JSON or text; the assistant filters, assesses impact, and generates the Markdown report.

**Example Case:** 'Please use the economic-calendar-fetcher skill to process my request.'

---

### 🛠️ edge-candidate-agent
**Description / Usage:** Generate and prioritize US equity long-side edge research tickets from EOD observations, then export pipeline-ready candidate specs for trade-strategy-pipeline Phase I. Use when users ask to turn hypotheses/anomalies into reproducible research tickets, convert validated ideas into `strategy.yaml` + `metadata.json`, or preflight-check interface compatibility (`edge-finder-candidate/v1`) before running pipeline backtests.

**Example Case:** 'Please use the edge-candidate-agent skill to process my request.'

---

### 🛠️ edge-concept-synthesizer
**Description / Usage:** Abstract detector tickets and hints into reusable edge concepts with thesis, invalidation signals, and strategy playbooks before strategy design/export.

**Example Case:** 'Please use the edge-concept-synthesizer skill to process my request.'

---

### 🛠️ edge-hint-extractor
**Description / Usage:** Extract edge hints from daily market observations and news reactions, with optional LLM ideation, and output canonical hints.yaml for downstream concept synthesis and auto detection.

**Example Case:** 'Please use the edge-hint-extractor skill to process my request.'

---

### 🛠️ edge-pipeline-orchestrator
**Description / Usage:** Orchestrate the full edge research pipeline from candidate detection through strategy design, review, revision, and export. Use when coordinating multi-stage edge research workflows end-to-end.

**Example Case:** 'Please use the edge-pipeline-orchestrator skill to process my request.'

---

### 🛠️ edge-signal-aggregator
**Description / Usage:** Aggregate and rank signals from multiple edge-finding skills (edge-candidate-agent, theme-detector, sector-analyst, institutional-flow-tracker) into a prioritized conviction dashboard with weighted scoring, deduplication, and contradiction detection.

**Example Case:** 'Please use the edge-signal-aggregator skill to process my request.'

---

### 🛠️ edge-strategy-designer
**Description / Usage:** Convert abstract edge concepts into strategy draft variants and optional exportable ticket YAMLs for edge-candidate-agent export/validation.

**Example Case:** 'Please use the edge-strategy-designer skill to process my request.'

---

### 🛠️ edge-strategy-reviewer
**Description / Usage:** >

**Example Case:** 'Please use the edge-strategy-reviewer skill to process my request.'

---

### 🛠️ estimate-analysis
**Description / Usage:** >

**Example Case:** 'Please use the estimate-analysis skill to process my request.'

---

### 🛠️ etf-premium
**Description / Usage:** >

**Example Case:** 'Please use the etf-premium skill to process my request.'

---

### 🛠️ exposure-coach
**Description / Usage:** Generate a one-page Market Posture summary with net exposure ceiling, growth-vs-value bias, participation breadth, and new-entry-allowed vs cash-priority recommendation by integrating signals from breadth, regime, and flow analysis skills.

**Example Case:** 'Give me feedback based on exposure-coach.'

---

### 🛠️ finance-sentiment
**Description / Usage:** >

**Example Case:** 'Please use the finance-sentiment skill to process my request.'

---

### 🛠️ finviz-screener
**Description / Usage:** Build and open FinViz screener URLs from natural language requests. Use when user wants to screen stocks, find stocks matching criteria, filter by fundamentals or technicals, or asks to open FinViz with specific conditions. Supports both Japanese and English input (e.g., "é«˜é…å½“ã§æˆé•·ã—ã¦ã„ã‚‹å°åž‹æ ªã‚’æŽ¢ã—ãŸã„", "Find oversold large caps with high ROE").

**Example Case:** 'Run the finviz-screener to find matching stocks.'

---

### 🛠️ ftd-detector
**Description / Usage:** Detects Follow-Through Day (FTD) signals for market bottom confirmation using William O'Neil's methodology. Dual-index tracking (S&P 500 + NASDAQ) with state machine for rally attempt, FTD qualification, and post-FTD health monitoring. Use when user asks about market bottom signals, follow-through days, rally attempts, re-entry timing after corrections, or whether it's safe to increase equity exposure. Complementary to market-top-detector (defensive) - this skill is offensive (bottom confirmation).

**Example Case:** 'Please use the ftd-detector skill to process my request.'

---

### 🛠️ funda-data
**Description / Usage:** >

**Example Case:** 'Please use the funda-data skill to process my request.'

---

### 🛠️ hormuz-strait
**Description / Usage:** >

**Example Case:** 'Please use the hormuz-strait skill to process my request.'

---

### 🛠️ ibd-distribution-day-monitor
**Description / Usage:** Detect IBD-style Distribution Days for QQQ/SPY (close down at least 0.2% on higher volume), track 25-session expiration and 5% invalidation, count d5/d15/d25 clusters, classify market risk (NORMAL/CAUTION/HIGH/SEVERE), and emit TQQQ/QQQ exposure recommendations. Use after market close, before TQQQ exposure changes, or as input to FTD/market-state frameworks. Does not execute trades.

**Example Case:** 'Please use the ibd-distribution-day-monitor skill to process my request.'

---

### 🛠️ institutional-flow-tracker
**Description / Usage:** Use this skill to track institutional investor ownership changes and portfolio flows using 13F filings data. Analyzes hedge funds, mutual funds, and other institutional holders to identify stocks with significant smart money accumulation or distribution. Helps discover stocks before major moves by following where sophisticated investors are deploying capital.

**Example Case:** 'Please use the institutional-flow-tracker skill to process my request.'

---

### 🛠️ macro-regime-detector
**Description / Usage:** Detect structural macro regime transitions (1-2 year horizon) using cross-asset ratio analysis. Analyze RSP/SPY concentration, yield curve, credit conditions, size factor, equity-bond relationship, and sector rotation to identify regime shifts between Concentration, Broadening, Contraction, Inflationary, and Transitional states. Run when user asks about macro regime, market regime change, structural rotation, or long-term market positioning.

**Example Case:** 'Please use the macro-regime-detector skill to process my request.'

---

### 🛠️ market-breadth-analyzer
**Description / Usage:** Quantifies market breadth health using TraderMonty's public CSV data. Generates a 0-100 composite score across 6 components (100 = healthy). No API key required. Use when user asks about market breadth, participation rate, advance-decline health, whether the rally is broad-based, or general market health assessment.

**Example Case:** 'Analyze this data using market-breadth-analyzer.'

---

### 🛠️ market-environment-analysis
**Description / Usage:** Comprehensive market environment analysis and reporting tool. Analyzes global markets including US, European, Asian markets, forex, commodities, and economic indicators. Provides risk-on/risk-off assessment, sector analysis, and technical indicator interpretation. Triggers on keywords like market analysis, market environment, global markets, trading environment, market conditions, investment climate, market sentiment, forex analysis, stock market analysis, ç›¸å ´ç’°å¢ƒ, å¸‚å ´åˆ†æž, ãƒžãƒ¼ã‚±ãƒƒãƒˆçŠ¶æ³, æŠ•è³‡ç’°å¢ƒ.

**Example Case:** 'Please use the market-environment-analysis skill to process my request.'

---

### 🛠️ market-news-analyst
**Description / Usage:** This skill should be used when analyzing recent market-moving news events and their impact on equity markets and commodities. Use this skill when the user requests analysis of major financial news from the past 10 days, wants to understand market reactions to monetary policy decisions (FOMC, ECB, BOJ), needs assessment of geopolitical events' impact on commodities, or requires comprehensive review of earnings announcements from mega-cap stocks. The skill automatically collects news using WebSearch/WebFetch tools and produces impact-ranked analysis reports. All analysis thinking and output are conducted in English.

**Example Case:** 'Please use the market-news-analyst skill to process my request.'

---

### 🛠️ market-top-detector
**Description / Usage:** Detects market top probability using O'Neil Distribution Days, Minervini Leading Stock Deterioration, and Monty Defensive Sector Rotation. Generates a 0-100 composite score with risk zone classification. Use when user asks about market top risk, distribution days, defensive rotation, leadership breakdown, or whether to reduce equity exposure. Focuses on 2-8 week tactical timing signals for 10-20% corrections.

**Example Case:** 'Please use the market-top-detector skill to process my request.'

---

### 🛠️ options-payoff
**Description / Usage:** >

**Example Case:** 'Please use the options-payoff skill to process my request.'

---

### 🛠️ options-strategy-advisor
**Description / Usage:** Options trading strategy analysis and simulation tool. Provides theoretical pricing using Black-Scholes model, Greeks calculation, strategy P/L simulation, and risk management guidance. Use when user requests options strategy analysis, covered calls, protective puts, spreads, iron condors, earnings plays, or options risk management. Includes volatility analysis, position sizing, and earnings-based strategy recommendations. Educational focus with practical trade simulation.

**Example Case:** 'Please use the options-strategy-advisor skill to process my request.'

---

### 🛠️ pair-trade-screener
**Description / Usage:** Statistical arbitrage tool for identifying and analyzing pair trading opportunities. Detects cointegrated stock pairs within sectors, analyzes spread behavior, calculates z-scores, and provides entry/exit recommendations for market-neutral strategies. Use when user requests pair trading opportunities, statistical arbitrage screening, mean-reversion strategies, or market-neutral portfolio construction. Supports correlation analysis, cointegration testing, and spread backtesting.

**Example Case:** 'Run the pair-trade-screener to find matching stocks.'

---

### 🛠️ parabolic-short-trade-planner
**Description / Usage:** Screen US equities for parabolic exhaustion patterns and generate conditional pre-market short plans, then evaluate intraday trigger fires from live 5-min bars. Phase 1 daily 5-factor scorer (MA extension / acceleration / volume climax / range expansion / liquidity), Phase 2 per-candidate plans for ORL break / first-red 5-min / VWAP fail with explicit borrow / SSR / manual-confirmation gating, Phase 3 one-shot intraday FSM that detects trigger fires and resolves concrete share counts. Covers Phase 1 + Phase 2 + Phase 3.

**Example Case:** 'Please use the parabolic-short-trade-planner skill to process my request.'

---

### 🛠️ pdf
**Description / Usage:** Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

**Example Case:** 'Please use the pdf skill to process my request.'

---

### 🛠️ pead-screener
**Description / Usage:** Screen post-earnings gap-up stocks for PEAD (Post-Earnings Announcement Drift) patterns. Analyzes weekly candle formation to detect red candle pullbacks and breakout signals. Supports two input modes - FMP earnings calendar (Mode A) or earnings-trade-analyzer JSON output (Mode B). Use when user asks about PEAD screening, post-earnings drift, earnings gap follow-through, red candle breakout patterns, or weekly earnings momentum setups.

**Example Case:** 'Run the pead-screener to find matching stocks.'

---

### 🛠️ perplexity-follow-up
**Description / Usage:** Always suggest 3 relevant follow-up questions at the end of every response, formatted like Perplexity AI.

**Example Case:** 'Please use the perplexity-follow-up skill to process my request.'

---

### 🛠️ portfolio-manager
**Description / Usage:** Comprehensive portfolio analysis using Alpaca MCP Server integration to fetch holdings and positions, then analyze asset allocation, risk metrics, individual stock positions, diversification, and generate rebalancing recommendations. Use when user requests portfolio review, position analysis, risk assessment, performance evaluation, or rebalancing suggestions for their brokerage account.

**Example Case:** 'Please use the portfolio-manager skill to process my request.'

---

### 🛠️ position-sizer
**Description / Usage:** Calculate risk-based position sizes for long stock trades. Use when user asks about position sizing, how many shares to buy, risk per trade, Kelly criterion, ATR-based sizing, or portfolio risk allocation. Supports stop-loss distance calculation, volatility scaling, and sector concentration checks.

**Example Case:** 'Please use the position-sizer skill to process my request.'

---

### 🛠️ pptx
**Description / Usage:** Use this skill any time a .pptx file is involved in any way â€” as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \

**Example Case:** 'Please use the pptx skill to process my request.'

---

### 🛠️ saas-valuation-compression
**Description / Usage:** >

**Example Case:** 'Please use the saas-valuation-compression skill to process my request.'

---

### 🛠️ scenario-analyzer
**Description / Usage:** |

**Example Case:** 'Analyze this data using scenario-analyzer.'

---

### 🛠️ sector-analyst
**Description / Usage:** This skill should be used when analyzing sector rotation patterns and market cycle positioning. It fetches sector uptrend data from CSV (no API key required) and optionally accepts chart images for supplementary analysis. Use this skill when the user requests sector rotation analysis, cyclical vs defensive assessment, overbought/oversold identification, or market cycle phase estimation. All analysis and output are conducted in English.

**Example Case:** 'Please use the sector-analyst skill to process my request.'

---

### 🛠️ sepa-strategy
**Description / Usage:** >

**Example Case:** 'Please use the sepa-strategy skill to process my request.'

---

### 🛠️ sharp
**Description / Usage:** Process images with the Sharp library for Node.js â€” resize, convert formats, composite, apply effects, and manage metadata. Use when the user mentions "sharp", "image processing", "resize image", "convert image", "image format", "jpeg quality", "png compression", "webp", "avif", "image thumbnail", "crop image", "watermark", "overlay image", "blur image", "sharpen image", "image metadata", "EXIF", "ICC profile", "colour space", "alpha channel", "animated gif", "image pipeline", or asks how to manipulate images in Node.js/TypeScript. Also use for "sharp constructor", "sharp cache", "sharp concurrency", "toFile", "toBuffer", or any Sharp API method.

**Example Case:** 'Please use the sharp skill to process my request.'

---

### 🛠️ signal-postmortem
**Description / Usage:** Record and analyze post-trade outcomes for signals generated by edge pipeline and other skills. Track false positives, missed opportunities, and regime mismatches. Feed results back to edge-signal-aggregator weights and skill improvement backlog.

**Example Case:** 'Please use the signal-postmortem skill to process my request.'

---

### 🛠️ skill-designer
**Description / Usage:** Design new Claude skills from structured idea specifications. Use when the skill auto-generation pipeline needs to produce a Claude CLI prompt that creates a complete skill directory (SKILL.md, references, scripts, tests) following repository conventions.

**Example Case:** 'Please use the skill-designer skill to process my request.'

---

### 🛠️ skill-idea-miner
**Description / Usage:** Mine Claude Code session logs for skill idea candidates. Use when running the weekly skill generation pipeline to extract, score, and backlog new skill ideas from recent coding sessions.

**Example Case:** 'Please use the skill-idea-miner skill to process my request.'

---

### 🛠️ skill-integration-tester
**Description / Usage:** Validate multi-skill workflows defined in CLAUDE.md by checking skill existence, inter-skill data contracts (JSON schema compatibility), file naming conventions, and handoff integrity. Use when adding new workflows, modifying skill outputs, or verifying pipeline health before release.

**Example Case:** 'Please use the skill-integration-tester skill to process my request.'

---

### 🛠️ social-media-content-engine
**Description / Usage:** No description found.

**Example Case:** 'Please use the social-media-content-engine skill to process my request.'

---

### 🛠️ stanley-druckenmiller-investment
**Description / Usage:** Druckenmiller Strategy Synthesizer - Integrates 8 upstream skill outputs (Market Breadth, Uptrend Analysis, Market Top, Macro Regime, FTD Detector, VCP Screener, Theme Detector, CANSLIM Screener) into a unified conviction score (0-100), pattern classification, and allocation recommendation. Use when user asks about overall market conviction, portfolio positioning, asset allocation, strategy synthesis, or Druckenmiller-style analysis. Triggers on queries like "What is my conviction level?", "How should I position?", "Run the strategy synthesizer", "Druckenmiller analysis", "ç·åˆçš„ãªå¸‚å ´åˆ¤æ–­", "ç¢ºä¿¡åº¦ã‚¹ã‚³ã‚¢", "ãƒãƒ¼ãƒˆãƒ•ã‚©ãƒªã‚ªé…åˆ†", "ãƒ‰ãƒ©ãƒƒã‚±ãƒ³ãƒŸãƒ©ãƒ¼åˆ†æž".

**Example Case:** 'Please use the stanley-druckenmiller-investment skill to process my request.'

---

### 🛠️ startup-analysis
**Description / Usage:** >

**Example Case:** 'Please use the startup-analysis skill to process my request.'

---

### 🛠️ stock-correlation
**Description / Usage:** >

**Example Case:** 'Please use the stock-correlation skill to process my request.'

---

### 🛠️ stock-liquidity
**Description / Usage:** >

**Example Case:** 'Please use the stock-liquidity skill to process my request.'

---

### 🛠️ strategy-pivot-designer
**Description / Usage:** Detect backtest iteration stagnation and generate structurally different strategy pivot proposals when parameter tuning reaches a local optimum.

**Example Case:** 'Please use the strategy-pivot-designer skill to process my request.'

---

### 🛠️ technical-analyst
**Description / Usage:** This skill should be used when analyzing weekly price charts for stocks, stock indices, cryptocurrencies, or forex pairs. Use this skill when the user provides chart images and requests technical analysis, trend identification, support/resistance levels, scenario planning, or probability assessments based purely on chart data without consideration of news or fundamental factors.

**Example Case:** 'Please use the technical-analyst skill to process my request.'

---

### 🛠️ the-council
**Description / Usage:** Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement before choosing.

**Example Case:** 'Please use the the-council skill to process my request.'

---

### 🛠️ theme-detector
**Description / Usage:** Detect and analyze trending market themes across sectors. Use when user asks about current market themes, trending sectors, sector rotation, thematic investing, what themes are hot or cold, or wants to identify bullish and bearish market narratives with lifecycle analysis.

**Example Case:** 'Please use the theme-detector skill to process my request.'

---

### 🛠️ token-budget-advisor
**Description / Usage:** >-

**Example Case:** 'Please use the token-budget-advisor skill to process my request.'

---

### 🛠️ trade-hypothesis-ideator
**Description / Usage:** >

**Example Case:** 'Please use the trade-hypothesis-ideator skill to process my request.'

---

### 🛠️ trade-performance-coach
**Description / Usage:** >-

**Example Case:** 'Give me feedback based on trade-performance-coach.'

---

### 🛠️ trader-memory-core
**Description / Usage:** Track investment theses across their lifecycle â€” from screening idea to closed position with postmortem. Register theses from screener outputs, manage state transitions, attach position sizing, review due dates, and generate postmortem reports with P&L and MAE/MFE analysis. Trigger when user says "register thesis", "track this idea", "thesis status", "review due", "close position", "postmortem", or "trading journal".

**Example Case:** 'Please use the trader-memory-core skill to process my request.'

---

### 🛠️ trading-skills-navigator
**Description / Usage:** >-

**Example Case:** 'Please use the trading-skills-navigator skill to process my request.'

---

### 🛠️ tradingview-reader
**Description / Usage:** >

**Example Case:** 'Please use the tradingview-reader skill to process my request.'

---

### 🛠️ uptrend-analyzer
**Description / Usage:** Analyzes market breadth using Monty's Uptrend Ratio Dashboard data to diagnose the current market environment. Generates a 0-100 composite score from 5 components (breadth, sector participation, rotation, momentum, historical context). Use when asking about market breadth, uptrend ratios, or whether the market environment supports equity exposure. No API key required.

**Example Case:** 'Analyze this data using uptrend-analyzer.'

---

### 🛠️ us-market-bubble-detector
**Description / Usage:** Evaluates market bubble risk through quantitative data-driven analysis using the revised Minsky/Kindleberger framework v2.1. Prioritizes objective metrics (Put/Call, VIX, margin debt, breadth, IPO data) over subjective impressions. Features strict qualitative adjustment criteria with confirmation bias prevention. Supports practical investment decisions with mandatory data collection and mechanical scoring. Use when user asks about bubble risk, valuation concerns, or profit-taking timing.

**Example Case:** 'Please use the us-market-bubble-detector skill to process my request.'

---

### 🛠️ us-stock-analysis
**Description / Usage:** Comprehensive US stock analysis including fundamental analysis (financial metrics, business quality, valuation), technical analysis (indicators, chart patterns, support/resistance), stock comparisons, and investment report generation. Use when user requests analysis of US stock tickers (e.g., "analyze AAPL", "compare TSLA vs NVDA", "give me a report on Microsoft"), evaluation of financial metrics, technical chart analysis, or investment recommendations for American stocks.

**Example Case:** 'Please use the us-stock-analysis skill to process my request.'

---

### 🛠️ value-dividend-screener
**Description / Usage:** Screen US stocks for high-quality dividend opportunities combining value characteristics (P/E ratio under 20, P/B ratio under 2), attractive yields (3% or higher), and consistent growth (dividend/revenue/EPS trending up over 3 years). Supports two-stage screening using FINVIZ Elite API for efficient pre-filtering followed by FMP API for detailed analysis. Use when user requests dividend stock screening, income portfolio ideas, or quality value stocks with strong fundamentals.

**Example Case:** 'Run the value-dividend-screener to find matching stocks.'

---

### 🛠️ vcp-screener
**Description / Usage:** Screen S&P 500 stocks for Mark Minervini's Volatility Contraction Pattern (VCP). Identifies Stage 2 uptrend stocks forming tight bases with contracting volatility near breakout pivot points. Use when user requests VCP screening, Minervini-style setups, tight base patterns, volatility contraction breakout candidates, or Stage 2 momentum stock scanning.

**Example Case:** 'Run the vcp-screener to find matching stocks.'

---

### 🛠️ xlsx
**Description / Usage:** Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path â€” even casually (like \

**Example Case:** 'Please use the xlsx skill to process my request.'

---

### 🛠️ yfinance-data
**Description / Usage:** >

**Example Case:** 'Please use the yfinance-data skill to process my request.'

---



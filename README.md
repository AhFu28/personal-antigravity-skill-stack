# Antigravity Skills Configuration

A personal, curated collection of 99 AI agent skills used to automate workflows in data analysis, content creation, and personal investing.

---

## Overview

This repository contains my personal configuration for the Antigravity AI environment. Rather than keeping a bloated installation with unnecessary frameworks (like biotech research or complex AI-swarm coding environments), I have narrowed down the skill stack to focus strictly on practical workflows:

1. **Data Analytics:** Querying databases, tracking metrics, and processing datasets.
2. **Content & Digital Projects:** Automating social media planning and generating documents.
3. **Personal Investing:** Fundamental analysis (DCF), market breadth tracking, and swing trading screening.

By archiving heavy dependencies, this setup keeps the AI context window efficient and relevant to daily tasks.

---

## Antigravity Installation

To install any of these skills into your local Antigravity environment:

1. Locate your Antigravity configuration directory (typically `~/.gemini/config/plugins/`). On Windows, this is usually `C:\Users\[YourName]\.gemini\config\plugins\`.
2. Create a custom plugin folder (e.g., `custom-skills`) containing a basic `plugin.json` file.
3. Inside your custom plugin folder, create a `skills` subdirectory (e.g., `~/.gemini/config/plugins/custom-skills/skills/`).
4. Download the specific skill folders from the source repositories linked in the tables below.
5. Place the downloaded skill folders directly into your `skills` directory. 
6. Antigravity will automatically detect the new `SKILL.md` files upon its next initialization.

---

## The Skill Inventory

*All sources link back to their original open-source repositories.*

### 1. Data & Analytics
*Practical tools for processing data, optimizing SQL, and evaluating campaign metrics without relying entirely on manual spreadsheet work.*

| Skill Name | Description | Source |
| :--- | :--- | :--- |
| `analytics-tracking` | Evaluates performance metrics of digital campaigns. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `campaign-analytics` | Analyzes marketing campaign ROI and conversion rates. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `financial-analyst` | Assists with financial data processing and cost modeling. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `product-analytics` | Analyzes product performance metrics and user retention. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `senior-data-scientist` | Assists with data modeling and statistical testing. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `sql-database-assistant`| Helps write, optimize, and debug SQL queries. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `statistical-analyst` | Performs statistical reviews and calculations. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `data-quality-checker` | Validates data scale and units in documents to prevent errors. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |

### 2. Marketing & Content
*Workflows designed to streamline the planning, writing, and strategy behind digital content creation.*

| Skill Name | Description | Source |
| :--- | :--- | :--- |
| `social-media-content-engine`| Structures social media content planning and scripting. | Custom |
| `social-media-analyzer` | Analyzes engagement metrics and audience retention. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `marketing-psychology` | Reviews copywriting based on behavioral psychology principles. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `cs-content-creator` | Assists with content drafting and basic SEO formatting. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `cs-demand-gen-specialist` | Provides frameworks for customer acquisition funnels. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `marketing-demand-acquisition`| Tactical planning for driving traffic to digital platforms. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `marketing-ideas` | Brainstorms marketing angles and promotional ideas. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `marketing-ops` | Suggests workflow automations for digital marketing tools. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `marketing-strategy-pmm` | Frameworks for high-level product positioning and strategy. | [Alireza](https://github.com/alirezarezvani/claude-skills) |

### 3. Project Management
*Tools to help track timelines, organize meeting notes, and structure digital product launches.*

| Skill Name | Description | Source |
| :--- | :--- | :--- |
| `cs-project-manager` | General project management and timeline tracking. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `meeting-analyzer` | Summarizes transcripts to extract action items. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `product-manager` | Digital product management and feature planning frameworks. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `product-manager-toolkit` | Templates for scoping out new digital products. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `project-health` | Monitors ongoing projects for blockers. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `release-manager` | Helps organize software or content release schedules. | [Alireza](https://github.com/alirezarezvani/claude-skills) |
| `report` | Structures status reports for stakeholders. | [Alireza](https://github.com/alirezarezvani/claude-skills) |

### 4. Financial & Fundamental Analysis
*Analytical skills for processing financial statements, reading analyst estimates, and building basic DCF models.*

| Skill Name | Description | Source |
| :--- | :--- | :--- |
| `company-valuation` | Assists with intrinsic value calculations using DCF modeling. | [Himself65](https://github.com/himself65/finance-skills) |
| `earnings-preview` | Compiles pre-earnings briefings and consensus estimates. | [Himself65](https://github.com/himself65/finance-skills) |
| `earnings-recap` | Reviews post-earnings beat/miss data. | [Himself65](https://github.com/himself65/finance-skills) |
| `estimate-analysis` | Tracks analyst EPS and revenue revision trends. | [Himself65](https://github.com/himself65/finance-skills) |
| `etf-premium` | Calculates ETF premium/discount versus NAV. | [Himself65](https://github.com/himself65/finance-skills) |
| `finance-sentiment` | Aggregates social sentiment data for specific equities. | [Himself65](https://github.com/himself65/finance-skills) |
| `funda-data` | Fetches raw financial statements and SEC filings. | [Himself65](https://github.com/himself65/finance-skills) |
| `hormuz-strait` | Tracks shipping chokepoints relevant to energy markets. | [Himself65](https://github.com/himself65/finance-skills) |
| `options-payoff` | Generates options payoff curves for multi-leg trades. | [Himself65](https://github.com/himself65/finance-skills) |
| `saas-valuation-compression` | Analyzes valuation changes between startup funding rounds. | [Himself65](https://github.com/himself65/finance-skills) |
| `startup-analysis` | Evaluates startups from an investment or operational perspective. | [Himself65](https://github.com/himself65/finance-skills) |
| `stock-correlation` | Maps sector peers and correlated trading pairs. | [Himself65](https://github.com/himself65/finance-skills) |
| `stock-liquidity` | Analyzes bid-ask spreads and estimated market impact. | [Himself65](https://github.com/himself65/finance-skills) |
| `yfinance-data` | Utility for fetching raw stock prices and historical data. | [Himself65](https://github.com/himself65/finance-skills) |

### 5. Swing Trading & Market Review
*Technical screening, breadth tracking, and risk management tools used to structure personal trading workflows.*

| Skill Name | Description | Source |
| :--- | :--- | :--- |
| `canslim-screener` | Screens stocks based on CANSLIM methodology. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `vcp-screener` | Screens for Volatility Contraction Patterns. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `sepa-strategy` | Analyzes breakouts using SEPA methodology. | [Himself65](https://github.com/himself65/finance-skills) |
| `portfolio-manager` | Reviews portfolio allocation and diversification. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `us-stock-analysis` | Compiles basic fundamental and technical reports on a ticker. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `position-sizer` | Helps calculate share counts based on ATR and risk tolerance. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `breakout-trade-planner` | Drafts trade plans with stop-loss and target levels. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `trade-performance-coach` | Framework for reviewing closed trades and process adherence. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `trader-memory-core` | A text-based journal for tracking investment theses. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `backtest-expert` | Methodologies for manual, systematic backtesting. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `breadth-chart-analyst` | Analyzes S&P 500 breadth charts for market context. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `market-breadth-analyzer` | Quantifies market participation into a basic score. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `uptrend-analyzer` | Assesses if current environments support equity exposure. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `ftd-detector` | Tracks Follow-Through Days for market direction. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `market-top-detector` | Tracks distribution days to evaluate market top risk. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `us-market-bubble-detector` | Evaluates structural market risks using basic frameworks. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `macro-regime-detector` | Looks at cross-asset ratios to track macro shifts. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `downtrend-duration-analyzer`| Calculates historical correction lengths by sector. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `ibd-distribution-day-monitor`| Tracks distribution days for index exposure adjustments. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `exposure-coach` | Summarizes market state to suggest cash vs. equity positioning. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `stanley-druckenmiller-investment`| Synthesizes various market signals into a single view. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `dividend-growth-pullback-screener`| Screens for dividend growers in technical pullbacks. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `value-dividend-screener` | Screens for fundamental value metrics in dividend stocks. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `earnings-calendar` | Retrieves basic earnings announcements schedules. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `economic-calendar-fetcher` | Fetches macroeconomic data release schedules. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `earnings-trade-analyzer` | Evaluates post-earnings gap behavior. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `pead-screener` | Screens for Post-Earnings Announcement Drift. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `finviz-screener` | Helps translate natural language into FinViz screening URLs. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `institutional-flow-tracker` | Basic tracker for 13F institutional filings. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `market-environment-analysis`| Provides a general global market overview. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `market-news-analyst` | Aggregates and categorizes recent financial news. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `options-strategy-advisor` | Basic Black-Scholes pricing references for options. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `pair-trade-screener` | Identifies cointegrated stock pairs for statistical arbitrage. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `parabolic-short-trade-planner`| Screens for technically overextended charts. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `scenario-analyzer` | Breaks down potential impacts of macro news headlines. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `sector-analyst` | Identifies basic sector rotation trends. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `technical-analyst` | Processes chart data for basic support/resistance levels. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `theme-detector` | Tracks current market narratives across sectors. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `tradingview-reader` | Read-only connection to local TradingView watchlists. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `trading-skills-navigator` | Directory assistant for finding the right skill in this repo. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |

### 6. Strategy & Testing Frameworks (Optional)
*Maintained for periodic backtesting and workflow automation, though generally kept inactive during daily use to save context space.*

| Skill Name | Description | Source |
| :--- | :--- | :--- |
| `edge-candidate-agent` | Auto-generates research tickets for new strategies. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `edge-concept-synthesizer` | Translates ideas into structured playbooks. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `edge-hint-extractor` | Extracts anomalies from daily market data. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `edge-pipeline-orchestrator`| Coordinates background backtesting pipelines. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `edge-signal-aggregator` | Ranks signals generated from other scripts. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `edge-strategy-designer` | Converts concepts into raw strategy code. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `edge-strategy-reviewer` | Reviews strategy code for logical errors. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `skill-designer` | Scaffolds directories for new custom skills. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `skill-idea-miner` | Parses chat logs to suggest new automations. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `skill-integration-tester` | Runs basic QA testing on newly written skills. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `dual-axis-skill-reviewer` | Grades custom skills for structural integrity. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `strategy-pivot-designer` | Restructures strategy code during backtest failures. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `trade-hypothesis-ideator` | Auto-generates hypothesis formats for new algorithms. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |
| `signal-postmortem` | Logs AI trade outcomes for post-review. | [TraderMonty](https://github.com/tradermonty/claude-trading-skills) |

### 7. Document & Asset Utilities
*Functional tools for outputting work directly into standard file formats.*

| Skill Name | Description | Source |
| :--- | :--- | :--- |
| `pdf` | Reads, edits, and processes PDF documents. | [Anthropic](https://github.com/anthropics/skills) |
| `docx` | Generates and edits Microsoft Word documents. | [Anthropic](https://github.com/anthropics/skills) |
| `xlsx` | Generates Excel spreadsheets and formats CSV data. | [Anthropic](https://github.com/anthropics/skills) |
| `pptx` | Generates Microsoft PowerPoint slide decks. | [Anthropic](https://github.com/anthropics/skills) |
| `sharp` | Resizes, crops, and processes image files via CLI. | [Clasen](https://github.com/clasen/Skills) |
| `token-budget-advisor` | Monitors API token usage to manage costs. | [ECC](https://github.com/affaan-m/ECC) |
| `the-council` | Framework for structured decision-making across personas. | Custom |

---

## Credits & Tributes
This repository is a heavily curated and opinionated assembly of open-source work. Full tribute, credit, and massive appreciation go to the original creators who engineered these skills:

*   **[TraderMonty (claude-trading-skills)](https://github.com/tradermonty/claude-trading-skills)** - For the unparalleled swing trading, risk management, and market breadth detection skills.
*   **[Alireza Rezvani (claude-skills)](https://github.com/alirezarezvani/claude-skills)** - For the exceptional data science, SQL, marketing psychology, and product management skills.
*   **[Himself65 (finance-skills)](https://github.com/himself65/finance-skills)** - For the deep fundamental financial modeling, DCF, and ETF analysis tools.
*   **[Anthropic (skills)](https://github.com/anthropics/skills)** - For the core PDF, DOCX, PPTX, and XLSX document generation capabilities.
*   **[Pedro Clasen (Skills)](https://github.com/clasen/Skills)** - For the programmatic image and asset manipulation tools (`sharp`).
*   **[ECC (token-budget-advisor)](https://github.com/affaan-m/ECC)** - For the token optimization and cost-saving advisory logic.

Thank you to the open-source AI community.

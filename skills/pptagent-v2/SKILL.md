---
name: pptagent-v2
description: End-to-End AI Presentation System with Research & Visuals.
---

# PPTAgent v2 Skill

## Overview
PPTAgent v2 is an advanced, end-to-end AI presentation system that features a deep research pipeline, automatic text-to-image generation for visuals, 20+ specialized tools, and an offline mode.

## Features
- **Deep Research Pipeline**: Automatically researches topics across multiple sources before generating slides.
- **Text-to-Image Generation**: Automatically generates diagrams, charts, and illustrative images directly on slides.
- **20+ Specialized Tools**: Includes web search, data extraction, chart rendering, layout selection, etc.
- **Offline Mode**: Can run fully locally without sending data to external APIs.

## When to Use
Use PPTAgent v2 when:
- The topic needs substantive research (market analysis, scientific briefings, policy papers, competitive landscapes).
- You need auto-generated charts and diagrams embedded directly in slides.
- Data privacy requires offline processing.

Do not use this skill for quick one-prompt decks, as the setup complexity is high.

## Setup Requirements
This skill uses `pptagent` CLI tool.
Installation:
- Recommended: `uvx pptagent generate "Your topic" -o output.pptx`
- Alternative: `pip install pptagent`

First-run setup requires configuring the LLM API key and a template PPTX before generation is possible (run `pptagent onboard`). 

## Usage
Commands:
- `uvx pptagent generate "Your presentation topic" -o output.pptx`
- To specify slide count and language: `uvx pptagent generate "AI in healthcare 2026" -o deck.pptx --slides 20 --lang en`
- Offline mode: `uvx pptagent generate "Your topic" -o output.pptx --offline`

Examples:
- "Global EV market analysis 2025 with competitive landscape"
- "Quantum computing: state of research and commercial applications"

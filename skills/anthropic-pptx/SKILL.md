---
name: anthropic-pptx
description: Official Claude Code PowerPoint Generator. General-purpose PPTX generation with built-in quality assurance.
---

# Anthropic PPTX Skill

## Overview
This skill generates general-purpose PPTX files with topic-specific color palettes and a built-in design QA pipeline. It can create new presentations, read existing decks, and make edits.

## Features
- **Topic-Specific Color Palettes**: Automatically selects a color scheme appropriate to your topic.
- **Built-in Design QA Pipeline**: Post-generation quality checks verify contrast ratios, font sizing, and layout consistency.
- **Create / Edit / Read Workflows**: Open an existing PPTX, read its content, and make targeted edits.

## When to Use
Use this skill for generating quick, clean decks without needing deep research. Best for general-purpose PPTX generation with built-in quality assurance. Do not use for brand-matched presentations or research-heavy decks needing auto-generated visuals.

## Setup Requirements
The underlying dependencies must be installed on the system:
1. `pip install "markitdown[pptx]" Pillow`
2. `npm install -g pptxgenjs`
3. Optional for PDF workflows: LibreOffice (soffice) + Poppler (pdftoppm)

## Usage
Examples of requests you can fulfill with this skill:
- "Create a 10-slide product roadmap for Q3"
- "Edit slide 3 of my deck to add a chart placeholder"
- "Read my existing deck.pptx and summarize the key points"
- "Make a pitch deck for a fintech startup raising Series A"

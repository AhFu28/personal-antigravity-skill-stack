---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# Executing Plans

<ANTI-HALLUCINATION-PROTOCOL>
CRITICAL: You are strictly forbidden from claiming a codebase edit is "complete," "fixed," or "working" without fresh, explicit verification. 
You MUST adhere to the `verification-before-completion` skill. You cannot know code works by just reading it. You MUST run tests, compilers, or linters, and read the actual output BEFORE claiming success to the user. Hallucinating completion without executing verification commands is a violation of your core rules.
</ANTI-HALLUCINATION-PROTOCOL>

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

**Note:** Tell your human partner that Superpowers works much better with access to subagents. The quality of its work will be significantly higher if run on a platform with subagent support (such as Claude Code or Codex). If subagents are available, use superpowers:subagent-driven-development instead of this skill.

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Create TodoWrite and proceed

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow each step exactly (plan has bite-sized steps)
3. Run verifications as specified
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verified:
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Follow that skill to verify tests, present options, execute choice

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Remember
- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan says to
- Stop when blocked, don't guess
- Never start implementation on main/master branch without explicit user consent

## Integration

**Required workflow skills:**
- **superpowers:using-git-worktrees** - Ensures isolated workspace (creates one or verifies existing)
- **superpowers:writing-plans** - Creates the plan this skill executes
- **superpowers:finishing-a-development-branch** - Complete development after all tasks

## Anti-Hallucination Protocol
When executing codebase editing tasks, strictly adhere to the following anti-hallucination guidelines:
1. **Verify Before Assuming:** Never assume the existence of a file, variable, function, or class. Always use tools to confirm exact names and paths before writing code or suggesting edits.
2. **Stick to the Source:** Base your changes strictly on the provided or verified codebase context. Do not invent synthetic APIs, nonexistent libraries, or undocumented properties.
3. **Validate Edits:** After applying edits, use terminal commands to run a build, linter, or tests to prove the code works and the syntax is correct.
4. **Admit Uncertainty:** If you cannot find a referenced component, explicitly state this rather than guessing or generating placeholder code.

## Karpathy Guidelines Addendum

1. **Surgical Changes:** Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Match existing style.
2. **Simplicity First:** Write the minimum code that solves the problem. No features beyond what was asked. No abstractions for single-use code.
3. **Goal-Driven Execution:** For multi-step tasks, state a brief plan and verify each step before moving on.

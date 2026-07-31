# Agent Workflow Toolkit

Submission for **Week 1, Thursday — Authoring AGENTS.md and Prompt Refactoring**.

Constrain the agent with an AGENTS.md file, build a small utility under those rules, and record how a vague prompt and a structured prompt produced different results.

This production-style Python CLI reports the Git/Python/Node toolchain and validates, normalizes, and converts JSON records without hiding malformed input.

## Run

```bash
python -m workflow_tool diagnostics
python -m workflow_tool clean input.json output.json
python -m unittest discover -s tests -v
```

The repository also records agent rules, prompt comparison, Git workflow, TDD evidence, root-cause review, architecture, deployment, and a short demonstration.

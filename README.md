# Agent Workflow Toolkit

Submission for **Week 2, Monday — Guided Git Workflows and Data Transformer**.

Drive Git through the agent to initialise a repository, work on a feature branch, and merge it back while building a data conversion tool with a clean, reviewed commit history.

This production-style Python CLI reports the Git/Python/Node toolchain and validates, normalizes, and converts JSON records without hiding malformed input.

## Run

```bash
python -m workflow_tool diagnostics
python -m workflow_tool clean input.json output.json
python -m unittest discover -s tests -v
```

The repository also records agent rules, prompt comparison, Git workflow, TDD evidence, root-cause review, architecture, deployment, and a short demonstration.

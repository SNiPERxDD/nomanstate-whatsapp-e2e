# Agent Workflow Toolkit

Submission for **Week 3, Thursday — Debugging and Agent-Assisted Code Review**.

Diagnose and repair defects in an existing codebase without rewriting it, then run an agent-assisted review. Document each defect, its root cause, the fix, and how you verified it.

This production-style Python CLI reports the Git/Python/Node toolchain and validates, normalizes, and converts JSON records without hiding malformed input.

## Run

```bash
python -m workflow_tool diagnostics
python -m workflow_tool clean input.json output.json
python -m unittest discover -s tests -v
```

The repository also records agent rules, prompt comparison, Git workflow, TDD evidence, root-cause review, architecture, deployment, and a short demonstration.

# Agent Workflow Toolkit

Submission for **Week 4 — Capstone Project and Production Delivery**.

Plan, build, test, document, and deploy one complete product. Include setup documentation, an architecture note, meaningful tests, and a short demonstration of the working software.

This production-style Python CLI reports the Git/Python/Node toolchain and validates, normalizes, and converts JSON records without hiding malformed input.

## Run

```bash
python -m workflow_tool diagnostics
python -m workflow_tool clean input.json output.json
python -m unittest discover -s tests -v
```

The repository also records agent rules, prompt comparison, Git workflow, TDD evidence, root-cause review, architecture, deployment, and a short demonstration.

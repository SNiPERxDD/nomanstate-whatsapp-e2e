# Agent Workflow Toolkit

Submission for **Week 3, Monday — Test-Driven Development with Coding Agents**.

Write the tests first, confirm they fail, then direct the agent to implement until they pass. Submit the implementation, the test suite, and evidence of the failing-to-passing transition.

This production-style Python CLI reports the Git/Python/Node toolchain and validates, normalizes, and converts JSON records without hiding malformed input.

## Run

```bash
python -m workflow_tool diagnostics
python -m workflow_tool clean input.json output.json
python -m unittest discover -s tests -v
```

The repository also records agent rules, prompt comparison, Git workflow, TDD evidence, root-cause review, architecture, deployment, and a short demonstration.

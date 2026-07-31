# TDD evidence

1. Added the normalization, malformed-row, and invalid-JSON tests first.
2. First run failed because `workflow_tool.cleaner` did not exist.
3. Added the smallest implementation and reran: all tests passed.
4. Extracted `clean_file`; the same tests stayed green and protect the refactor.

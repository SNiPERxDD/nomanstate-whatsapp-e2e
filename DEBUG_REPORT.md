# Debug and review report

- Defect: malformed JSON leaked a decoder traceback. Root cause: parsing errors crossed the CLI boundary. Fix: translate read/decode failures to a stable `ValueError`; regression test verifies it.
- Defect: bad rows could be silently discarded. Root cause: no error collection contract. Fix: return indexed errors and a non-zero CLI code.
- Review: subprocess arguments are fixed, shell execution is absent, files use explicit UTF-8, and modules have focused responsibilities.

# Prompt comparison

Vague: “Make a data tool.” This omitted formats, failure behavior, and acceptance checks.

Structured: “Using stdlib Python, accept a JSON array of name/email objects, normalize whitespace/case, report every malformed row, return non-zero on partial failure, and pass the named unittest cases.”

The structured prompt produced testable boundaries and prevented silent data loss.

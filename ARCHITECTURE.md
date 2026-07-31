# Architecture

`cli` owns argument parsing and exit codes; `diagnostics` owns bounded tool discovery; `cleaner` owns validation and deterministic conversion. Dependencies point inward to small functions, so tests exercise behavior without shelling out or network access.

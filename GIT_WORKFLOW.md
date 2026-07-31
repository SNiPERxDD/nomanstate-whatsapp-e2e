# Reviewed Git workflow

Work starts on a `feature/data-cleaner` branch. Before merge: inspect `git diff --check`, run the full unittest command, review error paths, then merge only a green commit into `main`. Commits separate diagnostics, cleaning, tests, and documentation so each change is reviewable.

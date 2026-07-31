# Delivery and demonstration

CI runs `python -m unittest discover -s tests -v` on every push. A release is the tagged repository: clone it and use the README commands on Python 3.9+. Demo: run `diagnostics`, clean a JSON fixture, observe normalized output plus indexed validation errors, then run the green suite. Rollback is the previous tag.

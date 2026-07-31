import tempfile
import unittest
from pathlib import Path

from workflow_tool.cleaner import clean_file, clean_records
from workflow_tool.diagnostics import system_report


class WorkflowToolTest(unittest.TestCase):
    def test_diagnostics_reports_required_toolchain(self):
        self.assertEqual(set(system_report()), {"platform", "python", "git", "node"})

    def test_clean_records_normalizes_and_reports_bad_rows(self):
        cleaned, errors = clean_records([{ "name": "  Ada  Lovelace ", "email": " ADA@EXAMPLE.COM "}, None])
        self.assertEqual(cleaned, [{"name": "Ada Lovelace", "email": "ada@example.com"}])
        self.assertEqual(errors, ["record 2: expected object"])

    def test_clean_file_rejects_invalid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.json"
            source.write_text("not json", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "could not read input"):
                clean_file(source, Path(directory) / "output.json")


if __name__ == "__main__":
    unittest.main()

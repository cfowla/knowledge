import json
import tempfile
import unittest
from pathlib import Path

import pmc_acquire
import server


class BasicTests(unittest.TestCase):
    def test_clean_pmid(self):
        self.assertEqual(pmc_acquire.clean_pmid("35124914"), "35124914")
        with self.assertRaises(ValueError):
            pmc_acquire.clean_pmid("PMID 35124914")

    def test_safe_run_dir_rejects_traversal(self):
        with self.assertRaises(ValueError):
            server._safe_run_dir("../etc")

    def test_api_manifest_adds_download_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "PMID_35124914_deadbeef"
            run_dir.mkdir()
            path = run_dir / "manifest.json"
            path.write_text(json.dumps({
                "artifacts": [{"kind": "xml", "path": str(run_dir / "article.xml")}]
            }), encoding="utf-8")
            result = server._api_manifest(path)
            self.assertEqual(
                result["artifacts"][0]["download_url"],
                "/api/runs/PMID_35124914_deadbeef/files/article.xml",
            )


if __name__ == "__main__":
    unittest.main()

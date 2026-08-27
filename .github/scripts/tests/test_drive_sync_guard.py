from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "drive_sync_guard.py"
spec = importlib.util.spec_from_file_location("drive_sync_guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = guard
assert spec.loader is not None
spec.loader.exec_module(guard)

SYNC_AUTHOR = "google-drive-sync[bot]"
SYNC_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"
HUMAN_AUTHOR = "Repository Author"
HUMAN_EMAIL = "author@example.com"


class DriveSyncGuardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.destination = self.root / "drive-sync"
        self.stage = self.root / "stage"
        self.report = self.root / "health-reports" / "drive-sync-conflicts" / "test.md"
        self.destination.mkdir()
        self.stage.mkdir()
        self.git("init", "-q")
        self.git("config", "user.name", HUMAN_AUTHOR)
        self.git("config", "user.email", HUMAN_EMAIL)
        (self.root / "README.md").write_text("test\n")
        self.commit("initial", HUMAN_AUTHOR, HUMAN_EMAIL)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.root), *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def commit(self, message: str, author: str, email: str) -> None:
        self.git("add", "-A")
        self.git(
            "-c",
            f"user.name={author}",
            "-c",
            f"user.email={email}",
            "commit",
            "-q",
            "--author",
            f"{author} <{email}>",
            "-m",
            message,
        )

    def run_guard(self) -> int:
        return guard.run_import(
            repo_root=self.root,
            stage_root=self.stage,
            destination_root=self.destination,
            conflict_report=self.report,
            sync_author=SYNC_AUTHOR,
        )

    def test_new_drive_file_is_added(self) -> None:
        (self.stage / "new.txt").write_text("from drive\n")
        self.assertEqual(self.run_guard(), 0)
        self.assertEqual((self.destination / "new.txt").read_text(), "from drive\n")

    def test_drive_owned_file_is_updated(self) -> None:
        path = self.destination / "owned.txt"
        path.write_text("old\n")
        self.commit("drive-owned", SYNC_AUTHOR, SYNC_EMAIL)
        (self.stage / "owned.txt").write_text("new\n")
        self.assertEqual(self.run_guard(), 0)
        self.assertEqual(path.read_text(), "new\n")

    def test_destination_only_github_file_survives(self) -> None:
        path = self.destination / "github-only.txt"
        path.write_text("keep me\n")
        self.commit("github-only", HUMAN_AUTHOR, HUMAN_EMAIL)
        self.assertEqual(self.run_guard(), 0)
        self.assertEqual(path.read_text(), "keep me\n")

    def test_github_modified_same_path_blocks_entire_import(self) -> None:
        conflict = self.destination / "shared.txt"
        conflict.write_text("drive baseline\n")
        self.commit("drive baseline", SYNC_AUTHOR, SYNC_EMAIL)
        conflict.write_text("github edit\n")
        self.commit("github edit", HUMAN_AUTHOR, HUMAN_EMAIL)
        (self.stage / "shared.txt").write_text("new drive edit\n")
        (self.stage / "otherwise-safe-new.txt").write_text("new\n")

        self.assertEqual(self.run_guard(), 2)
        self.assertEqual(conflict.read_text(), "github edit\n")
        self.assertFalse((self.destination / "otherwise-safe-new.txt").exists())
        report = self.report.read_text()
        self.assertIn("drive-sync/shared.txt", report)
        self.assertIn(HUMAN_AUTHOR, report)

    def test_excluded_media_remains_excluded(self) -> None:
        (self.stage / "clip.mp4").write_bytes(b"video")
        (self.stage / "disk.iso").write_bytes(b"image")
        (self.stage / "allowed.txt").write_text("ok\n")
        self.assertEqual(self.run_guard(), 0)
        self.assertFalse((self.destination / "clip.mp4").exists())
        self.assertFalse((self.destination / "disk.iso").exists())
        self.assertTrue((self.destination / "allowed.txt").exists())

    def test_no_destination_cleanup_occurs_during_owned_update(self) -> None:
        owned = self.destination / "folder" / "owned.txt"
        extra = self.destination / "folder" / "github-extra.txt"
        owned.parent.mkdir(parents=True)
        owned.write_text("old\n")
        self.commit("drive-owned", SYNC_AUTHOR, SYNC_EMAIL)
        extra.write_text("extra\n")
        self.commit("github extra", HUMAN_AUTHOR, HUMAN_EMAIL)
        staged_owned = self.stage / "folder" / "owned.txt"
        staged_owned.parent.mkdir(parents=True)
        staged_owned.write_text("new\n")

        self.assertEqual(self.run_guard(), 0)
        self.assertEqual(owned.read_text(), "new\n")
        self.assertEqual(extra.read_text(), "extra\n")

    def test_identical_github_owned_path_needs_no_overwrite(self) -> None:
        path = self.destination / "same.txt"
        path.write_text("same\n")
        self.commit("github file", HUMAN_AUTHOR, HUMAN_EMAIL)
        (self.stage / "same.txt").write_text("same\n")
        self.assertEqual(self.run_guard(), 0)
        self.assertFalse(self.report.exists())


class WorkflowConfigurationTests(unittest.TestCase):
    def test_workflow_stages_before_guarded_apply(self) -> None:
        workflow = Path(".github/workflows/sync-google-drive.yml").read_text()
        self.assertNotIn('rclone sync "$DRIVE_SOURCE"', workflow)
        self.assertNotIn('rclone copy "$DRIVE_SOURCE" "$REPO_DESTINATION"', workflow)
        self.assertIn('rclone copy "$DRIVE_SOURCE" "$DRIVE_STAGE"', workflow)
        self.assertIn("drive_sync_guard.py", workflow)
        self.assertIn("health-reports/drive-sync-conflicts", workflow)
        for suffix in ("mp4", "mov", "avi", "mkv", "iso"):
            self.assertIn(f'--exclude "**/*.{suffix}"', workflow)
        self.assertNotIn("--delete-during", workflow)
        self.assertNotIn("--delete-excluded", workflow)


if __name__ == "__main__":
    unittest.main()

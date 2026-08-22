from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from scholar_acquire.integrity import write_build_manifest

if __name__ == "__main__":
    path = write_build_manifest(ROOT / "src" / "scholar_acquire", version="0.4.0")
    print(path)

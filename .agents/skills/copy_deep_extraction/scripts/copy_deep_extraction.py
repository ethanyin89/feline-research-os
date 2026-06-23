import os
import shutil
import re
import logging
from pathlib import Path

def slugify(name: str) -> str:
    """Create a URL‑friendly slug from a filename.
    Removes leading/trailing spaces, lower‑cases, keeps alphanumerics and hyphens.
    """
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = name.strip("-")
    return name

def copy_deep_extractions(source_dir: str, target_dir: str, log_path: str = "copy_deep_extraction.log"):
    logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    source = Path(os.path.expanduser(source_dir)).resolve()
    target = Path(target_dir).resolve()
    if not source.is_dir():
        logging.error(f"Source directory does not exist: {source}")
        return
    target.mkdir(parents=True, exist_ok=True)
    pattern = re.compile(r"\.deep extract\.md$", re.IGNORECASE)
    for entry in source.iterdir():
        if entry.is_file() and pattern.search(entry.name):
            slug = slugify(entry.stem)
            dest_name = f"ext-src-{slug}.md"
            dest_path = target / dest_name
            if dest_path.exists():
                logging.info(f"Skipped existing file: {dest_path}")
                continue
            try:
                shutil.copy2(entry, dest_path)
                logging.info(f"Copied {entry} -> {dest_path}")
            except Exception as e:
                logging.error(f"Failed to copy {entry} -> {dest_path}: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Copy deep‑extraction markdown files from a source folder to the project raw/deep‑extractions directory.")
    parser.add_argument("--source", required=True, help="Path to the folder containing *.deep extract.md files (e.g., ~/Desktop)")
    parser.add_argument("--target", default="raw/deep-extractions", help="Relative or absolute path to the destination folder inside the project.")
    args = parser.parse_args()
    copy_deep_extractions(args.source, args.target)

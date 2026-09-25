"""Package tracked course materials for GitHub Pages, preserving relative URLs."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def is_site_file(name):
    if name == "index.html":
        return True
    parts = Path(name).parts
    return (
        parts[0] == "outputs"
        and not any(
            part in {"work", "verify"} or part.startswith("style-previews")
            for part in parts
        )
    )


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"src", "href", "poster"} and value:
                url = urlsplit(value)
                if not url.scheme and not url.netloc and url.path:
                    self.links.append(unquote(url.path))


def build(destination):
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT
    ).decode("utf-8").split("\0")
    files = {name for name in tracked if name and is_site_file(name)}
    if "index.html" not in files:
        raise RuntimeError("The root index.html must be tracked by Git.")

    # Check every HTML link before publishing, including images and downloads.
    references = 0
    for name in sorted(files):
        source = ROOT / name
        if source.is_symlink() or not source.is_file():
            raise RuntimeError(f"Missing file or unsupported symlink: {name}")
        if source.suffix.lower() != ".html":
            continue
        parser = LocalLinks()
        parser.feed(source.read_text(encoding="utf-8-sig"))
        for link in parser.links:
            target = (source.parent / link).resolve()
            if link.startswith("/") or not target.is_relative_to(ROOT):
                raise RuntimeError(f"Link is outside this project site: {name}: {link}")
            if target.relative_to(ROOT).as_posix() not in files:
                raise RuntimeError(f"Unpublished link target: {name}: {link}")
            references += 1

    size = sum((ROOT / name).stat().st_size for name in files)
    if size >= 1_000_000_000:
        raise RuntimeError("The published site must be smaller than 1 GB.")
    # Require a fresh output folder so old files cannot leak into a new release.
    destination.mkdir(parents=True, exist_ok=False)
    for name in sorted(files):
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / name, target)
    (destination / ".nojekyll").touch()
    print(
        f"Packaged {len(files)} files ({size / 1_000_000:.1f} MB); "
        f"validated {references} local links."
    )


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--output", type=Path, default=ROOT / "_site")
    build(cli.parse_args().output.resolve())

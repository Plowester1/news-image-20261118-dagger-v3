"""Entrypoint for the news-image-20261118 dagger entry.

This script has a single job: take the finished artwork that lives
next to it (entry.png) and place a faithful copy into the output
directory the make.fun runner expects. Nothing is generated here,
nothing is fetched from the network, and nothing is randomised --
running it twice in a row produces exactly the same bytes twice.

The destination folder comes from the MAKEFUN_OUTPUT_DIR environment
variable, falling back to /output when the variable is not set.
After the copy lands, both files are hashed with SHA-256 and the
digests are compared. A mismatch is treated as a hard failure so a
corrupt or truncated copy can never slip through silently.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def digest_of(target_path):
    """Return the SHA-256 hex digest for the file at target_path.

    The file is read in fixed-size chunks so memory use stays flat
    regardless of how large the image happens to be.
    """
    hasher = hashlib.sha256()
    with open(target_path, "rb") as handle:
        while True:
            block = handle.read(65536)
            if not block:
                break
            hasher.update(block)
    return hasher.hexdigest()


def run():
    """Copy entry.png into the output directory and verify the copy.

    Returns 0 on success and a non-zero code on any problem, with a
    plain-language message written to stderr so the failure is easy
    to spot in runner logs.
    """
    # Anchor everything to this file's own folder, never to the
    # caller's working directory -- the runner may launch us from
    # anywhere.
    home_folder = Path(__file__).resolve().parent
    artwork_source = home_folder / "entry.png"

    if not artwork_source.is_file():
        print(f"error: expected artwork at {artwork_source} but it is missing", file=sys.stderr)
        return 1

    # Honour the runner-provided output location, defaulting to
    # /output for local runs where the variable is absent.
    output_folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_folder.mkdir(parents=True, exist_ok=True)
    artwork_target = output_folder / "entry.png"

    shutil.copyfile(artwork_source, artwork_target)

    # Integrity gate: the copy must be byte-for-byte identical to
    # the original. Hash both sides and refuse to continue if the
    # digests disagree.
    source_digest = digest_of(artwork_source)
    target_digest = digest_of(artwork_target)

    if source_digest != target_digest:
        print(
            "error: SHA-256 mismatch after copy "
            f"(source={source_digest}, output={target_digest})",
            file=sys.stderr,
        )
        return 1

    print(f"entry.png copied to {artwork_target} (sha256={target_digest})")
    return 0


if __name__ == "__main__":
    sys.exit(run())

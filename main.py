#!/usr/bin/env python3
"""news-image-20261124 entry runner.

Verifies the bundled front-page image and writes an identical copy to
the output directory.

Checks performed before anything is written:
  * ``entry.png`` sits next to this script and is a real PNG file
    (8-byte signature, then an IHDR chunk);
  * the IHDR records a width and height of exactly 1024 x 1024;
  * the file is smaller than 1 MiB;
  * its SHA-256 digest matches the digest recorded below, so a
    corrupted or swapped image fails loudly instead of being copied.

Usage:
    python3 main.py [output-dir]

The output directory defaults to ``/output``. The program uses only
the Python standard library and performs no network access.
"""

import hashlib
import os
import shutil
import struct
import sys

EXPECTED_SHA256 = "f942fb8b12d621dec7118d015872fb1749487f1ded3b2eb6225442f0f0b06a76"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1024 * 1024

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_dimensions(path):
    """Return (width, height) from a PNG file's IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(24)
    if header[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file: bad signature")
    if header[12:16] != b"IHDR":
        raise ValueError("not a PNG file: first chunk is not IHDR")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = argv[1] if len(argv) > 1 else "/output"

    if not os.path.isfile(source):
        raise SystemExit("entry.png not found next to main.py")

    size = os.path.getsize(source)
    if size >= MAX_BYTES:
        raise SystemExit(
            "entry.png is %d bytes, over the 1 MiB limit" % size
        )

    width, height = read_png_dimensions(source)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(
            "entry.png is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )

    digest = sha256_of(source)
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            "entry.png SHA-256 mismatch: got %s" % digest
        )

    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, destination)

    # Confirm the copy itself is intact before reporting success.
    if sha256_of(destination) != EXPECTED_SHA256:
        raise SystemExit("copy failed verification: %s" % destination)

    print("verified entry.png: %dx%d PNG, %d bytes" % (width, height, size))
    print("sha256: %s" % digest)
    print("wrote %s" % destination)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

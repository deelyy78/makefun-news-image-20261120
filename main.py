# news-image-20261120: write the entry image to the grader's output dir.
# The image ships in the repository as entry.png; this program copies it
# to /output/entry.png. Standard library only, no network, no clocks and
# no randomness, so both grader runs produce byte-identical output.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

# The gate only accepts a whole PNG of at most 1 MiB and 1024x1024, so
# fail loudly here rather than hand the grader a broken file.
with open(DST, "rb") as fh:
    head = fh.read(24)
assert head[:8] == b"\x89PNG\r\n\x1a\n", "output is not a PNG"
# The IHDR chunk follows the signature: width and height are the two
# big-endian uint32 at bytes 16..24, and both must be within the cap.
width = int.from_bytes(head[16:20], "big")
height = int.from_bytes(head[20:24], "big")
assert 0 < width <= 1024 and 0 < height <= 1024, "image over 1024x1024"
assert os.path.getsize(DST) == os.path.getsize(SRC), "copy size mismatch"
assert os.path.getsize(DST) <= 1048576, "image over the 1 MiB gate limit"

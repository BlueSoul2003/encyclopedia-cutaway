"""Check packaged examples and relative Markdown links; no external dependencies."""
from pathlib import Path
import hashlib
import json
import re
import struct

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "examples/manifest.json").read_text(encoding="utf-8"))
plates = manifest["examples"]
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

check(len(plates) == 10, "The initial release must contain ten selected plates.")
for field in ("id", "image", "language", "domain"):
    check(len({p[field] for p in plates}) == len(plates), f"Duplicate {field}.")
for plate in plates:
    path = ROOT / "examples" / plate["image"]
    check(Path(plate["image"]).name == plate["image"], f"Unsafe image path: {plate['id']}")
    check(path.is_file(), f"Missing image: {plate['id']}")
    check(plate["status"] == "reviewed" and bool(plate.get("review")), f"Unreviewed: {plate['id']}")
    check(bool(plate["prompt"]) and len(plate["labels"]) == 6 and bool(plate["sources"]),
          f"Incomplete prompt/captions/sources: {plate['id']}")
    if path.is_file():
        data = path.read_bytes()
        check(data[:8] == b"\x89PNG\r\n\x1a\n", f"Not PNG: {plate['id']}")
        if len(data) >= 24:
            size = list(struct.unpack(">II", data[16:24]))
            check(size == plate.get("dimensions"), f"Dimensions mismatch: {plate['id']}")
        check(hashlib.sha256(data).hexdigest() == plate.get("sha256"),
              f"Hash mismatch: {plate['id']}")
        check(len(data) < 100 * 1024 * 1024, f"Image exceeds GitHub file limit: {plate['id']}")

for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
        target = target.strip("<>").split("#", 1)[0]
        if not target or re.match(r"[a-zA-Z]+:", target):
            continue
        check((md.parent / target).is_file(), f"Broken link in {md.relative_to(ROOT)}: {target}")

check((ROOT / ".agents/skills/encyclopedia-cutaway/SKILL.md").is_file(), "Missing skill.")
check((ROOT / "LICENSE").is_file(), "Missing license.")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(plates)} reviewed plates, PNG hashes/dimensions, and local Markdown links.")

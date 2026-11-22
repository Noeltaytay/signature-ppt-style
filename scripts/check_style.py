#!/usr/bin/env python3
"""Check a deck or template against the signature PPT structure rules.

Usage:
    python check_style.py <project_or_svg_dir> [--palette <json>] [--strict-palette]

Structural checks always run:
  - XML parses; viewBox is 0 0 1280 720
  - no banned tags (mask, style, foreignObject, script, animate)
  - image hrefs resolve
  - chapter divider files contain no <image>
  - project page count = notes count = animation slide keys

Palette and font checks are advisory:
  - off-palette colors are reported only with --strict-palette
  - non-standard font stacks are warnings

Exit code 1 on structural errors; warnings do not fail.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_PALETTE = SKILL_DIR / "presets" / "bluegray-example.json"
SUPPORTING_COLORS = {
    "#10254A", "#1B3E6B", "#192F59", "#0E2240", "#1C4069", "#142C4D",
    "#10233F", "#0B1B35", "#163A60", "#2E6AA8", "#3F6E9F", "#4A7FB0",
    "#5B8FBF", "#7FA5C9", "#8FB0C7", "#C2A368", "#D8BE86", "#E7CB92",
    "#F7FAFE", "#F5F8FA", "#C9D7E0", "#B9CAD7", "#C3D2DC", "#5B7080",
    "#094183", "#50638A", "#7C8FA6", "#8EADD0", "#7F9DBC", "#8FA9C6",
    "#AEC3D9", "#E4EDF3", "#D6E2EA", "#315F80", "#23435B", "#193B63",
    "#173A63", "#A98243", "#1E3445", "#24466F", "#FFFFFF",
}
APPROVED_FONT_HINTS = ("Microsoft YaHei", "Georgia", "KaiTi", "STKaiti", "SimSun", "Arial")
BANNED = ("mask", "style", "foreignObject", "script", "animate", "set")


def load_palette(path: Path) -> set[str]:
    allowed = set(SUPPORTING_COLORS)
    if path.is_file():
        data = json.loads(path.read_text(encoding="utf-8"))
        for value in data.get("colors", {}).values():
            if isinstance(value, str) and value.startswith("#"):
                allowed.add(value.upper())
    return allowed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path")
    ap.add_argument("--palette", help="palette JSON for strict color audit")
    ap.add_argument("--strict-palette", action="store_true", help="warn on colors outside the chosen palette")
    args = ap.parse_args()

    root = Path(args.path).resolve()
    svg_dir = root / "svg_output" if (root / "svg_output").is_dir() else root
    svgs = sorted(svg_dir.glob("*.svg"))
    if not svgs:
        print(f"ERROR: no SVG files in {svg_dir}")
        return 1

    palette_path = Path(args.palette) if args.palette else DEFAULT_PALETTE
    allowed = load_palette(palette_path)

    errors: list[str] = []
    warnings: list[str] = []
    stems = [p.stem for p in svgs]

    for svg in svgs:
        try:
            tree = ET.parse(svg)
        except ET.ParseError as exc:
            errors.append(f"{svg.name}: XML parse error: {exc}")
            continue
        doc = tree.getroot()
        view = doc.get("viewBox", "")
        if view.replace(",", " ").split() != ["0", "0", "1280", "720"]:
            errors.append(f"{svg.name}: viewBox is {view!r}, expected 0 0 1280 720")

        for elem in doc.iter():
            tag = str(elem.tag).split("}")[-1]
            if tag in BANNED:
                errors.append(f"{svg.name}: banned tag <{tag}>")
            if tag == "image":
                href = elem.get("href") or elem.get("{http://www.w3.org/1999/xlink}href")
                if "chapter" in svg.stem:
                    errors.append(f"{svg.name}: chapter divider must not use <image>")
                if not href:
                    errors.append(f"{svg.name}: image without href")
                elif not href.startswith("data:"):
                    target = (svg_dir / href).resolve()
                    if not target.is_file():
                        errors.append(f"{svg.name}: image not found: {href}")

        text = svg.read_text(encoding="utf-8")
        if args.strict_palette:
            for match in re.finditer(r"#[0-9A-Fa-f]{6}", text):
                color = match.group(0).upper()
                if color not in allowed:
                    warnings.append(f"{svg.name}: off-palette color {color}")

        for match in re.finditer(r'font-family="([^"]+)"', text):
            family = match.group(1)
            if not any(hint in family for hint in APPROVED_FONT_HINTS):
                warnings.append(f"{svg.name}: non-standard font stack {family!r}")

    if (root / "svg_output").is_dir():
        notes = root / "notes"
        note_stems = {p.stem for p in notes.glob("*.md")} if notes.is_dir() else set()
        for stem in stems:
            if stem not in note_stems:
                errors.append(f"{stem}: missing notes/{stem}.md")
        total = notes / "total.md"
        if total.is_file():
            text = total.read_text(encoding="utf-8")
            for stem in stems:
                if not re.search(rf"^#\s+{re.escape(stem)}\s*$", text, re.M):
                    errors.append(f"notes/total.md missing heading '# {stem}'")
        else:
            warnings.append("notes/total.md not found")

        anim = root / "animations.json"
        if anim.is_file():
            try:
                keys = set(json.loads(anim.read_text(encoding="utf-8")).get("slides", {}))
                if keys != set(stems):
                    missing = sorted(set(stems) - keys)
                    extra = sorted(keys - set(stems))
                    errors.append(f"animations.json key mismatch; missing={missing}, extra={extra}")
            except json.JSONDecodeError as exc:
                errors.append(f"animations.json parse error: {exc}")
        else:
            warnings.append("animations.json not found")

    warnings = sorted(set(warnings))
    print(f"Checked: {svg_dir}")
    print(f"SVG files: {len(svgs)}")
    print(f"Errors: {len(errors)}")
    for msg in errors:
        print(f"  [ERROR] {msg}")
    print(f"Warnings: {len(warnings)}")
    for msg in warnings[:60]:
        print(f"  [WARN] {msg}")
    if len(warnings) > 60:
        print(f"  ... {len(warnings) - 60} more warnings")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

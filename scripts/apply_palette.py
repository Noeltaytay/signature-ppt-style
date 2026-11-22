#!/usr/bin/env python3
"""Recolor the structural templates with a content-driven palette.

Usage:
    python apply_palette.py --palette presets/academic-warm.json \
        --src templates --out ./my-deck/templates

The geometry and decoration are preserved; only color values are remapped.
The base templates use the approved blue-gray example palette, which acts as the
semantic source: primary, secondary, action, background, accent, muted, divider,
on-primary, and their supporting tints.

Exit code 1 on invalid input; low-contrast warnings do not fail.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")


def parse_hex(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def to_hex(rgb: tuple[int, int, int]) -> str:
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(v))) for v in rgb)


def mix(a: str, b: str, t: float) -> str:
    ar, ag, ab = parse_hex(a)
    br, bg, bb = parse_hex(b)
    return to_hex((ar + (br - ar) * t, ag + (bg - ag) * t, ab + (bb - ab) * t))


def luminance(value: str) -> float:
    r, g, b = (v / 255 for v in parse_hex(value))
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def build_mapping(colors: dict[str, str]) -> dict[str, str]:
    c = {k: v.upper() for k, v in colors.items()}
    return {
        "#192F59": c["primary"],
        "#50638A": c["secondary"],
        "#094183": c["action"],
        "#F7FAFE": c["background"],
        "#FFFFFF": c.get("surface", "#FFFFFF"),
        "#C2A368": c["accent"],
        "#D8BE86": c["accent_light"],
        "#5B7080": c["muted"],
        "#C3D2DC": c["divider"],
        "#F5F8FA": c["on_primary"],
        "#C9D7E0": c["on_primary_muted"],
        "#10254A": c["dark_field"],
        "#1B3E6B": c["dark_field_mid"],
        "#10233F": c["dark_panel"],
        "#0E2240": c["dark_field"],
        "#0B1B35": c["dark_panel"],
        "#163A60": mix(c["dark_field"], c["primary"], 0.45),
        "#173A63": c["dark_field_mid"],
        "#193B63": c["dark_field_mid"],
        "#1C4069": c["dark_field_mid"],
        "#142C4D": c["dark_panel"],
        "#2E6AA8": mix(c["action"], "#FFFFFF", 0.20),
        "#3F6E9F": mix(c["secondary"], "#FFFFFF", 0.15),
        "#4A7FB0": mix(c["action"], "#FFFFFF", 0.35),
        "#5B8FBF": mix(c["secondary"], "#FFFFFF", 0.30),
        "#7C8FA6": mix(c["muted"], "#FFFFFF", 0.35),
        "#7F9DBC": mix(c["muted"], "#FFFFFF", 0.45),
        "#8EADD0": mix(c["secondary"], "#FFFFFF", 0.55),
        "#8FA9C6": mix(c["secondary"], "#FFFFFF", 0.60),
        "#8FB0C7": mix(c["secondary"], "#FFFFFF", 0.55),
        "#AEC3D9": mix(c["on_primary_muted"], "#FFFFFF", 0.25),
        "#B9CAD7": c["on_primary_muted"],
        "#E7CB92": mix(c["accent_light"], "#FFFFFF", 0.25),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--palette", required=True)
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--force", action="store_true", help="allow writing into a non-empty out dir")
    args = ap.parse_args()

    palette_path = Path(args.palette)
    src = Path(args.src)
    out = Path(args.out)
    if not palette_path.is_file():
        print(f"ERROR: palette not found: {palette_path}")
        return 1
    if not src.is_dir():
        print(f"ERROR: source not found: {src}")
        return 1
    if src.resolve() == out.resolve():
        print("ERROR: --out must differ from --src")
        return 1
    if out.exists() and any(out.iterdir()) and not args.force:
        print(f"ERROR: out dir is not empty: {out} (use --force to overwrite)")
        return 1

    data = json.loads(palette_path.read_text(encoding="utf-8"))
    colors = data.get("colors", {})
    required = ["primary", "secondary", "action", "background", "accent", "muted", "divider", "on_primary"]
    missing = [k for k in required if k not in colors]
    if missing:
        print(f"ERROR: palette missing colors: {missing}")
        return 1

    mapping = build_mapping(colors)
    out.mkdir(parents=True, exist_ok=True)
    svg_files = sorted(src.glob("*.svg"))
    if not svg_files:
        print(f"ERROR: no SVG files in {src}")
        return 1

    unknown: set[str] = set()
    for svg in svg_files:
        text = svg.read_text(encoding="utf-8")
        def repl(m: re.Match[str]) -> str:
            key = m.group(0).upper()
            if key in mapping:
                return mapping[key]
            unknown.add(key)
            return m.group(0)
        new = HEX_RE.sub(repl, text)
        (out / svg.name).write_text(new, encoding="utf-8")

    # copy non-SVG supporting files (README, etc.)
    for item in src.iterdir():
        if item.is_file() and item.suffix.lower() != ".svg":
            shutil.copy2(item, out / item.name)

    print(f"Palette: {data.get('name', palette_path.stem)}")
    print(f"Recolored: {len(svg_files)} SVG file(s) -> {out}")
    if unknown:
        print(f"WARNING: {len(unknown)} off-palette color(s) left unchanged:")
        for color in sorted(unknown):
            print(f"  {color}")

    for fg, bg, label in [
        (colors["text"], colors["background"], "text/background"),
        (colors["on_primary"], colors["primary"], "on-primary/primary"),
    ]:
        ratio = contrast(fg, bg)
        flag = "OK" if ratio >= 4.5 else "LOW"
        print(f"Contrast {label}: {ratio:.2f}:1 [{flag}]")
        if ratio < 4.5:
            print(f"  WARNING: {label} is below 4.5:1; adjust tokens before export.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

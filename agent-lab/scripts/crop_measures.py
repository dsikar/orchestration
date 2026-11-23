#!/usr/bin/env python3
"""Keep the first N <measure> elements of each part in a MusicXML score."""

from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from pathlib import Path


def local(tag: str) -> str:
    return tag.split("}", 1)[-1]


def crop(src: Path, dest: Path, n_measures: int, title_suffix: str) -> None:
    tree = ET.parse(src)
    root = tree.getroot()

    work_title = None
    for el in root.iter():
        if local(el.tag) == "work-title" and el.text:
            work_title = el
            break
    if work_title is not None:
        work_title.text = f"{work_title.text}{title_suffix}"

    credits = [c for c in list(root) if local(c.tag) == "credit"]
    for credit in credits:
        page = credit.attrib.get("page", "1")
        if page != "1":
            root.remove(credit)

    for part in root:
        if local(part.tag) != "part":
            continue
        measures = [c for c in list(part) if local(c.tag) == "measure"]
        if len(measures) < n_measures:
            raise SystemExit(
                f"part {part.attrib.get('id')} has only {len(measures)} measures"
            )
        for extra in measures[n_measures:]:
            part.remove(extra)
        last = measures[n_measures - 1]
        if not any(local(c.tag) == "barline" for c in last):
            barline = ET.SubElement(last, "barline", location="right")
            ET.SubElement(barline, "bar-style").text = "light-heavy"

    dest.parent.mkdir(parents=True, exist_ok=True)
    xml_body = ET.tostring(root, encoding="unicode")
    dest.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" '
        '"http://www.musicxml.org/dtds/partwise.dtd">\n'
        + xml_body
        + ("\n" if not xml_body.endswith("\n") else ""),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("src", type=Path)
    parser.add_argument("dest", type=Path)
    parser.add_argument("--measures", type=int, default=16)
    parser.add_argument(
        "--title-suffix",
        default=" — excerpt: movement I, bars 1–16",
    )
    args = parser.parse_args()
    crop(args.src, args.dest, args.measures, args.title_suffix)
    print(f"wrote {args.dest} ({args.dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

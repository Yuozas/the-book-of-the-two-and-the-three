# -*- coding: utf-8 -*-
"""
Check a translated edition against the English canon.

    python3 book/check_translation.py bible-lt
    python3 book/check_translation.py bible-ru bible-lt

The build pipeline (build_ru.py / build_lt.py) re-keys build.INJECT by matching
'### ' headings positionally against the English, so a heading-count mismatch
silently drops figures out of the bound book. That failure is invisible in the
markdown and only shows up as a missing plate 140 pages into a PDF -- so it is
checked here instead of being remembered.

Rulebook: this checks STRUCTURE, not meaning. It cannot tell you a translation
is good; it can only tell you the scaffolding still lines up with the English.
A clean run is a necessary condition, never a sufficient one.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EN = ROOT / "bible"
# README.md is repo-facing, not part of the bound book; editions omit it.
SKIP = {"README.md"}

VERSE = re.compile(r"\*\*([IVX]{1,3}\.\d+|[AREV]\.\d+)\*\*")
FENCE = re.compile(r"^```", re.M)
H3 = re.compile(r"^### ", re.M)
H2 = re.compile(r"^## ", re.M)
# Inline code carrying no letters at all is pure math/notation: it must survive
# translation. Spans with letters may legitimately be translated.
#
# An inline span may wrap across a source line break -- markdown joins it back
# together, so `1/k! <=\n1/2^(k-1)` is ONE span. Matching per-line would mispair
# every backtick after the first wrapped span, so fenced blocks are stripped and
# the text is unwrapped before extraction.
FENCED = re.compile(r"^```.*?^```", re.M | re.S)
CODE = re.compile(r"`([^`]+)`")


def inline_math(text):
    flat = re.sub(r"\s+", " ", FENCED.sub("", text))
    return {re.sub(r"\s+", " ", c).strip() for c in CODE.findall(flat)
            if pure_math(c)}


def pure_math(s):
    return not re.search(r"[A-Za-zА-Яа-яЁёĄČĘĖĮŠŲŪŽąčęėįšųūž]", s)


def check(edition):
    d = ROOT / edition
    problems = []
    if not d.is_dir():
        return [f"{edition}: no such directory"]

    want = {p.name for p in EN.glob("*.md")} - SKIP
    have = {p.name for p in d.glob("*.md")}
    for missing in sorted(want - have):
        problems.append(f"{edition}/{missing}: MISSING (present in bible/)")
    for extra in sorted(have - want):
        problems.append(f"{edition}/{extra}: extra file not in bible/")

    for name in sorted(want & have):
        e = (EN / name).read_text(encoding="utf-8")
        t = (d / name).read_text(encoding="utf-8")
        tag = f"{edition}/{name}"

        for label, rx in (("### headings", H3), ("## headings", H2),
                          ("code fences", FENCE)):
            a, b = len(rx.findall(e)), len(rx.findall(t))
            if a != b:
                problems.append(f"{tag}: {label} EN={a} vs {b}")

        # Verse markers are canonical addresses -- cross-references resolve to
        # them, so the set must match exactly, in count as well as identity.
        ve, vt = VERSE.findall(e), VERSE.findall(t)
        for v in sorted(set(ve) - set(vt)):
            problems.append(f"{tag}: verse {v} lost in translation")
        for v in sorted(set(vt) - set(ve)):
            problems.append(f"{tag}: verse {v} invented (not in English)")

        me, mt = inline_math(e), inline_math(t)
        for c in sorted(me - mt):
            problems.append(f"{tag}: math `{c}` lost")
        for c in sorted(mt - me):
            problems.append(f"{tag}: math `{c}` invented")

    return problems


if __name__ == "__main__":
    editions = sys.argv[1:] or ["bible-ru", "bible-lt"]
    bad = 0
    for ed in editions:
        problems = check(ed)
        bad += len(problems)
        if problems:
            print(f"--- {ed}: {len(problems)} problem(s)")
            for p in problems:
                print("   ", p)
        else:
            print(f"--- {ed}: OK")
    sys.exit(1 if bad else 0)

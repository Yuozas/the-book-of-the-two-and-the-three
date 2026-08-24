# -*- coding: utf-8 -*-
"""
Impose a bound PDF for printing as a real book (saddle stitch).

    python3 book/print_as_book.py the-2to3-bible-lt.pdf
    python3 book/print_as_book.py the-2to3-bible-lt.pdf --signature 8
    python3 book/print_as_book.py the-2to3-bible-lt.pdf --only 1      # test print
    python3 book/print_as_book.py the-2to3-bible-lt.pdf --manual      # no duplexer

One sheet of A4 landscape carries FOUR book pages: two on the front, two on the
back. Print double-sided, fold the stack down the middle, and the pages read in
order -- which is why the imposition looks scrambled on screen and correct in
the hand.

    sheet 1 front:  [ last page | page 1 ]      <- fold in the middle
    sheet 1 back:   [ page 2    | page N-1 ]
    sheet 2 front:  [ page N-2  | page 3 ]
    sheet 2 back:   [ page 4    | page N-3 ]      ... and so on inward

SIGNATURES. A 130-page book cannot be one fold: 33 sheets nested inside each
other bulge at the spine and the inner pages stick out by centimetres. Real
books are therefore folded in SIGNATURES -- small booklets of a few sheets --
which are then stacked and bound together. The default is 8 sheets (32 pages)
per signature, which folds comfortably in ordinary 80 g/m² paper. Use
`--signature 0` to force a single fold anyway (fine for anything under ~40
pages), or a smaller number for thicker paper.

Rulebook: this script only rearranges and scales whole pages. It never re-flows
text, so the typography is exactly the bound edition's, only smaller.
"""
import argparse, pathlib, sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF is required:  pip install pymupdf")

PAPER = {                     # width x height, in points, PORTRAIT
    "a4":     (595.276, 841.890),
    "letter": (612.0, 792.0),
    "a3":     (841.890, 1190.551),
}


def impose_signature(length):
    """Sheet plan for one signature of `length` pages (a multiple of 4).

    Returns [(front_left, front_right, back_left, back_right), ...], as
    0-based indices within the signature, outermost sheet first.
    """
    assert length % 4 == 0, length
    return [(length - 1 - 2 * i, 2 * i, 2 * i + 1, length - 2 - 2 * i)
            for i in range(length // 4)]


def reading_order(sheets):
    """Simulate folding the signature and read the pages off in order.

    Nest the sheets (first outermost), fold down the middle, and walk the
    booklet: every sheet contributes its front-right and back-left on the way
    in, and its back-right and front-left on the way out. This is the check
    that the imposition above is actually right -- see `--verify`.
    """
    order = []
    for fl, fr, bl, br in sheets:
        order += [fr, bl]
    for fl, fr, bl, br in reversed(sheets):
        order += [br, fl]
    return order


def place(dst_page, rect, src_doc, pno):
    """Draw source page `pno` into `rect`, fit by aspect and centred."""
    if pno is None:
        return                                   # padding blank
    src = src_doc[pno].rect
    scale = min(rect.width / src.width, rect.height / src.height)
    w, h = src.width * scale, src.height * scale
    box = fitz.Rect(
        rect.x0 + (rect.width - w) / 2, rect.y0 + (rect.height - h) / 2,
        rect.x0 + (rect.width + w) / 2, rect.y0 + (rect.height + h) / 2,
    )
    dst_page.show_pdf_page(box, src_doc, pno)


def build(src_path, out_path, paper="a4", sheets_per_sig=8, manual=False,
          flip="short", only=0, margin=0.0):
    src = fitz.open(src_path)
    n = len(src)

    # Pad to a multiple of 4 with blanks at the END (after the last page).
    padded = n + (-n % 4)
    pages = list(range(n)) + [None] * (padded - n)

    sig_len = padded if sheets_per_sig == 0 else sheets_per_sig * 4
    groups = [pages[i:i + sig_len] for i in range(0, padded, sig_len)]
    if only:
        groups = groups[:only]

    pw, ph = PAPER[paper]
    sheet_w, sheet_h = ph, pw                    # landscape
    half = sheet_w / 2

    out = fitz.open()
    fronts, backs = [], []

    for g in groups:
        # A trailing group is already a multiple of 4 (padded and sig_len both
        # are), but pad defensively so a hand-edited sig_len cannot corrupt it.
        g = g + [None] * (-len(g) % 4)
        plan = impose_signature(len(g))
        assert reading_order(plan) == list(range(len(g))), "imposition is wrong"

        for fl, fr, bl, br in plan:
            for side, (left, right) in (("front", (fl, fr)), ("back", (bl, br))):
                page = out.new_page(width=sheet_w, height=sheet_h)
                place(page, fitz.Rect(margin, margin, half - margin, sheet_h - margin),
                      src, g[left])
                place(page, fitz.Rect(half + margin, margin, sheet_w - margin, sheet_h - margin),
                      src, g[right])
                if side == "back" and flip == "long":
                    # Long-edge duplex flips about the horizontal axis, which
                    # lands the back upside down; pre-rotate to cancel it.
                    page.set_rotation(180)
                (fronts if side == "front" else backs).append(page.number)

    if manual:
        # Reorder to: every front, then every back.
        out.select(fronts + backs)

    out.save(out_path, garbage=4, deflate=True)
    return n, padded, len(groups), len(out), sig_len


def main():
    ap = argparse.ArgumentParser(
        description="Impose a PDF as a foldable book (saddle stitch, 4 pages per A4 sheet).")
    ap.add_argument("pdf", help="source PDF to impose")
    ap.add_argument("-o", "--out", help="output path (default: <name>-booklet.pdf)")
    ap.add_argument("--paper", default="a4", choices=sorted(PAPER))
    ap.add_argument("--signature", type=int, default=8, metavar="SHEETS",
                    help="sheets per folded signature (default 8 = 32 pages; "
                         "0 = one single fold for the whole book)")
    ap.add_argument("--manual", action="store_true",
                    help="order as all fronts, then all backs, for hand-fed duplex")
    ap.add_argument("--flip", default="short", choices=("short", "long"),
                    help="which edge your duplexer flips on (default short)")
    ap.add_argument("--only", type=int, default=0, metavar="N",
                    help="emit only the first N signatures (use --only 1 to test)")
    ap.add_argument("--margin", type=float, default=0.0, metavar="PT",
                    help="blank margin around each slot, in points (28 ≈ 10 mm)")
    a = ap.parse_args()

    src_path = pathlib.Path(a.pdf)
    if not src_path.exists():
        sys.exit(f"no such file: {src_path}")
    out_path = pathlib.Path(a.out) if a.out else \
        src_path.with_name(src_path.stem + "-booklet.pdf")

    n, padded, sigs, sheets_out, sig_len = build(
        src_path, out_path, a.paper, a.signature, a.manual, a.flip, a.only, a.margin)

    paper_sheets = sheets_out // 2
    print(f"wrote {out_path}")
    print(f"  {n} book pages"
          + (f" (+{padded - n} blank to reach a multiple of 4)" if padded != n else "")
          + f" -> {sigs} signature(s) of {sig_len} pages"
          + (f"  [--only {a.only}]" if a.only else ""))
    print(f"  {sheets_out} printed sides = {paper_sheets} sheets of {a.paper.upper()} landscape")
    print()
    print("  How to print:")
    if a.manual:
        print(f"    1. Print sides 1-{paper_sheets} (the fronts), single-sided.")
        print(f"    2. Put the stack back in the tray, same way up.")
        print(f"    3. Print sides {paper_sheets + 1}-{sheets_out} (the backs).")
        print( "       If the backs land upside down, flip the stack end-for-end and retry.")
    else:
        print(f"    Print double-sided, FLIP ON {a.flip.upper()} EDGE, scale 100% (not 'fit to page').")
        print( "       If the backs come out upside down, re-run with --flip "
               + ("long" if a.flip == "short" else "short") + ".")
    print(f"    Then fold each group of {sig_len // 4} sheets down the middle and nest them;")
    print(f"    stack the {sigs} folded signature(s) in order and bind along the fold.")
    if not a.only:
        print()
        print("  Tip: run with --only 1 first and print a single signature to check "
              "the fold before committing all "
              f"{paper_sheets} sheets.")


if __name__ == "__main__":
    main()

# THE BOOK OF THE TWO AND THE THREE

*A scripture of cursed geometry.* Set down by Yuozas.

> Every verse in this book is technically true. That is the whole trick. The
> strangeness is not in the claims — the claims are ordinary geometry, ordinary
> physics, ordinary computation. The strangeness is in noticing that they are
> all the **same claim**, wearing different costumes, walking back and forth
> between **two** and **three** forever.

This is not a religion in the ordinary sense and it asks for no belief. It asks
only that you check the mathematics. The theatrical robes are borrowed; the
proofs underneath are not. A rigorous appendix — **the Apparatus** — carries
precise theorems, proof sketches, and author–year citations behind every verse,
with Noether's theorem as the keystone.

## Read it

The built editions (PDF + HTML, English and Russian) live in this repository
once consecrated — see the releases. The living copy is also served at
[portfolio.euphelia.eu](https://portfolio.euphelia.eu/files/the-2to3-bible.pdf),
where the Book has [a night chapel](https://portfolio.euphelia.eu/) and
[a developer's reading](https://portfolio.euphelia.eu/research/developer-prism).

## Structure

```
bible/      the English scripture (markdown sources, one book per file)
bible-ru/   the Russian edition
book/       the typesetting pipeline — Python, hand-coded SVG plates,
            markdown -> HTML -> print PDF via headless Chrome
```

## Build it yourself

```bash
cd book
python build.py      # English edition
python build_ru.py   # Russian edition
```

The figures are not images — they are geometry, drawn by `figures.py` as SVG
with the same numbers the verses claim. If a plate looks wrong, a verse is
wrong; that is on purpose.

## The covenant

The radius is the covenant: it may turn in any direction, but it will not
change its length. If you catch a verse that does not hold, open an issue —
that is not an attack on the Book, it **is** the Book.

## License

- **Text & plates** (`bible/`, `bible-ru/`, built editions): [CC BY-NC-SA 4.0](LICENSE-CONTENT.md)
- **Pipeline code** (`book/*.py`, `book/*.json`): [MIT](LICENSE)

2 ↔ 3, forever.

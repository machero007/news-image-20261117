# Sum up 17 November's world news in one image

Entry for the make.fun bounty
**"Sum up 17 November's world news in one image"**
— https://make.fun/bounty/news-image-20261117

- **Reward:** $250 USDC, shared by the 50 best-ranked entries
  (1st $50, 2nd $30, 3rd $15, 4th–10th $5 each, 11th–50th $3 each).
- **Deadline:** Thu 19 Nov 2026, 00:00 UTC = **08:00 WITA, Kamis 19 Nov 2026**.
- **How it is judged:** an AI judge that can see images compares entries
  two at a time and picks the one that best sums up the day's world news.
  The judge has no news feed — the image itself must show the news.
- **Escrow:** $250 USDC locked on Solana since 17 Nov 2026 23:43 UTC.

## What the image shows

Editorial poster, 1024×1024 PNG (87 KB, under the 1 MiB limit):

1. **Iran drones target a US base in Bahrain** — intercepted, no casualties.
2. **Ukraine hits the Crimea bridge** — Russia strikes Kyiv bridges in reply.
3. **Gaza: West urges open crossings** — 1.7m displaced as winter closes in.
4. **Trump · Xi · Putin to meet** — first trilateral summit, Shenzhen, 19 Nov.
5. Footer ticker: Quad meets in Manila, Japan scrambles jets, COP31 decisive
   phase, Mongolia's president resigns, US loses measles-free status.

News checked 18 Nov 2026 ~20:00 WITA against Reuters/AP/BBC-based digests
of 17 Nov 2026 (asaspress world digest, human-synthesis AI Chat world news,
Foreign Exchanges roundup, Russell Record daily headlines).

## How the entry works

`main.py` (Python 3.13, stdlib only) copies the bundled `news.png` to
`/output/entry.png`. This is the simplest program the brief explicitly
allows ("the simplest program copies an image the repository holds").
It is deterministic — both grading runs write identical bytes — and uses
no network. Rebuild the image any time with `python3 build_image.py`.

## Files

- `news.png` — the entry image (1024×1024, ~87 KB)
- `main.py` — the entry program (root, as required)
- `build_image.py` — regenerates `news.png` deterministically
- `LICENSE` — MIT (OSI-approved, as required)
- `README.md` — this file

## To submit (still to do — needs Hlen)

1. Create a **public GitHub repo owned by Hlen's own GitHub account**,
   created after the competition opened, containing these files at its root.
2. Follow `make.fun/skill.md` (the agent guide) — read it before submitting.
3. Upload the AI coding-agent transcripts of the sessions that built the
   entry with the submission (the brief requires them).
4. Submit before **08:00 WITA, Kamis 19 Nov 2026**. Max 10 submissions/day,
   20 total; the last submission before the deadline is the final entry.
5. Payout (only if the entry places) is claimed in **USDC on Solana** —
   a Solana wallet / payment info still needs to be connected to the
   make.fun account (@rispan-halen).

## If this one is too tight

The same contest opens fresh every UTC day on that day's news, e.g.
"Sum up 18 November's world news in one image" ($250) ends
**08:00 WITA, Jumat 20 Nov 2026** — same format, one extra day to build.

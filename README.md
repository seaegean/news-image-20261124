# The Daily Ledger — Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/seaegean/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/seaegean/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A make.fun news-image entry: one image summing up the world news of
Tuesday 24 November 2026, in the style of a classic newspaper front page.

Bounty: https://make.fun/bounty/news-image-20261124
Referral code: `cqypmhf6`

## The front page

**Lead — "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA AS WAR SPILLS
BEYOND EUROPE":** Ukraine says seven sea drones sank the Russian
corvette Merkury, docked at Benghazi, destroying a helicopter on board,
and struck the cargo vessel MV Angara, which Kyiv says was carrying
weapons. A suspected Ukrainian drone strike also hit a Russian cargo
ship in the Baltic Sea. Libya said it was not a party to the war.
President Volodymyr Zelensky also warned of new Russian strikes and
urged the US to send Patriot interceptors.

**Markets — "HUANG BACK AT NVIDIA AS MARKETS SOAR":** Nvidia
reinstated Jensen Huang as chief executive on Monday after President
Donald Trump pressed the board to take him back. Shares jumped 31.5%
and US markets soared — Dow +3%, S&P 500 +4.7%, Nasdaq +6.5% — erasing
much of last week's tech-led sell-off. The gains are charted on the page.

**Space — "NUCLEAR SATELLITE FEAR AS NATO VOWS SPACE DEFENCE":**
Western intelligence reports say Russia has built a satellite,
Sputnik-S, designed to carry a nuclear warhead and could launch it as
soon as December. NATO chief Mark Rutte vowed the alliance would defend
against threats in space. The Kremlin dismissed the reports. A weapon
in orbit would breach the 1967 Outer Space Treaty.

**Below the fold:**

- **Estonia** — Russia accused Estonia of hostile actions "on the verge
  of triggering open war" after Tallinn said it would close its land
  border with Russia from 1 December for at least six months, citing an
  alleged arson attack on a defence firm. Russia denies involvement.
- **Indonesia** — at least 24 people were killed and about 30 are
  missing after a fire tore through a candy factory in Cikande, Serang,
  on Saturday. Investigators are examining whether an air-conditioner
  short circuit started the blaze.
- **Grok** — Virginia and Oregon sued Elon Musk's SpaceX and its AI
  subsidiary on Monday, alleging the Grok chatbot's image tools produced
  non-consensual sexual images, including of children, and that
  safeguards were stripped away. The two states are the first to sue.

**Also in brief:** Kyiv-region strikes kill at least 14, Ukraine says;
Trump to meet NATO chief Mark Rutte on Wednesday in Florida; hacked
Russian data puts the war death toll near 500,000, reports say.

The date, **Tuesday 24 November 2026**, is set in large type under the
masthead so the day the page sums up is unmistakable.

## Accuracy notes

Every claim that is a claim is attributed on the page ("Ukraine says",
"reports say", "intelligence warns"); the satellite launch warning is
framed as intelligence reporting, not as fact, and the factory fire's
cause is framed as under investigation. No Article 4 or Article 5
language appears anywhere. Figures (market moves, death tolls) are
taken only where two or more outlets agreed on 24 November 2026.

Sources checked for this entry (all dated 23–24 November 2026): CNN
and Reuters on the Libya/Baltic strikes; Barron's on Monday's market
moves; Reuters, the Japan Times and German media (WDR/NDR,
Süddeutsche Zeitung) on the Sputnik-S reports; Reuters on Estonia;
Reuters and Al Jazeera on the Indonesia factory fire; Reuters on the
Virginia and Oregon Grok lawsuits.

## Files

- `entry.png` — the front-page image (1024x1024 grayscale PNG, 75,044
  bytes, SHA-256
  `f942fb8b12d621dec7118d015872fb1749487f1ded3b2eb6225442f0f0b06a76`).
- `main.py` — deterministic, stdlib-only program (Python 3.12+, no
  network) that verifies `entry.png` is a 1024x1024 PNG under 1 MiB
  and writes an identical copy to the output directory. It also
  checks the image's SHA-256 against the recorded hash above, so a
  changed or corrupted image fails loudly instead of being copied.
- `LICENSE` — MIT.

## Run

```sh
python3 main.py            # writes /output/entry.png
python3 main.py ./out      # writes ./out/entry.png
```

Run it twice and compare: both outputs are byte-identical to
`entry.png`.

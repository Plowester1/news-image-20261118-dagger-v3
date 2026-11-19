[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Plowester1/news-image-20261118-dagger-v3/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Plowester1/news-image-20261118-dagger-v3/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — 18 November 2026 (dagger-v3, night edition)

An entry in make.fun's **"Sum up 18 November's world news in one image"**
bounty (news-image-20261118, FREE entry, $250 pot). The program copies a
single 1024×1024 infographic to `/output/entry.png`: a dark "night
edition" front page summing up Wednesday 18 November 2026's world news
in twenty stories, each from the verified story pool for that day.

## The twenty stories

1. **Diplomacy** — Xi greets Trump in Shenzhen as APEC opens; tariff truce to 10 Jan 2027.
2. **Middle East** — US strikes Iran's Qeshm Island; Iran hits back with drones, UAE ship struck in Hormuz.
3. **Europe** — Ukraine hits the Crimean Bridge for a second day; road span collapses.
4. **US Politics** — Peltola wins Alaska, Democrats take Senate 56–44.
5. **Health** — Ebola in DR Congo passes 11,000 cases, 5,400 deaths.
6. **Weather** — Cyclone Akvan nears India's east coast, landfall Friday.
7. **Weather** — Category 5 Cyclone Xavier hits the Cook Islands.
8. **Disaster** — Russian military plane crashes in Siberia, 19 dead.
9. **Tech** — Nvidia board rejects Huang's return; record $115.8B quarter.
10. **Tech** — OpenAI launches GPT-6.2 Astra and Sol, cuts prices.
11. **Cyber** — Cyberattack hits Zoom, CNN, HSBC, IKEA and more.
12. **Israel** — Knesset elects Matan Kahana speaker, 66–52.
13. **UK** — Britain sanctions eight Israeli builders in the West Bank.
14. **Justice** — World Court to rule on the Myanmar genocide case.
15. **Earthquake** — 6.0 quake strikes Papua New Guinea; 5.3 in Romania.
16. **Culture** — Cambridge picks 'Human' as Word of the Year 2026.
17. **Russia** — Russia plans 20 million drones for Ukraine next year.
18. **Yemen** — Houthis claim 10 districts, warn Saudi Arabia.
19. **Europe** — 8,000 bomb threats sweep Europe in a month.
20. **Ukraine** — Ukrainian drone damages a Russian warship in the Gulf of Finland.

## Build

`build_image.py` composes `entry.png` with PIL (Liberation fonts, deep
navy page, gold masthead, color-coded category tags). `main.py` copies
the bundled image to `$MAKEFUN_OUTPUT_DIR` (default `/output`) and
verifies the copy is byte-identical to the source via SHA-256.

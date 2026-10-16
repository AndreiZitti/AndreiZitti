# Idle/Incremental Games: Mechanics, Progression, Prestige, and Player Sentiment

Research note (October 2026). Method: about 18 web searches and fetch attempts. Direct page fetches failed with DNS errors for gamedeveloper.com, gameanalytics.com, en.wikipedia.org and a Reddit mirror, so many findings rest on search-result excerpts of those pages, not full reads. Fan wikis and Steam discussion threads are the main sources for mechanics. Several aggregator pages (vaporlens, niklasnotes, gamegeeker) appear to be machine-generated summaries of Steam reviews; treat them as rough signals only.

## Core loops and system archetypes (with named examples)

### Takeaway
The genre splits into a few mechanical archetypes. The base of nearly all of them is generators/producers whose costs grow exponentially, with prestige resets layered on top. The archetypes differ in what they stack on that base:
- multi-skill RPG grinding (Melvor Idle)
- life-sim aging and rebirth (Progress Knight, Increlution)
- village or civilization resource management (Kittens Game, Trimps, Evolve)
- active-to-idle hybrids (Leaf Blower Revolution)
- short skill-tree arcade runs of 3–5 hours (Nodebuster)
- desktop-overlay companions (Rusty's Retirement, Bongo Cat)

### Cited Findings
**Generator stacking (Cookie Clicker, AdVenture Capitalist, Antimatter Dimensions)**
- Idle games balance production rates against costs. Costs grow exponentially while production grows more slowly. Pecorella's worked example is AdVenture Capitalist's Lemonade Stand. — [Game Developer: The Math of Idle Games Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i) (search excerpt; full text not fetched)
- AdVenture Capitalist's first business has a cost multiplier of about 1.07 per purchase ("4/1.07 ≈ 3.738$" for the first stand). — [AdVenture Capitalist fan wiki](https://adventure-capitalist.fandom.com/wiki/File:BadDay.png) (search excerpt)
- Antimatter Dimensions is built in stages: the Infinity Stage (Infinity Upgrades, Challenges, Infinity Dimensions), the Eternity Stage (Eternity Milestones, Time Dimensions, Time Studies, Time Dilation) and the Reality Stage (Glyphs, Reality Upgrades, Perks, Black Hole). Reality unlocks the Celestials, which arrived in the Reality update in December 2022. — [Antimatter Dimensions Wiki: Celestials](https://antimatter-dimensions.fandom.com/wiki/Celestials)

**Skill-grinding RPG idler (Melvor Idle)**
- Each skill has a Mastery Pool. Filling it unlocks perks at checkpoints of 10%, 25%, 50% and 95%. The base-game pool total is 20,000,000 XP. — [Melvor Wiki: Fishing](https://wiki.melvoridle.com/w/Fishing)
- Each Mastery Token adds 0.1% of the maximum pool XP to its skill's pool. Token drop chances differ between the level 99 cap and the level 120 cap. — [Melvor Wiki: Mastery Tokens](https://wiki.melvoridle.com/w/Mastery_Tokens)
- The Throne of the Herald expansion raises the level cap for many skills to 120. Without it, levels have no mechanical effect past 99. — [Melvor Wiki: FAQ](https://wiki.melvoridle.com/w/FAQ); [Melvor Wiki: Throne of the Herald guide](https://wiki.melvoridle.com/w/Throne_of_the_Herald/Guide)
- Township is a city-building skill. Unlike Farming, it has no Mastery levels and progresses on its own tick system. Township level 120 requires Throne of the Herald. — [Melvor Wiki: Township](https://wiki.melvoridle.com/w/Township)
- The Atlas of Discovery expansion adds Cartography and Archaeology. Cartography requires Archaeology for 100% completion. — [Steam discussion: How is Atlas of Discovery now?](https://steamcommunity.com/app/1267910/discussions/0/4413047330420501156/)
- The "Ancient Relics" mode is a restricted game mode. One reviewer likened it to "a New Game Plus or Post-Game for a JRPG." — [Steam review of Atlas of Discovery](https://steamcommunity.com/profiles/76561198056323344/recommended/2492940); [Steam discussion](https://steamcommunity.com/app/1267910/discussions/0/4342103279866837375/)

**Life-sim with aging and rebirth (Progress Knight, Increlution)**
- In Progress Knight, the player chooses a job and a skill to train, and the character ages. Rebirth uses the amulet and unlocks at age 65; it becomes forced at 70, when the lifespan ends. Rebirth keeps a max-level XP multiplier, scaling with each job or skill's max level divided by 10, so relearning goes faster. — [Progress Knight Wiki](https://progress-knight.fandom.com/wiki/Progress_knight_Wiki); [Progress Knight Quest Wiki: Rebirths](https://progress-knight-quest.fandom.com/wiki/Rebirths)
- The second layer in Progress Knight is Evil. It unlocks at age 200 and requires Immortality level 660. An Evil Rebirth grants Evil, a persistent token that multiplies the Dark Magic skill ladder. Reaching Evil thresholds unlocks new Dark Magic skills. — [Progress Knight Wiki](https://progress-knight.fandom.com/wiki/Progress_knight_Wiki)
- Fan forks add further layers. Progress Knight 2.0 and Quest add Transcend, which multiplies max levels by Cosmic Recollection and yields Essence. The Quest wiki lists Eye, Void, Transcend and Collapse. — [Progress Knight Quest Wiki](https://progress-knight-quest.fandom.com/wiki/Rebirths); [Progress Knight 2.0](https://symb1.github.io/progress_knight_2/)
- Increlution is "an incremental built entirely on dying well": death is the core progression mechanic. The game is designed around queueing and automating actions, and automation slots unlock only after high completion counts. — [PlayWanderer review](https://playwanderer.online/game-reviews/increlution); [incrementaldb review](https://www.incrementaldb.com/community/review/4288); [Steam: How far have you automated?](https://steamcommunity.com/app/1593350/discussions/0/3061869473061553889/)

**Resource/civilization management (Kittens Game, Trimps, Evolve)**
- Kittens Game is a village-themed game with multiple prestige levels. Trimps is broadly similar but built around quests and combat. — [Quarter To Three forums](https://forum.quartertothree.com/t/some-incremental-idle-clicker-games-including-really-a-lot-of-incremental-epic-hero-2/145358)
- In Trimps, maps are where equipment upgrades ("prestiges") come from. Void Maps are rarer and harder and drop Heirlooms. — [coolidlegames: Trimps](https://coolidlegames.com/games/trimps); see also [Incremental Game Review: Trimps (itch devlog)](https://drhernandez1002.itch.io/system-design-blog/devlog/144095/incremental-game-review-trimps)
- One player's view of Evolve: "prestige just starts you out faster next time." The energy mechanic is rate-capped to create an artificial time limit. — [Quarter To Three forums](https://forum.quartertothree.com/t/some-incremental-idle-clicker-games-including-really-a-lot-of-incremental-epic-hero-2/145358)

**Faction-based prestige (Realm Grinder)**
- Realm Grinder has six core factions on a Good/Evil/Neutral alignment axis, plus prestige factions (elite versions). Dragons are the neutral prestige faction. Reincarnation resets progress but keeps permanent gains. As reincarnation count rises, more unlocks open: Dwarf/Drow treaties, Druid/Titan/Faceless affiliations, and Mercenaries that can use two spells from different factions. Players often switch factions mid-run, e.g. Elf/Goblin, then Titan, then Elf. — [TV Tropes: Realm Grinder](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/RealmGrinder); [Steam: reincarnation discussion](https://steamcommunity.com/app/610080/discussions/0/1489987634000397190/); [JayIsGames review](https://jayisgames.com/review/realm-grinder.php)

**Active-to-idle hybrid (Leaf Blower Revolution)**
- Leaf Blower Revolution keeps adding systems late. A long-time player: "every time I think I'm getting near the endgame the game throws an entirely new and unique concept at me." It is free-to-play and its gameplay is "not limited by in-game purchases." — [leafblowerguide.com review](https://www.leafblowerguide.com/blog/leaf-blower-revolution-review/); [Google Play listing](https://play.google.com/store/apps/details?id=com.ezplugins.leafblowerrevolution&hl=en_GB)

**Bite-sized upgrade-tree arcade incrementals (Nodebuster, Gnorp Apologue, Unnamed Space Idle, Ballionaire)**
- Nodebuster was completed in "just over four hours" by one reviewer, who praised the pacing and an "intuitive and well streamlined" skill tree. Another reviewer finished in about 3.5 hours; health upgrades are the main early blocker. — [Mancunion review](https://mancunion.com/2025/05/08/nodebuster-review-a-short-and-sweet-incremental-game/); [Higher Plain Games review](https://higherplaingames.com/pc/nodebuster-review/)
- Reviewers praise (the) Gnorp Apologue for its look and feel. Reported times run from about 16 hours to 48.8 hours for 100%, and much of that is overnight idling. — [Steam Community: Gnorp Apologue](https://steamcommunity.com/app/1473350); [Steam discussion](https://steamcommunity.com/app/1473350/discussions/0/4038104133466644335/?l=danish)
- Ballionaire is a pachinko roguelike, an adjacent genre rather than a pure incremental. It sits at roughly 86% positive on about 2,500 reviews (aggregator). Praise is for addictiveness; criticism targets balance, RNG and replayability. — [vaporlens: Ballionaire](https://vaporlens.app/app/2667120/ballionaire/stats/details); [Steam Deck HQ review](https://steamdeckhq.com/game-reviews/ballionaire/)
- Unnamed Space Idle is a free-to-play game released July 27, 2023. It is about 93% positive on about 4,300 reviews (3,991 positive / 318 negative per one aggregator). Reviewers with 20h+ played are about 95% positive, while under-2h reviewers are more mixed. Complaints: slow start, steep learning curve. — [vaporlens: Unnamed Space Idle](https://vaporlens.app/app/2471100/unnamed_space_idle/stats/details); [gamegeeker](https://gamegeeker.com/games/unnamed-space-idle)
- ResetEra has a thread on "bite-sized incremental games," which suggests a recognized sub-genre. — [ResetEra thread](https://www.resetera.com/threads/bite-sized-incremental-games.1087230/)

**Desktop companion idlers (Rusty's Retirement, Bongo Cat)**
- Rusty's Retirement is an idle farming sim that runs in a strip at the bottom of the screen. It sold over 100,000 copies in its first week (April 2024) and 550,000 by July 2025. GameDiscoverCo estimated about 330,000 copies a few months after launch, at about $5 net per unit. — [Wikipedia: Rusty's Retirement](https://en.wikipedia.org/wiki/Rusty%27s_Retirement) (search excerpt); [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed)
- The developer celebrated "spawning a genre." Followers include My Little Life (Nine Finger Games) and Tiny Pasture. — [GamesRadar](https://www.gamesradar.com/games/simulation/after-selling-100000-copies-of-its-idle-stardew-valley-like-rustys-retirement-dev-celebrates-spawning-a-genre-of-games-that-run-at-the-bottom-of-your-screen/); [gamepressure](https://www.gamepressure.com/newsroom/from-rustys-retirement-to-tiny-pasture-the-new-wave-of-desktop-bu/z679b4)
- Bongo Cat was inspired by Rusty's Retirement and was reported as Steam's #4 most-played title, with about 150,000 daily concurrents in 2025. — [gamer.org](https://www.gamer.org/bongo-cat-isnt-a-game-so-why-is-it-steams-4-title/) (secondary source; verify on SteamDB)

**Idle RPG / hero collectors (Legends of Idleon)**
- Idleon is a multi-character idle MMO. A 2026 analysis reports multiple progression "walls," veterans complaining that the idle element has disappeared (the device needs to be on 24/7), and severe monetization criticism. — [Vortex Gaming](https://vortexgaming.io/en/postdetail/721245)

### Inferences
- Across archetypes, the base engine (exponential costs against slower production growth, plus resets) is shared. What sets an archetype apart is the **theme of the reset**:
  - life/death (Progress Knight, Increlution)
  - a new reality or dimension (Antimatter Dimensions)
  - a faction choice (Realm Grinder)
  - no reset at all, using a level cap plus mastery instead (Melvor Idle)

  The theme is where story and visuals can attach most naturally to mechanics.
- Melvor shows that a "no-prestige" structure works: many parallel skills that feed each other, mastery as a slow second axis, and paid expansions that raise caps and add skills. It also shows the risk: new skills must integrate with existing loops (see complaints).
- Bite-sized incrementals of 3–5 hours with a real ending, and desktop overlays, are the two commercially visible growth areas on Steam since 2024. Both reject endless F2P structures.

### Gaps
- I could not find primary detail on Cookie Clicker (ascension, heavenly chips), NGU Idle's many systems, Idle Champions, Idle Slayer, Idle Loops (time-loop with mana), Evolve's specific prestige types, or automation/factory-lite idlers. Searches for Idle Slayer and Idle Champions returned only Leaf Blower Revolution results.
- I found no source on Ballionaire's or The Gnorp Apologue's specific upgrade-tree structures.

## Prestige/reset design and pacing techniques

### Takeaway
Prestige means resetting most progress in exchange for a persistent currency or multiplier that speeds the next run. Good games stack two to five layers, each with its own currency, and each new layer adds whole new systems (challenges, new generator types, research trees), not just bigger multipliers. Pacing comes from exponential costs, milestones that grant automation, and thresholds tied to completion counts.

### Cited Findings
- Pecorella's definition: prestige is "a reset that keeps some progress, gaining currency (prestige currency) and/or persistent multipliers to accelerate the next time through." Part III of the series covers "prestige loops and patterns," analyzing real-world examples "and how to vary them to keep things interesting." The series is based on publicly released spreadsheet models. — [Game Developer: Math of Idle Games Part III](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii); [Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i) (search excerpts only)
- Part II covers "alternative growth models and generator relevancy," i.e. keeping early generators useful. — [Game Developer: Part II](https://www.gamedeveloper.com/game-platforms/the-math-of-idle-games-part-ii)
- Antimatter Dimensions has three named layers (Infinity, then Eternity, then Reality), and each adds a system cluster:
  - Infinity: Challenges and Infinity Dimensions
  - Eternity: Time Studies tree, Eternity Milestones, Time Dilation
  - Reality: Glyph equipment, Perks, Black Hole, and Celestials as endgame "bosses"

  — [Antimatter Dimensions Wiki](https://antimatter-dimensions.fandom.com/wiki/Celestials)
- Progress Knight has two native layers. Rebirth is forced at age 70 and keeps XP multipliers. Evil requires age 200 and Immortality 660; it yields a new token that powers a new skill ladder. Forks go to six or more layers. — [Progress Knight Wiki](https://progress-knight.fandom.com/wiki/Progress_knight_Wiki); [PK Quest Wiki](https://progress-knight-quest.fandom.com/wiki/Rebirths)
- Realm Grinder adds faction-choice prestige, where each reincarnation unlocks new factions and alliances. Each reincarnation starts with no gems, so the early run is harsh. — [Steam: Realm Grinder reincarnation](https://steamcommunity.com/app/610080/discussions/0/1489987634000397190/); [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/RealmGrinder)
- Increlution gates automation behind completion counts. Players cite the 400-completion and 8-completion requirements as too high, and some quit early because of them. — [Steam discussion](https://steamcommunity.com/app/1593350/discussions/0/4626981776940619365)
- AdVenture Capitalist's angel investors (its prestige currency) need about 44.4B lifetime earnings for the 1st angel, 177.8B for the 2nd and 400B for the 3rd. Each angel adds +2% to profits. — [Steam discussion](https://steamcommunity.com/app/346900/discussions/0/364039531219683031); [Steam discussion](https://steamcommunity.com/app/346900/discussions/0/487870763318777936)
  - These thresholds fit a quadratic formula (lifetime ∝ angels², i.e. angels ∝ √lifetime). That is my own derivation from 44.4/177.8/400 ≈ 1:4:9; the source does not state it.
- Community advice: time resets so that restarting overtakes continuing. — [West Games prestige timing calculator](https://west-games.com/idle-game-prestige-timing-calculator/)
- Players want "several prestige layers and increasing unlocks of automation, as the game becomes more complex." — [r/incremental_games, "What makes an idle game fun" (Aug 2024)](https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3)
- Melvor Idle uses level caps and mastery checkpoints (10/25/50/95%) instead of resets; expansions raise the cap from 99 to 120. — [Melvor Wiki: Fishing](https://wiki.melvoridle.com/w/Fishing)

### Inferences
- A common structure: each layer reset (a) wipes the previous layer's currency, (b) grants a new currency spent on a new upgrade tree, (c) unlocks automation of the previous layer through milestones, and (d) introduces one or two novel mechanics. Antimatter Dimensions is the clearest example. The automation milestones turn the previous layer into a "free" background process, and that change is what the reveal feels like.
- Prestige yield usually scales sub-linearly (square root or similar) with run earnings, as AdVenture Capitalist's angel thresholds imply. This produces diminishing returns per run and a natural "when to reset" decision.
- Gates based on completion counts or tokens (Increlution) are a high-risk pacing tool. They create strong walls if thresholds are high.

### Gaps
- I could not retrieve the full text of Pecorella's Part III. Specific prestige formulas or the full list of cost-growth rates (e.g. the commonly cited AdVenture Capitalist range of 1.07–1.15) were not verified in this research.
- I found no sourced material on softcaps (as in Antimatter Dimensions or The Prestige Tree) or on NGU Idle's systems. Antimatter Dimensions' exact reset contents per layer were not verified.

## Offline progress, active vs idle balance, playthrough length

### Takeaway
Players expect offline progress, and the details are contentious: caps, averaged RNG, and "leave it on overnight" requirements all draw complaints. Length is bimodal. Bite-sized games of about 3–5 hours (Nodebuster) or 16–50 hours (Gnorp) have a defined end; F2P or live games (Leaf Blower Revolution, Idleon, Unnamed Space Idle) run to hundreds of hours with continuous content.

### Cited Findings
- Leaf Blower Revolution players complain that a newer offline system "throws out averages from RNG elements like fruits, seeds, and enemies" and so "ruins offline progression." Another said parts of the game make it feel like "I need to leave the game on overnight to progress." Offline coin earnings are reportedly capped around 1e16. — [Steam: New offline calculations are kinda bad](https://steamcommunity.com/app/1468260/discussions/0/3004430047194342712/); [leafblowerguide.com](https://www.leafblowerguide.com/blog/leaf-blower-revolution-review/)
- Idleon veterans complain that the game now effectively requires the device on 24/7, so the "idle" element has disappeared. — [Vortex Gaming](https://vortexgaming.io/en/postdetail/721245)
- An indie devlog singles out Trimps for friction-reducing features: a display of time until the next upgrade, and offline simulation that catches up on time away. — [itch.io devlog: How to make a good game](https://tinytakinteller.itch.io/the-best-game-ever/devlog/739972/interlude-week-6-how-to-make-a-good-game)
- A design paper argues a good idle game should be "fun without playing the game." — [KPI repository paper](https://repository.kpi.kharkov.ua/server/api/core/bitstreams/6aee56d1-21ab-4ef4-bb35-9baf71adf24e/content) (search excerpt)
- Reported lengths:
  - Nodebuster: about 3.5–4 hours. — [Higher Plain Games](https://higherplaingames.com/pc/nodebuster-review/); [Mancunion](https://mancunion.com/2025/05/08/nodebuster-review-a-short-and-sweet-incremental-game/)
  - Gnorp Apologue: about 16–49 hours, mostly idle. — [Steam](https://steamcommunity.com/app/1473350)
  - Space Plan: about 2 days of active play, praised. — [r/incremental_games thread](https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun)
  - Unnamed Space Idle: 79% of reviews come from players with 20h+ played. — [vaporlens](https://vaporlens.app/app/2471100/unnamed_space_idle/stats/details)
  - Increlution: one early-access player reported 400 hours. — [GameLoop page](https://www.gameloop.com/game/steam-game/increlution-on-pc) (third-party page)
- Evolve rate-caps energy to create an artificial time limit, an example of timer-based gating. — [Quarter To Three](https://forum.quartertothree.com/t/some-incremental-idle-clicker-games-including-really-a-lot-of-incremental-epic-hero-2/145358)
- Desktop idlers (Rusty's Retirement) are designed to run while the player does other work, which pushes the idle end of the spectrum to its extreme. — [GamesRadar](https://www.gamesradar.com/games/simulation/after-selling-100000-copies-of-its-idle-stardew-valley-like-rustys-retirement-dev-celebrates-spawning-a-genre-of-games-that-run-at-the-bottom-of-your-screen/)

### Inferences
- Offline progress that is deterministic and transparent avoids the most common grievance. An uncapped (or generously capped) offline simulation with a "while you were away" summary does this; averaged RNG and hidden caps break trust.
- Active play should speed things up; it should not be required. The complaint pattern in Idleon and Leaf Blower Revolution is games that drifted from idle to "must be open."
- A 3–10 hour target fits the bite-sized premium model ($5–15) that reviewers reward for "respecting time." The endless model fits F2P or live-service, with its known content-drought and monetization risks.

### Gaps
- No hard data was found on median playthrough lengths (e.g. HowLongToBeat) for Melvor Idle, Antimatter Dimensions, Progress Knight, Cookie Clicker or Kittens Game.
- No sourced data was found on standard offline cap lengths (e.g. 8h/12h/24h) across mobile idlers.

## Most-praised design elements

### Takeaway
Players praise games where the player's decisions shape how the numbers grow. They also praise new systems revealed late ("every time I think I'm near the endgame..."), automation unlocked as complexity rises, short games with a satisfying end, the absence of pay-to-win, and polished presentation and feel.

### Cited Findings
- "Numbers go up, but in a way that I can influence with smart decisions. Good loops, preferably several prestige layers and increasing unlocks of automation." — [r/incremental_games, Aug 2024](https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3)
- Players praise Leaf Blower Revolution because it keeps revealing "an entirely new and unique concept" near the apparent endgame. — [leafblowerguide.com](https://www.leafblowerguide.com/blog/leaf-blower-revolution-review/)
- A commentator on Melvor Idle and Farm RPG names "calm progression punctuated by bursts of epiphany and dopamine" as the core trait of the best examples. — [jmduke.com](https://jmduke.com/posts/post/wizrobe)
- Nodebuster: pacing is a strength, and the skill tree is "intuitive and well streamlined"; its shortness is praised by some players. — [Mancunion](https://mancunion.com/2025/05/08/nodebuster-review-a-short-and-sweet-incremental-game/)
- Space Plan is praised for being finishable (about 2 days) and fun throughout. — [r/incremental_games](https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun)
- Gnorp Apologue: "very satisfying to play and visually appealing." — [Steam Community](https://steamcommunity.com/app/1473350)
- Increlution: players praise death as the core progression mechanic and the queue/automation system. — [PlayWanderer](https://playwanderer.online/game-reviews/increlution); [GameLoop](https://www.gameloop.com/game/steam-game/increlution-on-pc)
- Melvor's Ancient Relics mode is praised as a New Game Plus-style twist, and the DLC's low price is appreciated. — [Steam review](https://steamcommunity.com/profiles/76561198056323344/recommended/2492940); [niklasnotes aggregator](https://niklasnotes.com/dashboard/game/88630/melvor_idle_atlas_of_discovery)
- Players value non-predatory F2P. Leaf Blower Revolution is praised as "not limited by in-game purchases," with optional IAP and no ads. Unnamed Space Idle (F2P) holds about 93% positive. — [leafblowerguide.com](https://www.leafblowerguide.com/blog/leaf-blower-revolution-review/); [vaporlens](https://vaporlens.app/app/2471100/unnamed_space_idle/stats/details)
- Trimps is praised for its QoL: time-to-next-upgrade displays and offline catch-up. — [itch.io devlog](https://tinytakinteller.itch.io/the-best-game-ever/devlog/739972/interlude-week-6-how-to-make-a-good-game)

### Inferences
- The praised "discovery" moment works best when a reset reveals a new tab or system. The genre's strongest emotional beat is a reveal, not raw growth. Story and visuals can be timed to these reveals.
- Respecting player time spans both ends of the market: short complete games, and long games that automate tedium as it appears.

### Gaps
- I did not retrieve primary Steam review text for Melvor Idle's base game, Progress Knight, or Antimatter Dimensions' Steam release, so praise for those is inferred from wiki and forum context, not quoted reviews.

## Most common complaints

### Takeaway
The recurring complaints:
- progression walls that force grind
- monetization pressure
- requirements to be "always on" or play actively, which undercut the idle promise
- currencies that sit unused
- tedium in the core loop
- shallow click-when-highlighted play when numbers grow too fast
- new systems that do not integrate with existing ones
- abandoned development, unfinished story or no ending
- games that end too soon, or overstay their welcome

### Cited Findings
- Idleon: multiple progression walls that require grinding, "severe" monetization criticism, and the game effectively needing to stay on 24/7. — [Vortex Gaming (2026)](https://vortexgaming.io/en/postdetail/721245)
- Indie idle reviewers: "you have a bunch of currencies and you don't even use them until later in the game"; a game "requires active attention," undercutting the idle premise. — [itch.io post](https://itch.io/post/11430602); [itch.io post](https://itch.io/post/14862561)
- Dodecadragons is criticized because numbers grow so fast that "you just click buttons as they highlight." — [r/incremental_games thread](https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun)
- Players reject battle passes: "no battle passes, please." — [r/incremental_games](https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3)
- Increlution:
  - Repeating the same act for two days. — [Steam Community](https://steamcommunity.com/app/1593350?l=english)
  - Efficient play turns tedious, and "an unattended meal can kill you and waste a whole generation." — [Steam: A mixed review](https://steamcommunity.com/app/1593350/discussions/0/3940147280192817912/)
  - Automation thresholds are too high. — [Steam](https://steamcommunity.com/app/1593350/discussions/0/4626981776940619365)
  - The last substantive update is years old and the story is unfinished. — [PlayWanderer](https://playwanderer.online/game-reviews/increlution)
- Melvor Idle: Atlas of Discovery sits at Mixed, 59% positive of 241 reviews. It was about 94% positive at launch. — [Steam store page](https://store.steampowered.com/app/2492940/Melvor_Idle_Atlas_of_Discovery/); [Linux Game Consortium](https://linuxgameconsortium.com/melvor-idle-atlas-of-discovery-out-now/)
  - The complaints center on the "barrier combat portion" (later patched with QoL), confusing mechanics, grindy progression, new skills that don't integrate with existing play, and Cartography depending on Archaeology. — [Steam discussion](https://steamcommunity.com/app/1267910/discussions/0/4413047330420501156/); [niklasnotes aggregator](https://niklasnotes.com/dashboard/game/88630/melvor_idle_atlas_of_discovery)
  - One player warned the expansion can be expensive in in-game gold. — [Steam review (Japanese)](https://steamcommunity.com/profiles/76561198124068957/recommended/2492940)
- Leaf Blower Revolution: averaged-RNG offline calculation, the need to leave it on overnight, and "cryptic" progression that "feels useless" (Android review). — [Steam](https://steamcommunity.com/app/1468260/discussions/0/3004430047194342712/); [AppBrain](https://www.appbrain.com/app/leaf-blower-revolution-idle/com.ezplugins.leafblowerrevolution)
- Nodebuster: one reviewer gave it 7/10, saying it "overstays its welcome"; others said it ended too soon. Short-game expectations are split. — [Steam Community: Nodebuster](https://steamcommunity.com/app/3107330); [Steam discussion](https://steamcommunity.com/app/3107330/discussions/0/6929437211297706726)
- Unnamed Space Idle: progression is "very slow, especially at the start," with a steep learning curve. — [vaporlens](https://vaporlens.app/app/2471100/unnamed_space_idle/stats/details)
- Ballionaire: balance, RNG reliance, replayability. — [vaporlens](https://vaporlens.app/app/2667120/ballionaire/stats/details)
- Realm Grinder: each reincarnation's start with no gems is harsh. — [Steam](https://steamcommunity.com/app/610080/discussions/0/1489987634000397190/)

### Inferences
- The two most damaging failure modes are (1) a slow, confusing opening; Unnamed Space Idle's under-2h reviewers are its most negative group. (2) Late expansions that bolt on systems which don't feed the existing economy (Melvor Atlas).
- The first 30–60 minutes need fast reveals. Every new currency should have an immediate use.

### Gaps
- I found no quantified ranking of complaint frequency across the genre. The ordering above is qualitative, based on recurrence across sources.
- No sourced material on "it's just a spreadsheet," UI bloat, or late-game balance collapse (e.g. Antimatter Dimensions or NGU inflation) beyond indirect mentions.

## Design writing and talks

### Takeaway
The canonical design reference is Anthony Pecorella's three-part "Math of Idle Games." Pecorella produced AdVenture Capitalist at Kongregate. Part I covers growth, cost, prestige and generator balance; Part II covers alternative growth models and keeping generators relevant; Part III covers prestige loops and patterns. Public spreadsheet models back all three parts. His GDC talks ("Quest for Progress," GDC Europe 2016) trace the genre to Progress Quest (2002).

### Cited Findings
- Series overview and authorship: originally posted on the Kongregate Developer Blog and republished on Game Developer and GameAnalytics. — [Game Developer Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i); [Part II](https://www.gamedeveloper.com/game-platforms/the-math-of-idle-games-part-ii); [Part III](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii); [GameAnalytics author page](https://gameanalytics.com/author/anthony-pecorella)
- "Quest for Progress: The Math and Design of Idle Games" (GDC Europe 2016): its graphs come from public spreadsheets. — [SlideShare](https://www.slideshare.net/slideshow/quest-for-progress-gdc-europe-2016/65405507)
- Pecorella credits Progress Quest (2002) as the first self-playing game. — [Game Developer: The rise of games you mostly don't play](https://www.gamedeveloper.com/design/the-rise-of-games-you-mostly-don-t-play)
- An independent system-design blog reviews Trimps from a design perspective. — [Game Developer / itch devlog: Incremental Game Review: Trimps](https://www.gamedeveloper.com/design/incremental-game-review-trimps)
- 2025–26 indie postmortems apply this theory directly, e.g. "I built 7 idle games in 30 days" and a prestige-economy design writeup. — [DEV Community](https://dev.to/aguier/i-built-7-idle-games-in-30-days-what-i-learned-about-incremental-design-5d3f); [DEV Community](https://dev.to/tanishpaul1106/aura-data-and-prestige-designing-the-economy-of-doomscroll-2077-293f)
- Steam idle revenue trends in 2026 were examined by a lower-authority site. — [NextBigGames](https://nextbiggames.com/2026/05/09/idle-games-on-steam-revenue-trends-2026/)

### Inferences
- A designer should start from Pecorella's spreadsheets for cost/production/prestige curves. The genre's newer commercial successes (Nodebuster, Gnorp, Rusty's Retirement) suggest the math is a solved baseline; what differentiates games is theme, feel, reveal pacing and a defined ending.

### Gaps
- I could not access the Kongregate blog originals or GDC Vault pages directly. DNS failed for gamedeveloper.com and gameanalytics.com, and search excerpts did not include formulas.
- I found no Eric Guan GDC talk material in this research.
- Melvor Idle's base-game and Progress Knight's Steam review corpora were not retrieved in full.

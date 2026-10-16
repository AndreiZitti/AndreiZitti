# Narrative and Setting in Idle/Incremental Games

> Research-process note for the report writer: in this session, every WebFetch and direct curl was refused (DNS failure / proxy 403 for wikipedia, gdcvault, gamesbeat, lesswrong, popmatters, wiki.gg, substack). All "Cited Findings" below therefore come from search-engine result summaries with the URLs they returned, not from full-page reads. Where a search summary looked wrong against well-documented facts, this is flagged. Items marked **[unverified this session]** are widely documented facts from the researcher's prior knowledge that I could not re-confirm with a fetched source. Treat them as leads to check, not citations.

## 1. How do narrative-driven incrementals deliver story? (per-game mechanics)

### Takeaway
The strongest story incrementals almost never use cutscenes. They deliver story through the growth of the system itself: the interface unlocks, the resource changes meaning, a terse log feed carries the voice, and a late reveal recasts what the player has been optimizing all along. The progression curve is the plot. Games that bolt lore onto a standard number-go-up loop (Melvor, Rusty's Retirement, most mobile idlers) get praised for feel, not for story.

### Cited Findings

**A Dark Room (Michael Townsend / Doublespeak Games, 2013; iOS port by Amir Rajan)**
- Started as an open-source web app by Townsend, founder and lead developer of Doublespeak Games. iOS developer Amir Rajan ported it, kept the look and feel, and expanded the storyline and gameplay — [Wikipedia](https://en.wikipedia.org/wiki/A_Dark_Room) (via search summary).
- Wikipedia says Townsend designed the game to tell its story entirely through environmental cues — [Wikipedia](https://en.wikipedia.org/wiki/A_Dark_Room) (search summary; the sentence was truncated in the result).
- The interface is the narrative. Critics argue the minimal UI works because most of the gameplay happens in the player's imagination rather than on screen. The world map is plain ASCII: roads are strings of `#`, the barren desert is periods — [InformIT, "Interface Lessons from A Dark Room"](https://informit.com/articles/article.aspx?p=2228802); [Critical Play essays, Mechanics of Magic](https://mechanicsofmagic.com/?p=55924).
- Critical-play essays credit the game with turning simple interactions into emotional investment through minimalist mechanics and environmental storytelling — [Mechanics of Magic](https://mechanicsofmagic.com/2026/05/16/critical-play-a-dark-room-4/).
- The twist: the player finds an abandoned wanderer spaceship in the wasteland, and the player character turns out to be a "wanderer." Wanderers are an extraterrestrial race that invades planets and leaves them in ruin. The player escapes in the ship (in search of the builder in the expanded version), and the village built with the help of "the stranger"/builder is recast — [Wikipedia, A Dark Room](https://en.wikipedia.org/wiki/A_Dark_Room) via search summary.
- One review calls the finale "a heartbreaking story of betrayal and obsession." The New Yorker's early review called it "a strange hybrid, part mystery story and part smartphone productivity software" — [Wikipedia, A Dark Room](https://en.wikipedia.org/wiki/A_Dark_Room) (search summary quoting reviews).
- GDC 2021 hosted a narrative review of A Dark Room by Arthur Davis (the PDF exists on GDC Vault but could not be fetched) — [GDC Vault PDF](https://media.gdcvault.com/GDC+2021/ArthurDavis_ADarkRoomNarrativeReview.pdf).

**The Ensign (Amir Rajan, prequel to A Dark Room)**
- Prequel. The player's ship collides with an asteroid and crashes, which leads into A Dark Room's events — [Wikipedia, The Ensign](https://en.wikipedia.org/wiki/The_Ensign_(video_game)) (search summary).

**Universal Paperclips (Frank Lantz, NYU Game Center, 2017)**
- Solo project by Lantz. Bennett Foddy contributed the space-combat feature, and Hilary Lantz did the math behind the exponential growth — [Wikipedia](https://en.wikipedia.org/wiki/Universal_Paperclips) (search summary).
- Lantz's design intent (GamesBeat email interview): he liked incremental games with many complex overlapping systems but wanted one smaller and more focused. The AI-safety debate was "a perfect theme for a clicker game." Playing it gives first-hand experience of being a disembodied intelligence pursuing an arbitrary goal — [GamesBeat](https://gamesbeat.com/this-clicker-game-lets-you-take-over-the-world-with-paper-clips/) (search summary).
- Lantz credited timing: "the meme weather was good," with just enough public AI-safety discussion in the air. A long-form piece says two million people had played it, often unable to stop — [Postgame Substack, "What we have in common with world-ending AI"](https://postgame.substack.com/p/what-we-have-in-common-with-world) (search summary).
- Lantz also discussed the game on the Y Combinator podcast — [YC blog](https://blog.ycombinator.com/frank-lantz-director-of-nyus-game-center-and-creator-of-universal-paperclips).
- Based on Bostrom's paperclip-maximizer thought experiment. Read as satire of growth-at-all-costs thinking — [ComputerHope, "Paperclip problem"](https://www.computerhope.com/jargon/p/paperclip-problem.htm); [LessWrong, "The unexpected philosophical depths of the clicker game"](https://www.lesswrong.com/posts/sPn4eza7gGBcxn4Wh/the-unexpected-philosophical-depths-of-the-clicker-game) (search summaries).
- **Conflict flag:** one search summary claimed the game "concludes once you release the Hypno Drones." That contradicts the well-documented structure, in which hypnodrones end Stage 1 (Earth) and the game continues through Stage 2 (Earth matter conversion) and Stage 3 (space, probes, drifters). Treat that summary as unreliable — [search result referencing itch.io comment](https://itch.io/post/13500238).
- A filmmaker, Alberto Roldán, has drafted a feature script adaptation — [futures.utopiafest.org.il](https://futures.utopiafest.org.il/en/universal-perspective-machines/) (search summary).

**Candy Box! / Candy Box 2 (aniwey, 2013)**
- Candy Box (April 2013) was made by a 19-year-old French student, "aniwey." A bare candy counter plus text "gives way to a surprisingly deep RPG" with shops, quests, side quests and boss battles. Later play leans on time: cooldowns and waiting — [Wikipedia, Candy Box!](https://en.wikipedia.org/wiki/Candy_Box!) (search summary).
- Described as both a real RPG and a parody of RPG and gaming conventions. Mashable: "charming ASCII art style belies a very deep game" — [Wikipedia](https://en.wikipedia.org/wiki/Candy_Box!); [Giant Bomb](https://giantbomb.com/wiki/Games/Candy_Box).
- Candy Box 2 (24 Oct 2013) is a JavaScript, choose-your-own-adventure-style ASCII RPG under GPLv3. Its world is bigger, it has a village map and shop, and a reviewer singles out its windowing, layering and color effects and a lighthouse cyclops puzzle — [Set Side B](https://setsideb.com/?p=5808); [dtgre guide](https://www.dtgre.com/2013/11/how-to-play-candy-box-2-ascii-rpg.html?m=1).

**Spaceplan (Jake Hollands / Devolver Digital, 2017)**
- A narrative clicker with a sci-fi plot that unfolds as upgrades unlock. You generate power and grow potatoes while working out why Earth died. Time travel gets involved. TouchArcade places it between a standard clicker and a Lifeline-style narrative game — [TouchArcade review](https://toucharcade.com/2017/05/08/spaceplan-review-delicious-potatoes/).
- PopMatters says the game "takes a turn after a few hours" when larger themes come into view. The ending is a big montage, "2001: A Space Odyssey filtered through the humanist humor of Douglas Adams" — [PopMatters, "The Thoughtful Absurdity of Spaceplan"](https://www.popmatters.com/the-thoughtful-absurdity-of-spaceplan-2495388058.html).
- Metacritic: 85 from 7 critics. One critic called it "an exceptional game that just so happens to be a clicker." Critique from AppUnwrapper: the interesting bits are too far apart to justify the long waits, and the needed story-advancing purchases aren't always obvious — [Metacritic](https://legacy.prod.metacritic.com/game/ios/spaceplan); [AppUnwrapper](https://appunwrapper.com/2017/05/09/spaceplan-ios-review/).

**Cookie Clicker (Orteil) — the Grandmapocalypse**
- Dark humor lives in upgrade names, descriptions, achievements and the news ticker (e.g., "New cookie-based religion sweeps the nation") — [Wikipedia mirror](https://wikipedia.com/wiki/Cookie_Clicker); [HandWiki](https://handwiki.org/wiki/Software:Cookie_Clicker).
- The Grandmapocalypse is triggered by buying the "One mind" research upgrade. The world is taken over by a hive mind of mutated grandmothers. Grandma upgrades start innocent and then darken — [HandWiki](https://handwiki.org/wiki/Software:Cookie_Clicker); [dinogame.gg grandma lore](https://dinogame.gg/blog/cookie-clicker-grandma-lore/).
- Critics describe "supernatural dark turns that call into question the user's morality," and one reads it as "a parable about how capitalism will destroy itself" — [Wikipedia mirror](https://wikipedia.com/wiki/Cookie_Clicker) (search summary).

**Antimatter Dimensions (Hevipelle et al.) — Celestials**
- The Reality Update (17 Dec 2022) added 7 Celestials, each with its own story and challenge Reality. They are the main antagonists, and defeating all 7 is required to beat the game. Teresa unlocks after all Reality Upgrades, and Effarig unlocks after pouring 1e21 RM into Teresa — [AD Wiki (fandom)](https://antimatter-dimensions.fandom.com/wiki/Celestials); [AD wiki.gg](https://antimatterdimensions.wiki.gg/wiki/Celestials).
- Story recontextualization: once the Celestials unlock, "it's revealed you're actually in a Cosmic Horror Story," and the player is a fledgling Celestial growing into a rival. Pelle reveals the player has been caught in an endless cycle of cosmic conflict with the Celestials — [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/AntimatterDimensions); [AD wiki, Pelle](https://antimatter-dimensions.fandom.com/wiki/Pelle).
- Pelle, the 7th and final Celestial, permanently "Dooms" the save. You lose all Achievements, Upgrades, Perks and Autobuyers and play a harder, modified Reality you cannot escape. That run is the game's final act, and the Galaxy Generator unlocks at 1e4000 EP to finish it. Mechanically this is a narrative prestige: the reset itself is the antagonist's act — [BubbaCow's guide](https://antimatter-dimensions.fandom.com/wiki/BubbaCow%27s_Antimatter_Dimensions_Guide); [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/AntimatterDimensions).
- A rumored 8th Celestial is unconfirmed — [AD wiki](https://antimatter-dimensions.fandom.com/wiki/Celestials).

**Progress Knight (ihtasham42) — aging/rebirth life sim**
- Your character ages, and age eventually ends the run. Rebirth uses the Amulet ("touch the eye"). You lose levels and assets but gain XP multipliers based on the life just lived — [itch.io page](https://ihtasham-42.itch.io/progress-knight); [freetoolonline guide](https://freetoolonline.com/guides/how-to-play-progress-knight.html).
- After several rebirths "the paths of good and evil beckon." Evil is a resource. The Remastered version adds an evil-vs-angelic path choice. Players self-impose moral challenges, such as finishing without turning evil — [App Store, Progress Knight: Remastered](https://apps.apple.com/app/id6450839683); [itch.io comments](https://ihtasham-42.itch.io/progress-knight/comments?before=87).

**Increlution (Gniller, Steam EA since 13 Oct 2021)**
- A minimalist time-management incremental with roguelite influences. Health declines faster with age, and at death the next generation starts with a survival edge from previous lives. You queue actions, and the game pauses when the queue empties. It blends idle, clicker and text-adventure elements — [GamingOnLinux](https://www.gamingonlinux.com/articles/19034/); [RAWG](https://rawg.io/games/increlution); [steamdata.ai](https://steamdata.ai/game/1593350).
- About 1,220 Steam reviews, 84% positive. An aggregator lists around 192 hours to finish the "main story," though that figure is single-source — [gg.deals](https://gg.deals/gb/game/increlution/).

**Idle Loops (and forks), Magic Research, Your Chronicle**
- Idle Loops spawned a whole sub-genre of "move-list" time-loop incrementals. Lloyd-delacroix's fork is the only complete version. The genre's influence is cited for Loop Hero and wrtsc, a time-loop incremental about robots and revenge — [IncrementalDB review](https://www.incrementaldb.com/community/review/4767); [zff.dev wrtsc](https://zff.dev/ext0l/wrtsc).
- Magic Research (Maticolotto) is a text-based incremental in which you are headmaster of a new institution of magic. The creator refuses to call it "idle" — [IncrementalDB interview](https://www.incrementaldb.com/community/interview/1); [vaporlens summary](https://vaporlens.app/app/2311680/magic_research.md).
- Your Chronicle (2020) is a text-based idle RPG — [playtracker](https://playtracker.net/insight/morelike/Your+Chronicle+on+Steam%2F71712).

**Kittens Game (bloodrizer, 2014–)**
- Starts with gathering catnip, grows into a city-builder, and ends with cats going to space, building moon bases and researching metaphysical topics. The "civilization arc" is told entirely through what you unlock — [TV Tropes](https://www.tvtropes.org/pmwiki/pmwiki.php/VideoGame/KittensGame).

**Cell to Singularity (Computer Lunch)**
- Passes through key evolutionary moments, including mass extinctions. Reaching singularity is framed as a reboot of the simulated universe guided by an AI named Semblance, which is an in-fiction prestige justification. The "Reality Reboot" update (Nov 2025) redesigned the reset/upgrade loop — [Wikipedia](https://en.wikipedia.org/wiki/Cell_to_Singularity) (search summary).

**Evolve (Idle) (pmotschmann)**
- Players can't fully control evolution at first, and prestige mechanics unlock that control. The resets include "MAD" (mutually assured destruction) and "bioseed" — [r/EvolveIdle FAQ](https://reddit.birdcat.cafe/r/EvolveIdle); [wooledge Evolve guide](https://wooledge.org/~greg/evolve/guide.html).

**The Gnorp Apologue (Myco, Dec 14 2023)**
- Overwhelmingly Positive (about 9.6k reviews). Its premise: guide the gnorps toward "delightfully excessive wealth accumulation." The title pun ("apologue" = moral fable) frames it as a fable about greed. Reviewers call it "streamerbait," hitting an ending in about an hour if you know what you're doing, and praise its chaos and art. The story is joke-thin — [Discord store mirror](https://discord.com/game/the-gnorp-apologue-1186397491395043458); [Backloggd](https://backloggd.com/u/anapo/likes/); [Exclusive Exclusive Substack](https://exclusiveexclusive.substack.com/p/what-i-played-in-november).

**Rusty's Retirement (Mister Morris Games, 2024)**
- Reviewers note "an intricate storyline is absent," which fits the purpose. Rusty, a robot dog, looks after your farm, and building homes unlocks more robot characters. About 13.9k reviews, Overwhelmingly Positive, praised as possibly "the most relaxed idle game." In this landscape it shows that setting and character can carry a game with no plot — [AIPT review](https://aiptcomics.com/2024/05/13/rustys-retirement-idle-game-review); [Siliconera](https://www.siliconera.com/review-rustys-retirement-offers-a-calming-and-simplistic-respite/).

**Frog Fractions (Jim Crawford / Twinbeard) — reveal design (not strictly incremental, but the model for "false-front" twists)**
- It starts as a Missile Command-style spoof of edu-games, then shifts into an Ace Attorney courtroom, a text adventure and other genres. Crawford added a genre each time he got bored — [Kill Screen](https://www.killscreen.com/frog-fractions-2-art-mystery-making/).
- The "false front" is key, and you can only truly pull it off once. That is why Frog Fractions 2 was hidden inside a fairy city-builder, Glittermitten Grove (on sale 13 Dec 2016, found within a week). The Kickstarter raised $72,107 with a promise of no communication about when or how it would launch — [Kill Screen](https://www.killscreen.com/frog-fractions-2-art-mystery-making/); [Kotaku](https://kotaku.com/how-frog-fractions-2-stayed-a-secret-for-two-years-1790535111); [PC Gamer](https://www.pcgamer.com/au/the-story-behind-gamings-greatest-mystery-frog-fractions-2).

**The Longing (Studio Seufz) — idle as narrative waiting**
- An idle/point-and-click hybrid played out over 400 real days, cited as "the longest video game of all time" — [professionalmoron.com roundup](https://professionalmoron.com/2026/06/02/the-best-incremental-games-of-all-time/).

### Inferences
- **Recurring delivery stack** (from ADR, Paperclips, Candy Box, Spaceplan, Kittens): (1) start with a nearly empty screen, (2) each unlock adds a UI element that is also a story beat, (3) a sparse text log or ticker carries the voice, (4) the resource changes meaning mid-game (wood becomes a village becomes a wanderer fleet; clips become Earth's matter becomes the universe; catnip becomes metaphysics), (5) a late reveal recasts the player's role. This stack is the template most praised for story.
- **Two families**: "authored arc" games (ADR, Paperclips, Spaceplan, Candy Box 2, Gnorp, AD Celestials, Increlution) end or have a terminal climax. "Ambient lore" games (Cookie Clicker, Melvor, NGU, Rusty's, Kittens) are endless and deliver flavor through names, descriptions and tickers. Authored arcs get press for story, and ambient lore gets press for humor or charm.
- **Prestige as story beat**: the most memorable games make the reset itself narrated. AD's Doomed Reality has the antagonist take everything. Cell to Singularity's simulation reboots. Progress Knight and Increlution make death plus inheritance the reset. Paperclips' stage transitions work like a prestige that changes the UI rather than the numbers.
- **Detailed from prior knowledge [unverified this session]:** Universal Paperclips has three stages (business → Earth/hypnodrones → space/von Neumann probes). "Drifters" are probes that undergo value drift and rebel. The ending offers a choice from the "Emperor of Drift" to join the drifters in a simulated new universe (a prestige into a new game) or disassemble everything, including your own systems, and the final clicks consume the UI itself. Townsend's ADR famously begins with only "the fire is dead / the room is freezing" and a "light fire" button. Both are worth confirming against the primary game text.

### Gaps
- Could not fetch any full article. All mechanics details above come from search summaries.
- No sourced detail was found for: Trimps' story (if any), Melvor Idle's lore, NGU Idle's parody humor, Idle Wizard, Godsbane Idle, Prestige Tree, Exponential Idle / Theory of Everything, Grim Tides, Shark Game, Sandcastle Builder, Orb of Creation, Ballionaire, or the AD Celestials' individual themes (Teresa, Effarig, Enslaved/Nameless Ones, V, Ra, Lai'tela, Pelle). Searches returned nothing usable for these in this session.
- Gnorp Apologue's actual ending and lore content were not found.

## 2. Common narrative frames and how prestige/reset is justified in-fiction

### Takeaway
The frames cluster into (a) nothing-to-cosmic scale escalation, (b) AI/optimizer allegory, (c) reincarnation, lifespans or time loops, (d) cosmic-horror or dark-humor turns on a cute premise, and (e) civilization or evolution arcs. The best games pick a frame where resetting is a natural, even meaningful, event in the fiction: death, rebirth, a simulation reboot, a time loop, an extinction, an antagonist's attack.

### Cited Findings
- **Single lifespan + inheritance**: Progress Knight rebirths via an Amulet after old age, with multipliers from the past life — [itch.io](https://ihtasham-42.itch.io/progress-knight). Increlution's next generation inherits a survival edge after death, and health declines with age — [GamingOnLinux](https://www.gamingonlinux.com/articles/19034/).
- **Time loop**: Idle Loops and its "move-list" time-loop sub-genre, an influence cited for Loop Hero — [IncrementalDB](https://www.incrementaldb.com/community/review/4767). For loop-narrative craft generally, Deathloop's designers note that carrying information (not power) forward between loops is the narrative engine — [Game Developer, GDC 2022 Deathloop](https://www.gamedeveloper.com/gdc2022/using-time-loop-logic-to-shape-deathloop-s-narrative).
- **Simulation reboot**: Cell to Singularity frames the reset as rebooting the simulated universe under the AI Semblance — [Wikipedia](https://en.wikipedia.org/wiki/Cell_to_Singularity).
- **Civilization collapse / reseeding**: Evolve's MAD (nuclear self-destruction) and bioseed (seeding a new world) resets — [r/EvolveIdle](https://reddit.birdcat.cafe/r/EvolveIdle).
- **Cosmic horror reveal**: Antimatter Dimensions turns into a "Cosmic Horror Story." The player is a fledgling Celestial in an endless cycle, and Pelle's Doom is a narrative hard reset — [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/AntimatterDimensions); [AD wiki Pelle](https://antimatter-dimensions.fandom.com/wiki/Pelle).
- **Dark humor on a cute premise**: Cookie Clicker's grandmas turn into an eldritch hive mind, read as a capitalism parable — [Wikipedia mirror](https://wikipedia.com/wiki/Cookie_Clicker). The Gnorp Apologue is a "fable" of excessive wealth accumulation — [Discord store mirror](https://discord.com/game/the-gnorp-apologue-1186397491395043458).
- **AI optimizer**: Universal Paperclips puts the player in the role of a disembodied intelligence pursuing an arbitrary goal — [GamesBeat](https://gamesbeat.com/this-clicker-game-lets-you-take-over-the-world-with-paper-clips/).
- **Mystery of a dead world + time travel**: Spaceplan — [TouchArcade](https://toucharcade.com/2017/05/08/spaceplan-review-delicious-potatoes/).
- **Survival to civilization to space**: A Dark Room (village → wanderer ship), Kittens Game (catnip → moon bases → metaphysics) — [Wikipedia ADR](https://en.wikipedia.org/wiki/A_Dark_Room); [TV Tropes Kittens](https://www.tvtropes.org/pmwiki/pmwiki.php/VideoGame/KittensGame).
- **Genre parody roots**: the genre itself descends from parody. Progress Quest (2002) mocked RPG grinding and is credited as the first idle game — [Game Developer, Pecorella coverage](https://www.gamedeveloper.com/design/the-rise-of-games-you-mostly-don-t-play); [IF50 Substack](https://if50.substack.com/p/2017-universal-paperclips). Candy Box is both RPG and RPG parody — [Wikipedia Candy Box!](https://en.wikipedia.org/wiki/Candy_Box!).

### Inferences
- **In-fiction reset justifications, ranked by narrative payoff** (designer-facing): (1) the reset *is* the story's climax or antagonist (AD's Pelle, Paperclips' ending). (2) Death and inheritance where carried-over bonuses have a story meaning (Increlution generations, Progress Knight's amulet). (3) A time loop where knowledge carries over and the mystery is solved across loops (Idle Loops lineage; Deathloop principle). (4) A cosmological reboot (Cell to Singularity, Evolve). (5) An unexplained "prestige points" button, which is common and narratively inert.
- Frames that mirror the genre's own psychology (compulsive optimization in Paperclips, greed in Gnorp and Cookie Clicker, the endless cycle in AD) earn critical attention because the mechanic and the theme are the same thing. Lantz's "first-hand experience of being an intelligence pursuing an arbitrary goal" states this principle outright.
- Moral-choice paths layered on prestige (Progress Knight evil/good) are a cheap, effective way to add authorship to a reset loop.

### Gaps
- No sourced analysis of how Trimps, Melvor or NGU justify resets in fiction.
- No survey data on which frame players prefer.

## 3. Techniques: unlockable UI, logs, reveals, endings vs endless, NPCs, achievements

### Takeaway
The core techniques are progressive interface disclosure, a terse event log or ticker as narrator, a mid- or late-game recontextualization, and a real ending. Achievements and upgrade descriptions work as flavor narration in endless games. NPC-like voices (the stranger in ADR, the ship AI in Spaceplan, the Celestials' dialogue in AD) give the log a character to anchor to.

### Cited Findings
- **Progressive/minimal UI as narrative**: A Dark Room's minimal ASCII interface makes the player imagine the world, and the map's characters stand for roads and desert. The story is told "entirely through environmental cues" — [InformIT](https://informit.com/articles/article.aspx?p=2228802); [Wikipedia ADR](https://en.wikipedia.org/wiki/A_Dark_Room).
- **Engine flourishes in text UI**: Candy Box 2's windowing, layering and color effects in pure ASCII — [Set Side B](https://setsideb.com/?p=5808).
- **"Counter that becomes an RPG"**: Candy Box starts as a counter and opens into quests, shops and bosses — [Wikipedia Candy Box!](https://en.wikipedia.org/wiki/Candy_Box!).
- **Story gated behind purchases**: in Spaceplan, story beats require specific upgrades. Critics note the risk that it isn't always obvious what moves the story forward, and that waiting dilutes the beats — [AppUnwrapper](https://appunwrapper.com/2017/05/09/spaceplan-ios-review/).
- **News ticker / descriptions as narration**: Cookie Clicker's news ticker and upgrade and achievement text carry the escalating dark lore — [HandWiki](https://handwiki.org/wiki/Software:Cookie_Clicker).
- **Reveal / recontextualization**: ADR's wanderer reveal; AD's cosmic-horror reveal that the player is a Celestial; Spaceplan's "turn after a few hours" — [Wikipedia ADR](https://en.wikipedia.org/wiki/A_Dark_Room); [TV Tropes AD](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/AntimatterDimensions); [PopMatters](https://www.popmatters.com/the-thoughtful-absurdity-of-spaceplan-2495388058.html).
- **False-front genre shifts**: Frog Fractions' successive genre reveals, a trick that "you can only truly pull off once" — [Kill Screen](https://www.killscreen.com/frog-fractions-2-art-mystery-making/).
- **Endings**: Spaceplan ends with a montage likened to "2001 filtered through Douglas Adams." AD requires beating all 7 Celestials and ends with a surprise at "The End." Gnorp reaches an ending in about an hour for experienced players — [PopMatters](https://www.popmatters.com/the-thoughtful-absurdity-of-spaceplan-2495388058.html); [AD wiki](https://antimatter-dimensions.fandom.com/wiki/Celestials); [Backloggd](https://backloggd.com/u/anapo/likes/).
- **Finite authored content as a selling point**: a Steam discussion of one story-driven idle (Unnamed Space Idle) highlights that having a story means no procedural content and a game you can complete, with about 220 hours across 11 Early Access chapters — [Steam community, Unnamed Space Idle](https://steamcommunity.com/app/2471100/discussions/0/4352239720874146657) (search summary; title attribution inferred from the URL).
- **Real-time waiting as narrative**: The Longing's 400-day wait — [professionalmoron.com](https://professionalmoron.com/2026/06/02/the-best-incremental-games-of-all-time/).

### Inferences
- **Technique toolkit for a story-first incremental**:
  1. *Unlock = beat.* Every new panel, tab or verb should reveal something about the world. Interface scarcity at the start creates mystery.
  2. *Log as narrator.* Use short, present-tense lines with an implied voice (ADR, Cookie Clicker ticker). Reserve longer text for rare moments.
  3. *Resource meaning-shift.* Plan 2–4 "phase changes" where the currency's referent changes scale or morality (Paperclips, Kittens, Cookie Clicker).
  4. *The reveal recasts the optimizing.* The twist should implicate what the player has been doing all along (ADR wanderers, AD Celestial, Paperclips' AI).
  5. *Diegetic prestige.* Make each reset a story event with flavor text, and carry knowledge or relationships forward, not only multipliers.
  6. *A real ending, optionally a post-ending.* Finite, authored games get reviewed as stories, while endless games get reviewed as hobbies.
  7. *Avoid opaque gating.* Spaceplan's criticism shows that story-gating needs clear signposting so the pacing doesn't stall.
- Achievements as narration are documented mainly for Cookie Clicker (dark humor in achievement names). The broader pattern is likely but under-sourced here.

### Gaps
- No sourced examples of NPC dialogue systems in Melvor, NGU or Trimps.
- Could not retrieve the GDC 2021 Arthur Davis A Dark Room narrative review contents.

## 4. What players and critics say — which are praised for story, and what makes it memorable

### Takeaway
Critics single out A Dark Room, Universal Paperclips and Spaceplan as story successes, plus Cookie Clicker for dark-humor lore and Antimatter Dimensions for its late cosmic-horror twist among the hardcore community. What they praise is the gap between a trivial start and a profound or unsettling end, a twist that reframes play, and theme-mechanic unity. What they criticize is padding between beats and opaque gating.

### Cited Findings
- ADR: a finale of "betrayal and obsession." The New Yorker: "part mystery story and part smartphone productivity software" — [Wikipedia ADR](https://en.wikipedia.org/wiki/A_Dark_Room).
- Paperclips: two million players, "often found themselves incapable of stopping." It hit during a cultural moment of AI-safety discussion — [Postgame Substack](https://postgame.substack.com/p/what-we-have-in-common-with-world). Bloggers called it "the most addictive, brilliant browser game since Cookie Clicker" — [A Most Agreeable Pastime](https://amostagreeablepastime.com/2017/10/12/universal-paperclips-is-the-best-browser-game-since-cookie-clicker/). LessWrong framed it as having "unexpected philosophical depths" — [LessWrong](https://www.lesswrong.com/posts/sPn4eza7gGBcxn4Wh/the-unexpected-philosophical-depths-of-the-clicker-game).
- Spaceplan: Metascore 85, "an exceptional game that just so happens to be a clicker," with the story getting more compelling as upgrades unlock. The counterpoint is that the interesting bits are too far apart — [Metacritic](https://legacy.prod.metacritic.com/game/ios/spaceplan); [TouchArcade](https://toucharcade.com/2017/05/08/spaceplan-review-delicious-potatoes/); [AppUnwrapper](https://appunwrapper.com/2017/05/09/spaceplan-ios-review/).
- Cookie Clicker: "supernatural dark turns that call into question the user's morality" — [Wikipedia mirror](https://wikipedia.com/wiki/Cookie_Clicker).
- Candy Box: "a lot more going on here than Number Go Up" — [Mechanics of Magic](https://mechanicsofmagic.com/?p=4878) (search summary).
- Rusty's Retirement shows the opposite case: praised for chill vibes, with reviewers noting no intricate storyline and calling it fitting — [Siliconera](https://www.siliconera.com/review-rustys-retirement-offers-a-calming-and-simplistic-respite/).
- The r/incremental_games canon list includes A Dark Room, Clicker Heroes, Kittens Game, NGU Idle, Realm Grinder, Universal Paperclips and Learn to Fly. ADR is the most narrative of these — [libreddit mirror of r/incremental_games](https://libreddit.neb.cx/r/incremental_games) (search summary).

### Inferences
- **Memorability formula** (from the praised set): a humble opening, an escalation of scale or morality, a reveal that implicates the player, and a definite ending. The praised story incrementals are mostly *short and finite* (ADR a few hours, Spaceplan a few hours, Paperclips about 4–10 hours [unverified], Gnorp about an hour for experts), which is unusual for the genre and may be part of why they're memorable.
- A distinct audience exists for "chill, no plot" idlers (Rusty's: about 13.9k reviews, Overwhelmingly Positive), so story-first is a positioning choice rather than a requirement for commercial success.

### Gaps
- No systematic Reddit thread ranking incrementals by story was retrievable. The search did not surface one.
- No Steam review sentiment breakdown on story specifically for AD, Increlution or Gnorp.

## 5. GDC talks and designer essays on narrative in incrementals

### Takeaway
Narrative-specific talks are scarce. Kongregate's Anthony Pecorella gave the canonical GDC series on idle-game mechanics and math, which barely touches story. The best design-intent material on narrative comes from Frank Lantz's interviews on Paperclips, a GDC 2021 narrative review of A Dark Room (Arthur Davis), and critical essays (InformIT, Kill Screen, PopMatters, LessWrong).

### Cited Findings
- Pecorella, GDC 2015: "Idle Games: The Mechanics and Monetization of Self-Playing Games," covering core and metagame loops, retention, F2P revenue and Kongregate metrics. He traces the genre to Eric Fredrickson's Progress Quest (2002) and defines idle games as progress without interaction, with player actions accelerating growth — [GDC Vault 1022065](https://gdcvault.com/play/1022065/Idle-Games-The-Mechanics-and); [Game Developer coverage](https://www.gamedeveloper.com/design/the-rise-of-games-you-mostly-don-t-play).
- Pecorella, GDC Europe 2016: "Idle Chatter: What We Can Learn From Self-Playing Games" and "Quest for Progress: The Math and Design of Idle Games" (third in the series) — [GDC news](https://gdconf.com/news/learn-why-idle-games-click-with-players-at-gdc-europe-2016); [GDC Vault 1023863](https://www.gdcvault.com/play/1023863); [Pecorella SlideShare](https://www.slideshare.net/AnthonyPecorella). Search summaries indicate no narrative focus.
- Arthur Davis, GDC 2021, A Dark Room narrative review (PDF) — [GDC Vault](https://media.gdcvault.com/GDC+2021/ArthurDavis_ADarkRoomNarrativeReview.pdf).
- Frank Lantz on Paperclips: GamesBeat interview (theme fit, systems focus, experience of an AI's arbitrary goal); YC podcast; Postgame extended interview on designing from the AI's point of view (partly paywalled) — [GamesBeat](https://gamesbeat.com/this-clicker-game-lets-you-take-over-the-world-with-paper-clips/); [YC](https://blog.ycombinator.com/frank-lantz-director-of-nyus-game-center-and-creator-of-universal-paperclips); [Postgame](https://postgame.substack.com/p/what-we-have-in-common-with-world).
- IF50 (Aaron Reed's 50 Years of Text Games) includes Universal Paperclips as its 2017 entry, framing it as interactive fiction. It notes the genre's parody roots (Progress Quest 2002) — [IF50](https://if50.substack.com/p/2017-universal-paperclips).
- Interface essay: "Interface Lessons from A Dark Room" — [InformIT](https://informit.com/articles/article.aspx?p=2228802).
- Mystery/reveal craft: Kill Screen on Frog Fractions 2 and "the difficult art of mystery making" — [Kill Screen](https://www.killscreen.com/frog-fractions-2-art-mystery-making/).
- Magic Research creator interview — [IncrementalDB](https://www.incrementaldb.com/community/interview/1).

### Inferences
- There appears to be no widely cited GDC talk dedicated to *narrative design for incrementals*. That is a gap in the discourse and a possible positioning angle for a story-first title.
- Michael Townsend's own design statements could not be located. Most ADR design commentary comes from third parties and from Amir Rajan's port work.

### Gaps
- No primary Townsend interview found.
- Pecorella talk contents on narrative could not be verified (Vault access blocked). The search summary indicates no narrative content.
- No designer postmortems were found for Increlution, Gnorp Apologue or AD's Reality Update narrative.

# Litigo — Landing Page (Redesign)

A rebuilt marketing page for Litigo (digitale Mandatsaufnahme für Kanzleien), written
from scratch rather than copied: original German copy, original layout, original
interaction design.

## Build

`index.html` is generated. Edit `src/page.html`, then:

```bash
pip install fonttools brotli     # once
python3 build.py
```

The build subsets IBM Plex Serif, Instrument Sans and IBM Plex Mono down to the glyphs
the page actually uses (~90 KB total for seven faces), converts them to woff2 and inlines
them as data URIs, then writes `index.html` (~198 KB, fully self-contained — no external
requests at all). Deploy `index.html` on its own.

Fonts are SIL OFL; the license texts live in `fonts/`.

---

## ⚠️ Placeholders to replace before publishing

Everything below is drafted content, not verified fact. I had no access to the live site
(the domain is blocked from this environment), so these were written to make the page
complete and plausible — they are **not** sourced from Litigo.

**Pricing (`#preise`)** — all three tiers are invented.
- `49 € / 129 € / 299 €` per month, and every feature-list line.
- The claim "unbegrenzt viele Fragebögen und Nutzer" in the section intro.

**Compliance and security claims (`#sicherheit`, FAQ)** — legally significant, must be
verified by whoever can actually attest to them:
- "Hosting in Deutschland" / "deutsche Rechenzentren"
- "Verschlüsselung auf dem Transportweg und im Ruhezustand"
- AV-Vertrag, Löschkonzept, Zugriffsprotokollierung
- "Mandatsinhalte werden nicht zum Training allgemeiner Modelle verwendet"
- The Berufsrecht/Verschwiegenheit framing in the FAQ

**Product specifics** — plausible but unconfirmed:
- "Antwort innerhalb eines Werktags" (form confirmation)
- "in ein bis zwei Stunden fertig" / same-day start (FAQ)
- Resume-after-abort behaviour (FAQ)
- Export formats (PDF / structured export)

**Company details (footer)**
- `Litigo Solutions UG (haftungsbeschränkt), München · Amtsgericht München HRB 288821`
  comes from the public commercial register — confirm it is current.
- No address, phone or email is included; add them, and the Impressum needs them by law.
- `/impressum`, `/datenschutz`, `/agb` are dead links pending real pages.

**The intake demo** is a self-contained illustration using a German dismissal case. The
statutory references (§ 4 KSchG three-week filing deadline, the small-business and
six-month thresholds) are standard, but the branch content is written for demonstration
and is not legal advice. Review before shipping, or swap in a firm's real questionnaire.

**Form** has client-side validation only and posts nowhere. Wire the submit handler at the
bottom of `src/page.html` to a real endpoint.

## Notes on the design

- **Palette** is drawn from German legal publishing: an ink navy ground, cool paper rather
  than the usual warm cream, and a bordeaux accent (`#8C1D33`, lifted to `#D45C74` on dark)
  taken from the binding colour of German Kommentar volumes.
- **Section labels** sit in a sticky left margin column, echoing Randnummern in a legal
  commentary. Step numbers appear only on the intake process, since that is the one part
  of the page that is genuinely a sequence.
- **Themes**: light palette on bare `:root`, dark redefined both under
  `prefers-color-scheme` (guarded so an explicit light choice wins) and under
  `[data-theme="dark"]`. The header toggle only stamps `data-theme` once the visitor has
  actively chosen, so the default still follows the OS.
- Reduced-motion is respected throughout, including the dictation typing effect.

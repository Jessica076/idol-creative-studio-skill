<div align="center">

# Idol Creative Studio ✦ 偶像创意工坊

**Upload one photo. Get a wallpaper, sticker, or photocard — inside your own AI workspace.**

上传一张照片，在你自己的 Codex / ChatGPT 环境中制作饭制壁纸、透明贴纸和收藏小卡。

[![Skill](https://img.shields.io/badge/Codex-Skill-111827)](https://developers.openai.com/codex/skills)
[![No owner API key](https://img.shields.io/badge/owner_API_key-not_required-16a34a)](#how-usage-works)
[![Tests](https://img.shields.io/badge/tests-unittest-2563eb)](#development)
[![License: MIT](https://img.shields.io/badge/license-MIT-f59e0b)](LICENSE)

</div>

## What it creates

| Wallpaper | Sticker sheet | Photocard |
|---|---|---|
| Lock-screen-safe composition | People stay realistic | Front/back collectible design |
| Phone and desktop sizes | Objects become bold color blocks | Album, birthday, luxury concepts |
| Luxury, dreamy, dark, retro | Opaque palette-matched paper | Safe margins and exact ratio |

The skill asks the host's available image editor to preserve the reference person's identity, checks common generation defects, and labels potentially confusing designs as unofficial fan-made work.

Sticker sheets default to a tall **16:25 portrait canvas** (recommended `1600×2500`), matching the approved reference layout: full and balanced with natural breathing room and no heavy overlap.

## Install from GitHub

Ask Codex:

```text
$skill-installer install https://github.com/Jessica076/idol-creative-studio-skill
```

Then invoke it explicitly:

```text
$idol-creative-studio 把我上传的照片做成黑银奢华风生日小卡，文字写 “HAPPY J DAY”
```

Or use a natural request after installation:

```text
Turn my attached concert photo into a cinematic iPhone lock-screen wallpaper.
```

```text
把照片里的人物和代表性物品拆成一整页贴纸：人物保持真实，物品用大色块画风，背景用与原图匹配的奶油纸张色，不要透明底。
```

If the skill does not appear immediately, restart Codex. Availability of image generation/editing depends on the user's product, plan, workspace policy, region, and current usage limits.

## How usage works

- This repository contains instructions and local utilities; it does not ship a hosted image API.
- It does not contain, collect, proxy, or require the repository owner's OpenAI API key.
- Image work runs through tools available to the installing user's Codex/ChatGPT environment and is subject to that user's account access and limits.
- The optional prompt builder runs locally and makes no network requests.

This means the maintainer does not pay per-user API charges. It does **not** mean image generation is universally free or unlimited.

## Try it

```bash
python scripts/generate_prompt.py \
  --type photocard \
  --style "black and silver luxury editorial" \
  --text "HAPPY J DAY"
```

The command only creates a portable editing prompt. It never reads an API key or sends data over the network.

## Designed for sharing

- Chinese and English trigger phrases
- Three focused, repeatable workflows
- Built-in identity and output QA checklist
- Clear fan-made and rights guardrails
- No backend, database, signup, telemetry, or maintainer credentials
- Portable `SKILL.md` plus `agents/openai.yaml` metadata

## Project map

```text
.
├── SKILL.md                 # Trigger metadata and core workflow
├── agents/openai.yaml       # Skill picker metadata
├── workflows/               # Wallpaper, sticker, photocard playbooks
├── styles/                  # Reusable art-direction guides
├── config/                  # Size and quality rules
├── scripts/                 # Local prompt and image utilities
└── tests/                   # Offline unit tests
```

## Responsible fan creation

Do not use this project for sexualized minors, harassment, impersonation, fabricated endorsements, or counterfeit “official” merchandise. Commercial users are responsible for image, publicity, trademark, and font rights.

## Development

```bash
python -m unittest discover -s tests -v
python scripts/generate_prompt.py --type sticker --style "pastel cute fan style"
```

Pillow is optional and only required by the local resize helper.

Contributions that add a reusable workflow, improve identity preservation, or add real before/after examples with proper rights are welcome.

## License

[MIT](LICENSE) · Fan-made project; not affiliated with or endorsed by any artist, agency, or platform.

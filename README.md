# GEO / AEO Optimization Skill (LLM Visibility)

This repository contains the `geo-llm-optimization` skill: a practical framework, checklists, templates, and an audit script to improve how websites and brands get **retrieved, cited, and recommended** by generative search engines and LLMs (ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude).

## What’s included

- `geo-llm-optimization/SKILL.md`: the skill entrypoint and workflow.
- `geo-llm-optimization/references/`: the 6-layer playbook (Infrastructure → Monitoring).
- `geo-llm-optimization/assets/`: ready-to-use templates (`llms.txt`, JSON-LD schema templates).
- `geo-llm-optimization/scripts/audit_geo.py`: a lightweight automated audit (Python stdlib only).
- `geo-llm-optimization.skill`: packaged skill bundle.

## Install

Pick one of the options below (depending on how you manage skills in your setup):

1. **Folder-based**: copy the `geo-llm-optimization/` directory into your skills directory.
2. **Bundle-based**: import/use `geo-llm-optimization.skill` if your skill runner supports `.skill` bundles.

## Usage

- Start with `geo-llm-optimization/SKILL.md` and follow the “Recommended workflow”.
- Run the automated audit when you have a target site:

  `python3 geo-llm-optimization/scripts/audit_geo.py https://example.com`

## Repository “About” (suggested)

GitHub repository description:

> GEO/AEO optimization skill: checklists, templates, and an audit script to improve visibility in LLM answers (ChatGPT, Perplexity, AI Overviews).

Suggested topics:

`geo` `aeo` `llm-seo` `generative-engine-optimization` `answer-engine-optimization` `schema-org` `json-ld` `llms-txt` `seo`

## Contributing

See `CONTRIBUTING.md`.

## License

MIT — see `LICENSE`.


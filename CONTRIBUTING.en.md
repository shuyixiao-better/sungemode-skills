# Contributing

Useful contributions include observed decision failures, reproducible installation issues, better evidence rules, bilingual corrections, and vendor-documented tool adapters.

1. Keep Chinese `SKILL.md` and English `SKILL.en.md` equivalent in names, constraints, metrics, record paths, and authorization scope.
2. Each skill must stand alone. Keep templates/resources local, without links to sibling skills or external project files. Load detail only when needed.
3. Update both `agents/openai.yaml` and `agents/openai.en.yaml`. Prompts mention `$skill-name`; short descriptions contain 25–64 characters.
4. Date and cite market facts. Label examples real/fictional, anonymize data, and keep profiles, credentials, and private feedback out of contributions.
5. Directory changes need vendor documentation and updates to both compatibility guides. Do not claim untested product discovery is verified.

Run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Frontmatter deliberately uses single-line, double-quoted strings compatible with YAML and the dependency-free checker. More complex standard fields require parser/test updates.

For content changes, run [the behavioral scenarios](evals/README.en.md) in your agent. PRs should describe the problem, behavior change, checks, agent/version, and limitations. Preserve the MIT attribution.


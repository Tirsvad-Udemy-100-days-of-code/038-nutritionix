# RC-010: MIL-001 YAML review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [0c1627b] |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-YML-001] (`QC-YML-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | `yaml.safe_load` (PyYAML 6.0.3) parses every file in test_workflows.py; no duplicate key. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | Checked on ci.yml, english-comments.yml, publish-wiki.yml and .yamllint.yml. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `yamllint` 1.38.0 with the committed `.yamllint.yml` reports nothing; the two relaxed rules are explained in comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `on` is a key, not a value; versions are quoted where needed (`"3.13"`, `"true"`). |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | Checked on ci.yml, english-comments.yml, publish-wiki.yml and .yamllint.yml. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | Only `secrets.TOKEN_FOR_GITEA_WIKI` is named, never a value. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | The longest `run:` is one line. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | Checked on ci.yml, english-comments.yml, publish-wiki.yml and .yamllint.yml. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors, aliases or merge keys. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | N-A | Gitea Actions publishes no schema; test_workflows.py checks the required keys. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Checked on ci.yml, english-comments.yml, publish-wiki.yml and .yamllint.yml. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | Checked on ci.yml, english-comments.yml, publish-wiki.yml and .yamllint.yml. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | N-A | No multi-line string is used. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | Checked on ci.yml, english-comments.yml, publish-wiki.yml and .yamllint.yml. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | test_workflows.py checks the files offline. |

## Overall Verdict

Go — All Mandatory criteria of QC-YML-001 pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[MIL-001]: ../../milestones/mil-001-project-setup.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[0c1627b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/0c1627b24991d5659f04d5d128919b2db3d4f246

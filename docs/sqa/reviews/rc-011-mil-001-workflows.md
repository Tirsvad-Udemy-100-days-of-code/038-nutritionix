# RC-011: MIL-001 workflow review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-WF-001] (`QC-WF-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See RC-010. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | All files are in `.gitea/workflows/` with `.yml`; none in `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | Checked on ci.yml, english-comments.yml and publish-wiki.yml. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Checked on ci.yml, english-comments.yml and publish-wiki.yml. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Checked on ci.yml, english-comments.yml and publish-wiki.yml. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | No actionlint; the project's workflow validation test (test_workflows.py, pytest 9.1.1) runs on every pull request. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Every job declares `permissions`; write access only on the metrics job. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | Third-party actions use exact tags; the shared workflows of the same organisation use the moving major tag `@v2`. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | The wiki secret is passed as `secrets.TOKEN_FOR_GITEA_WIKI`; nothing is echoed. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No `${{ }}` of untrusted text in a `run:` script. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | No `pull_request_target` or `workflow_run` trigger. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | Wiki publishing runs only on a push to main and has no manual trigger. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | Optional; the shared workflows decide the token. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | Checked on ci.yml, english-comments.yml and publish-wiki.yml. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | Checked on ci.yml, english-comments.yml and publish-wiki.yml. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Checked on ci.yml, english-comments.yml and publish-wiki.yml. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Python tools are installed from `pyproject.toml` at pinned versions. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Optional; the install is fast. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | N-A | Optional; the shared workflows format their logs. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | No `run:` block above one line. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | The shared logic is the reusable workflows of TirSystem/github-action. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Run 2639 (ci.yml) and run 2640 (english-comments.yml) on pull request 27 of git.tirsystem.com, Gitea 1.27.3, passed all jobs; the metrics job was skipped as designed. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | Optional; the workflows are callers, not reusable workflows. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Pass | test_workflows.py runs in the tests job of every pull request. |

## Overall Verdict

Go — All Mandatory criteria of QC-WF-001 pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[MIL-001]: ../../milestones/mil-001-project-setup.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md

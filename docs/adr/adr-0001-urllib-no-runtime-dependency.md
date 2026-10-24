# Architecture Decision Record

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The lectures use the `requests` module. S02 compares code with the lectures. S03 asked for no runtime dependencies, and the brief says to avoid runtime dependencies unless they are needed. The two needs conflict.

Options evaluated:

1. Use `requests`, one runtime dependency. S02 can compare line by line, but S03 has to install a package.
2. Use only `urllib` from the standard library behind a small gateway port. No runtime dependency; the adapter is about thirty lines and the rest of the code does not see which client is used.

The brief for this project states S03's need as a requirement and names no need that only `requests` can meet, so option 2 is chosen.

## Decision

The project has no runtime dependency. HTTP calls use `urllib.request` inside one adapter of the infrastructure layer, behind the `HttpGateway` port of the application layer.

## Consequences

**Positive:**

- `pip install .` installs nothing else; S03 can run the project at once.
- The domain and application layers are tested with a fake gateway.

**Negative:**

- The adapter is longer than the `requests` lecture code; the README maps each lecture call to its function.
- A reader who wants `requests` must write a second adapter, which the port makes a small change.

## Affected Artifacts

- [BC-001] — the constraint "no runtime dependency" follows this decision.
- [SA-001] — the conflict between S02 and S03 is resolved here.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md

# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b64ad78] |

---

## Purpose

The analysis names the people who influence or use the Exercise Tracker and decides how closely each is involved. It uses the power/interest grid. The IDs below are the stable identifiers that every other document uses for owners, reviewers and RACI (responsible, accountable, consulted, informed).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment with work that is correct, reviewable and reusable |
| S02 | Udemy coursists | Participants of the 100 Days of Code course who share code and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | GitHub community | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews every document and accepts the plan. High power and high interest.
- **Keep Informed (S02):** cannot change the project, but uses the result and compares it with their own. High interest, low power.
- **Monitor (S03):** browses the repository and may use an idea. Low power and low interest; the repository description, topics and README are enough for them.

## Primary Concerns and FURPS+ Mapping

FURPS+ stands for functionality, usability, reliability, performance and supportability, plus design, implementation, interface and physical constraints.

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Correct calls to the Nutritionix and Sheety APIs, reviewable steps, reuse | Functionality, Supportability |
| S02 | Readable code, the assignment's function names, instructions that work | Usability, Functionality |
| S02 | Code that runs without hidden setup | Usability |
| S03 | Clear description, topics and README | Usability |
| S03 | No runtime dependencies | Implementation constraint (+) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat in the working session | At every plan and every end-of-run summary | Plan, review records, summary | All milestones |
| S02 | Repository README and wiki | At each merge to `main` | Run instructions, wiki pages in three languages | MIL-004 |
| S03 | Repository description, topics and README | Once, updated when scope changes | Description, topics, README | MIL-001, MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies, S02 compares with lecture code that uses `requests` | S02, S03 | S01 chose the standard library (ADR-0001, an Architecture Decision Record). The HTTP code is one small adapter, and the README maps each lecture step to a function |
| S02 wants the code to look like the lecture, S01 wants layered, tested code | S01, S02 | The assignment's steps keep their names in one readable module of the application layer, and the layers are explained in the wiki |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct calls, reviewable work | Objectives 1, 2 and 4 ([BC-001]) |
| S02 | Assignment's function names | Objectives 1 and 2 ([BC-001]) |
| S02 | Instructions that work | Objectives 5 and 7 ([BC-001]) |
| S03 | Description, topics, README | Objectives 8 and 7 ([BC-001]) |
| S03 | No runtime dependencies | Constraint on dependencies ([BC-001]) |

## Sign-Off

S01 accepts the analysis as Product Owner. In autonomous mode the review is recorded as AI as stand-in for S01.

---

[BC-001]: ./business-case.md
[b64ad78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/b64ad78da4e7a2bd6357aebc7435f940aabd3474

"""@file test_workflows.py
@brief Static checks of the CI workflow files in .gitea/workflows/.

The checks are offline: they parse each file and test the rules of the
workflow checklist that a parser can see (keys, permissions, runner, timeout,
pinned actions, no secret in the file).
"""

import re
from pathlib import Path
from typing import Any

import pytest
import yaml

WORKFLOW_DIR = Path(__file__).resolve().parents[2] / ".gitea" / "workflows"
WORKFLOWS = sorted(WORKFLOW_DIR.glob("*.yml"))

EXACT_TAG = re.compile(r"@v\d+\.\d+\.\d+$")
SHARED_MAJOR_TAG = re.compile(r"^TirSystem/github-action/.+@v\d+$")


# YAML has no schema here, so the parsed values are typed Any.
def _load(path: Path) -> dict[Any, Any]:
    """@brief Parse one workflow file with the safe YAML loader.

    @param path The workflow file.
    @return The parsed mapping.
    """
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(loaded, dict)
    return loaded


def _jobs(path: Path) -> dict[str, dict[str, Any]]:
    """@brief Return the jobs of a workflow file.

    @param path The workflow file.
    @return The mapping from job id to job.
    """
    jobs = _load(path)["jobs"]
    assert isinstance(jobs, dict)
    return jobs


def test_workflow_files_exist() -> None:
    assert WORKFLOWS, "no workflow file found"


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_workflow_has_name_trigger_and_jobs(path: Path) -> None:
    workflow = _load(path)
    # YAML 1.1 reads the key "on" as the boolean True.
    assert {"name", "jobs"} <= set(workflow)
    assert "on" in workflow or True in workflow


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_every_job_declares_permissions(path: Path) -> None:
    for job_id, job in _jobs(path).items():
        assert "permissions" in job, f"{path.name}: job {job_id} has no permissions"


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_every_own_job_has_runner_and_timeout(path: Path) -> None:
    for job_id, job in _jobs(path).items():
        if "uses" in job:
            continue
        assert "runs-on" in job, f"{path.name}: job {job_id} has no runs-on"
        assert "timeout-minutes" in job, f"{path.name}: job {job_id} has no timeout"


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_actions_are_pinned(path: Path) -> None:
    for job_id, job in _jobs(path).items():
        references = [job["uses"]] if "uses" in job else []
        references += [s["uses"] for s in job.get("steps", []) if "uses" in s]
        for reference in references:
            pinned = EXACT_TAG.search(reference) or SHARED_MAJOR_TAG.match(reference)
            assert pinned, f"{path.name}: {job_id} uses unpinned {reference}"


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_no_secret_value_or_tab_in_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    assert "\t" not in text
    for line in text.splitlines():
        if "secrets." in line:
            assert "${{" in line, f"{path.name}: secret is not read as an expression"

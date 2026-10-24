"""@file test_wiki.py
@brief Static checks of the wiki pages in docs/wiki/.

The checks are offline: they read the Markdown files and test that the three
languages have the same pages, the language line, the sidebar links, the
images and the code blocks of the Usage page.
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
WIKI_DIR = ROOT / "docs" / "wiki"
IMAGE_DIR = ROOT / "docs" / "images"

SIDEBAR = "_Sidebar"
LANGUAGE_SUFFIXES = ("-da", "-ms")
PAGES = sorted(
    path.stem
    for path in WIKI_DIR.glob("*.md")
    if path.stem != SIDEBAR and not path.stem.endswith(LANGUAGE_SUFFIXES)
)

ALL_PAGE_NAMES = [f"{p}{s}" for p in PAGES for s in ("", *LANGUAGE_SUFFIXES)]

IMAGE_URL = re.compile(r"/raw/branch/main/docs/images/([^)\s\"']+)")
CODE_BLOCK = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)


def _language_line(page: str, suffix: str) -> str:
    """@brief Build the expected first line of a page.

    @param page The English page name.
    @param suffix The language suffix: "", "-da" or "-ms".
    @return The language line with the current language in bold.
    """
    english = "**English**" if suffix == "" else f"[English]({page})"
    danish = "**Dansk**" if suffix == "-da" else f"[Dansk]({page}-da)"
    malay = "**Bahasa Malaysia**"
    if suffix != "-ms":
        malay = f"[Bahasa Malaysia]({page}-ms)"
    return f"{english} · {danish} · {malay}"


def _read(name: str) -> str:
    """@brief Read one wiki file.

    @param name The file name without the extension.
    @return The text of the file.
    """
    return (WIKI_DIR / f"{name}.md").read_text(encoding="utf-8")


def _code_blocks(name: str) -> list[str]:
    """@brief Return the fenced code blocks of a wiki file.

    @param name The file name without the extension.
    @return The blocks, in order, with their fences.
    """
    return CODE_BLOCK.findall(_read(name))


def test_wiki_has_pages() -> None:
    assert PAGES, "no English wiki page found"


@pytest.mark.parametrize("page", PAGES)
@pytest.mark.parametrize("suffix", LANGUAGE_SUFFIXES)
def test_page_has_twin_in_every_language(page: str, suffix: str) -> None:
    assert (WIKI_DIR / f"{page}{suffix}.md").is_file()


@pytest.mark.parametrize("page", PAGES)
@pytest.mark.parametrize("suffix", ("", *LANGUAGE_SUFFIXES))
def test_page_starts_with_language_line(page: str, suffix: str) -> None:
    first_line = _read(f"{page}{suffix}").splitlines()[0]
    assert first_line == _language_line(page, suffix)


@pytest.mark.parametrize("page", PAGES)
@pytest.mark.parametrize("suffix", ("", *LANGUAGE_SUFFIXES))
def test_sidebar_links_every_page_in_every_language(page: str, suffix: str) -> None:
    assert f"({page}{suffix})" in _read(SIDEBAR)


@pytest.mark.parametrize("name", ALL_PAGE_NAMES)
def test_repo_image_urls_refer_to_existing_files(name: str) -> None:
    for file_name in IMAGE_URL.findall(_read(name)):
        assert (IMAGE_DIR / file_name).is_file(), f"{name}: missing image {file_name}"


@pytest.mark.parametrize("suffix", LANGUAGE_SUFFIXES)
def test_usage_code_blocks_are_identical_in_every_language(suffix: str) -> None:
    english = _code_blocks("Usage")
    assert english, "the Usage page has no code block"
    assert _code_blocks(f"Usage{suffix}") == english

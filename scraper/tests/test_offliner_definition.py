"""Regression checks for Zimfarm recipe options."""

import json
from pathlib import Path

DEFINITION_PATH = Path(__file__).parents[2] / "offliner-definition.json"


def test_recipe_defines_supported_sources_and_source_specific_filters():
    definition = json.loads(DEFINITION_PATH.read_text(encoding="utf-8"))
    flags = definition["flags"]

    assert flags["source"] == {
        "type": "string-enum",
        "required": False,
        "title": "Source",
        "description": (
            "Book source to scrape. Source-specific options are shown below; do not "
            "combine options from different sources."
        ),
        "choices": [
            {"title": "Project Gutenberg", "value": "gutenberg"},
            {"title": "Open Textbook Library", "value": "opentextbooks"},
        ],
    }
    assert {"lcc_shelves", "subjects", "otl_ids"}.issubset(flags)


def test_recipe_uses_enum_choices_for_supported_formats():
    definition = json.loads(DEFINITION_PATH.read_text(encoding="utf-8"))

    assert definition["flags"]["formats"]["type"] == "list-of-string-enum"
    assert [
        choice["value"] for choice in definition["flags"]["formats"]["choices"]
    ] == ["epub", "html", "pdf"]

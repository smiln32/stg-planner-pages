"""Hold the Studio stylesheet to the colour tokens in _config/design-system.md.

The design system is the authority for how Topical Study Studio looks (CONTEXT.md, "Change the
Studio"). These checks fail when the stylesheet uses a colour the token table does not
name, or when a token is named that nothing in the Studio uses. The page preview inside the
editor copies the page engine's own colours, which are owned by study_factory.py, so those
are allowed too.
"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import study_factory  # noqa: E402

HEX = re.compile(r"#[0-9a-fA-F]{3,6}\b")


def normalise(value):
    value = value.lower()
    if len(value) == 4:
        value = "#" + "".join(ch * 2 for ch in value[1:])
    return value


def hexes(text):
    return {normalise(m) for m in HEX.findall(text)}


def read(*parts):
    return (ROOT.joinpath(*parts)).read_text(encoding="utf-8")


def colour_tokens():
    front = read("_config", "design-system.md").split("---")[1]
    block = front.split("colors:")[1].split("typography:")[0]
    return {m.group(1): normalise(m.group(2)) for m in re.finditer(r'^\s+([a-z-]+): "(#[0-9a-fA-F]{6})"', block, re.M)}


class DesignTokenTests(unittest.TestCase):
    def setUp(self):
        self.tokens = colour_tokens()
        self.styles = read("studio", "styles.css")
        self.studio = self.styles + read("studio", "index.html") + read("studio", "app.js")

    def test_token_table_is_present_and_well_formed(self):
        self.assertGreaterEqual(len(self.tokens), 14)
        for name in ("ink", "canvas", "surface", "border", "rule", "focus", "sage", "slate"):
            self.assertIn(name, self.tokens)

    def test_every_colour_token_is_used_by_the_studio(self):
        used = hexes(self.studio)
        unused = sorted(name for name, value in self.tokens.items() if value not in used)
        self.assertEqual(unused, [], f"tokens nothing in studio/ uses: {unused}")

    def test_stylesheet_uses_only_tokens_and_page_engine_colours(self):
        allowed = set(self.tokens.values()) | hexes(study_factory.CSS)
        stray = sorted(hexes(self.styles) - allowed)
        self.assertEqual(stray, [], f"colours in styles.css that are neither tokens nor page-engine colours: {stray}")


if __name__ == "__main__":
    unittest.main()

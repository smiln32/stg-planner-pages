"""The ICM structure, held by a test.

A stage that loses its contract, a contract that names a file which is not there, or a
router that stops naming a stage fails here. See records/icm-audit.md for the walk.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGES = ROOT / "stages"
EXPECTED = ["01_brief", "02_pages", "03_spec", "04_check", "05_export"]
REQUIRED_SECTIONS = ("## Inputs", "## Process", "## Outputs", "## Human gate")
PATH_TOKEN = re.compile(r"`([A-Za-z0-9_./-]+(?:\.(?:md|json|txt|py|html)|/))`")


def stage_dirs():
    return sorted(p for p in STAGES.iterdir() if p.is_dir())


class StructureTests(unittest.TestCase):
    def test_root_layers_exist(self):
        for name in ("CLAUDE.md", "CONTEXT.md", "DECISIONS.md", "HANDOFF.md", "shared/CONTEXT.md"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_stages_are_numbered_without_gaps(self):
        names = [p.name for p in stage_dirs()]
        self.assertEqual(names, EXPECTED)
        for n, name in enumerate(names, 1):
            self.assertRegex(name, r"^\d{2}_[a-z]+$")
            self.assertEqual(int(name[:2]), n)

    def test_each_stage_has_contract_references_and_output(self):
        for stage in stage_dirs():
            with self.subTest(stage=stage.name):
                contract = stage / "CONTEXT.md"
                self.assertTrue(contract.is_file())
                text = contract.read_text(encoding="utf-8")
                for section in REQUIRED_SECTIONS:
                    self.assertIn(section, text)
                self.assertLessEqual(len(text.splitlines()), 80, "contract over 80 lines")
                references = [p for p in (stage / "references").iterdir() if p.is_file()]
                self.assertTrue(references, "references/ is empty")
                self.assertTrue((stage / "output" / ".gitkeep").is_file())

    def test_every_path_a_contract_names_exists(self):
        for stage in stage_dirs():
            text = (stage / "CONTEXT.md").read_text(encoding="utf-8")
            for token in PATH_TOKEN.findall(text):
                if "<" in token or token.startswith("output/"):
                    continue
                with self.subTest(stage=stage.name, path=token):
                    candidates = (stage / token, ROOT / token)
                    self.assertTrue(any(c.exists() for c in candidates), token)

    def test_contracts_chain_forward_only(self):
        names = [p.name for p in stage_dirs()]
        for i, stage in enumerate(stage_dirs()):
            text = (stage / "CONTEXT.md").read_text(encoding="utf-8")
            for later in names[i + 1:]:
                self.assertNotIn(f"../{later}/output", text, f"{stage.name} reads a later stage")
            if i + 1 < len(names):
                self.assertIn(f"../{names[i + 1]}/CONTEXT.md", text, "missing Next pointer")

    def test_router_names_every_stage(self):
        router = (ROOT / "CONTEXT.md").read_text(encoding="utf-8")
        for name in EXPECTED:
            self.assertIn(f"stages/{name}", router)

    def test_shared_router_names_only_real_files(self):
        text = (ROOT / "shared" / "CONTEXT.md").read_text(encoding="utf-8")
        for token in PATH_TOKEN.findall(text):
            with self.subTest(path=token):
                self.assertTrue((ROOT / "shared" / token).exists() or (ROOT / token).exists(), token)


if __name__ == "__main__":
    unittest.main()

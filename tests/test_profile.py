import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = ROOT / "assets"

EXPECTED_ASSETS = {
    "assets/banner-dark.svg",
    "assets/banner-light.svg",
    "assets/captain-mark.svg",
    "assets/card-arcpredict.svg",
    "assets/card-captain-dock.svg",
    "assets/card-llm-template.svg",
    "assets/card-predictarena.svg",
    "assets/card-web-demo.svg",
}

REQUIRED_README_TEXT = [
    "CAPTAIN // FANGTIGER",
    "AI × WEB3 BUILDER",
    "Building intelligent agents, prediction systems and developer infrastructure.",
    "CURRENT MISSION",
    "Winner, Binance AI Competition",
    "Arc Builder",
    "Hong Kong",
    "https://www.captain-dock.xyz/",
    "FRONTEND WEBSITE",
    "web_demo",
    "Large Model Template",
    "Agent prompt, tool-call and workflow templates for reusable AI systems.",
    "https://www.linkedin.com/in/lao-shugen-0aa058349/",
    "https://x.com/mycndota",
]

REQUIRED_REPOSITORIES = {
    "ArcPredict": "https://github.com/fangTiger/ArcPredict",
    "captain-dock": "https://github.com/fangTiger/captain-dock",
    "PredictArena": "https://github.com/fangTiger/PredictArena",
    "web_demo": "https://github.com/fangTiger/web_demo",
    "Large Model Template": "#large-model-template",
}

FORBIDDEN_README_TOKENS = [
    "github-readme-stats",
    "shields.io",
    "komarev",
    "visitor",
    "snake",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def local_asset_references(markdown: str) -> set[str]:
    html_refs = re.findall(r"""(?:src|srcset|href)=["']([^"']+)["']""", markdown)
    image_refs = re.findall(r"""!\[[^\]]*]\((assets/[^)\s]+)""", markdown)
    return {
        ref.split()[0]
        for ref in [*html_refs, *image_refs]
        if ref.startswith("assets/")
    }


class ProfileReadmeTest(unittest.TestCase):
    def test_readme_includes_brand_identity_and_repository_links(self):
        self.assertTrue(README.exists(), "README.md should exist")
        markdown = read_text(README)

        for text in REQUIRED_README_TEXT:
            self.assertIn(text, markdown)

        for label, url in REQUIRED_REPOSITORIES.items():
            self.assertIn(label, markdown)
            self.assertIn(url, markdown)

        self.assertIn("assets/banner-dark.svg", markdown)
        self.assertIn("assets/banner-light.svg", markdown)
        self.assertIn("Personal command deck for AI × Web3 projects.", markdown)
        self.assertIn("assets/card-web-demo.svg", markdown)
        self.assertIn("assets/card-llm-template.svg", markdown)

    def test_readme_uses_local_assets_without_dynamic_badges(self):
        self.assertTrue(README.exists(), "README.md should exist")
        markdown = read_text(README)
        refs = local_asset_references(markdown)

        self.assertEqual(EXPECTED_ASSETS, refs)
        for ref in refs:
            self.assertTrue((ROOT / ref).exists(), f"{ref} should exist")

        lowered = markdown.lower()
        for token in FORBIDDEN_README_TOKENS:
            self.assertNotIn(token, lowered)

    def test_svg_assets_are_accessible_static_and_described(self):
        for relative in EXPECTED_ASSETS:
            path = ROOT / relative
            self.assertTrue(path.exists(), f"{relative} should exist")
            tree = ET.parse(path)
            root = tree.getroot()
            tag_names = {element.tag.split("}")[-1] for element in root.iter()}

            self.assertEqual("svg", root.tag.split("}")[-1])
            self.assertTrue(root.attrib.get("viewBox"), f"{relative} needs a viewBox")
            self.assertIn("title", tag_names, f"{relative} needs a title")
            self.assertIn("desc", tag_names, f"{relative} needs a desc")
            self.assertNotIn("script", tag_names, f"{relative} must not use scripts")
            self.assertNotIn("foreignObject", tag_names, f"{relative} must not use foreignObject")

            for element in root.iter():
                for name, value in element.attrib.items():
                    local_name = name.split("}")[-1].lower()
                    if local_name in {"href", "src"}:
                        self.assertFalse(
                            value.startswith(("http://", "https://", "//")),
                            f"{relative} must not reference remote resources",
                        )

    def test_visual_assets_include_required_palette(self):
        combined = "\n".join(read_text(ROOT / relative) for relative in EXPECTED_ASSETS)
        self.assertIn("#66E3FF", combined)
        self.assertIn("#FF7A18", combined)
        self.assertIn("#0B0F14", combined)
        self.assertNotRegex(combined.lower(), r"purple|violet|#8b5cf6|#a855f7")


if __name__ == "__main__":
    unittest.main()

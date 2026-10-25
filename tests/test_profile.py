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
    "assets/card-arc-dungeon.svg",
    "assets/card-llm-template.svg",
    "assets/card-predictarena.svg",
    "assets/card-web-demo.svg",
    "assets/card-yarrow.svg",
    "assets/card-bounty-dungeon.svg",
    "assets/card-mars-roadster.svg",
}

REQUIRED_README_TEXT = [
    "CAPTAIN // FANGTIGER",
    "AI × WEB3 BUILDER",
    "构建智能体、链上预测产品与可复用的 AI 开发工作流。",
    "精选作品",
    "新作 · Mars Roadster",
    "https://mars-roadster.vercel.app/",
    "推进器升空",
    "空中翻滚",
    "轨道再入",
    "Binance AI 竞赛获奖",
    "Arc Builder",
    "香港",
    "https://www.captain-dock.xyz/",
    "web_demo",
    "ai-config-templates",
    "https://www.linkedin.com/in/lao-shugen-0aa058349/",
    "https://x.com/mycndota",
]

REQUIRED_REPOSITORIES = {
    "ARC Dungeon": "https://github.com/fangTiger/Arc-Dungeon",
    "ArcPredict": "https://github.com/fangTiger/ArcPredict",
    "PredictArena": "https://github.com/fangTiger/PredictArena",
    "web_demo": "https://github.com/fangTiger/web_demo",
    "ai-config-templates": "https://github.com/fangTiger/ai-config-templates",
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
    def test_mars_roadster_is_first_work_without_network_label(self):
        markdown = read_text(README)
        first_card = re.search(r'<img[^>]+src="(assets/card-[^"]+)"', markdown)
        self.assertIsNotNone(first_card)
        self.assertEqual("assets/card-mars-roadster.svg", first_card.group(1))
        section = markdown.split("### 最新作品", 1)[1].split("### 近期上线 · Arc 主网", 1)[0]
        self.assertRegex(section, r'<a href="https://mars-roadster\.vercel\.app/">\s*<img[^>]+src="assets/card-mars-roadster\.svg"')
        self.assertIn("实时 3D", section)
        self.assertNotRegex(section, r"主网|测试网|USDC|Mainnet|Testnet")
        root = ET.parse(ASSETS / "card-mars-roadster.svg").getroot()
        text = " ".join(root.itertext())
        self.assertIn("Mars Roadster", text)
        self.assertNotRegex(text, r"主网|测试网|USDC|Mainnet|Testnet")

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
        self.assertIn("assets/card-web-demo.svg", markdown)
        self.assertIn("assets/card-llm-template.svg", markdown)

    def test_project_cards_link_to_public_repositories(self):
        markdown = read_text(README)
        expected_cards = {
            "card-arc-dungeon.svg": "ARC Dungeon",
            "card-arcpredict.svg": "ArcPredict",
            "card-predictarena.svg": "PredictArena",
            "card-web-demo.svg": "web_demo",
            "card-llm-template.svg": "ai-config-templates",
        }
        for card, project in expected_cards.items():
            with self.subTest(project=project):
                self.assertRegex(
                    markdown,
                    rf'<a href="{re.escape(REQUIRED_REPOSITORIES[project])}">\s*'
                    rf'<img[^>]+src="assets/{re.escape(card)}"',
                )
        self.assertNotIn("https://github.com/fangTiger/captain-dock", markdown)
        self.assertIn('<a id="large-model-template"></a>', markdown)

    def test_recent_mainnet_showcase_precedes_existing_featured_projects(self):
        markdown = read_text(README)
        heading = "### 近期上线 · Arc 主网"
        self.assertIn(heading, markdown)
        recent = markdown.split(heading, 1)[1].split("### 精选作品", 1)[0]
        self.assertLess(markdown.index(heading), markdown.index("### 精选作品"))
        self.assertIn("Arc 主网已上线", recent)
        cards = re.findall(r'<p align="center">(.*?)</p>', recent, re.S)
        self.assertEqual(1, len(cards))
        for repository, asset, demo in (
            ("yarrow", "card-yarrow.svg", "https://yarrow-six.vercel.app"),
            ("bounty-dungeon", "card-bounty-dungeon.svg", "https://bounty-dungeon.vercel.app"),
        ):
            with self.subTest(repository=repository):
                self.assertRegex(
                    cards[0],
                    rf'<a href="https://github.com/fangTiger/{repository}">\s*'
                    rf'<img[^>]+src="assets/{asset}"[^>]+width="48%"\s*>\s*</a>',
                )
                self.assertIn(demo, recent)
                root = ET.parse(ASSETS / asset).getroot()
                self.assertEqual("0 0 760 300", root.attrib.get("viewBox"))
                for tag in ("title", "desc"):
                    element = root.find(f"{{http://www.w3.org/2000/svg}}{tag}")
                    self.assertIsNotNone(element)
                    self.assertRegex(element.text or "", r"[\u4e00-\u9fff]")
        self.assertIn("Yarrow · 三易", recent)
        self.assertIn("Bounty Dungeon", recent)
        for term in ("三流派", "USDC", "区块哈希", "复算", "24 小时", "首位超分者", "服务器重放验证", "合约托管"):
            self.assertIn(term, recent)
        legacy_row = next(line for line in markdown.splitlines() if line.startswith("| [ARC Dungeon]"))
        self.assertIn("https://github.com/fangTiger/Arc-Dungeon", legacy_row)
        self.assertIn("Arc 测试网游戏原型", legacy_row)

    def test_project_summaries_explain_capabilities_and_stage(self):
        markdown = read_text(README)
        rows = {
            project: next(
                (line for line in markdown.splitlines() if line.startswith(f"| [{project}]")),
                "",
            )
            for project in REQUIRED_REPOSITORIES
        }
        for project, terms in {
            "ARC Dungeon": ("像素地牢", "职业战斗", "钱包", "战绩", "本地模拟", "Arc 测试网游戏原型", "真实钱包发布待验证", "代码待上传"),
            "ArcPredict": ("AI Lens", "测试网原型"),
            "PredictArena": ("智能体对决", "测试网演示"),
            "web_demo": ("静态前端模板", "目录"),
            "ai-config-templates": ("OpenSpec", "编码工作流"),
        }.items():
            for term in terms:
                with self.subTest(project=project, term=term):
                    self.assertIn(term, rows[project])

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
        for path in ASSETS.glob("*.svg"):
            relative = str(path.relative_to(ROOT))
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

    def test_new_card_has_chinese_accessible_description(self):
        for filename in ("card-giwa-intent.svg", "card-arc-dungeon.svg"):
            with self.subTest(card=filename):
                path = ASSETS / filename
                self.assertTrue(path.exists(), f"缺少卡片：{filename}")
                root = ET.parse(path).getroot()
                for tag in ("title", "desc"):
                    element = root.find(f"{{http://www.w3.org/2000/svg}}{tag}")
                    self.assertIsNotNone(element)
                    self.assertRegex(element.text or "", r"[\u4e00-\u9fff]")

    def test_readme_omits_giwa_showcase(self):
        markdown = read_text(README)
        self.assertNotIn("giwa", markdown.lower())
        self.assertNotIn("链上付款请求", markdown)

    def test_project_cards_form_rows_of_three_and_two(self):
        groups = re.findall(r'<div align="center">(.*?)</div>', read_text(README), re.S)
        rows = [group for group in groups if 'src="assets/card-' in group]
        self.assertEqual(2, len(rows))
        for row, count in zip(rows, (3, 2)):
            cards = re.findall(r'<img[^>]+src="assets/card-[^"]+"[^>]+width="([^"]+)"', row)
            self.assertEqual(["31%"] * count, cards)

    def test_visual_assets_include_required_palette(self):
        for relative in EXPECTED_ASSETS:
            self.assertTrue((ROOT / relative).exists(), f"缺少本地资产：{relative}")
        combined = "\n".join(read_text(ROOT / relative) for relative in EXPECTED_ASSETS)
        self.assertIn("#66E3FF", combined)
        self.assertIn("#FF7A18", combined)
        self.assertIn("#0B0F14", combined)
        self.assertNotRegex(combined.lower(), r"purple|violet|#8b5cf6|#a855f7")


if __name__ == "__main__":
    unittest.main()

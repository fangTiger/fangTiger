## Why

用户希望保留 Captain 风格，让 GitHub 首页突出近期 AI × Web3 成果。现有项目描述偏抽象，模板入口只指向本页锚点，且核心卡片包含已核实为空的 captain-dock 仓库。

## What Changes

- 保留横幅、标志和青色／橙色配色，用中文介绍作品方向。
- 用 GiwaIntent 替换空仓库的核心卡片，更新 ArcPredict、PredictArena 的具体能力与测试网状态。
- 将模板卡片与文字入口直接链接到 ai-config-templates，准确描述 OpenSpec 与 AI 编码工作流。
- 将 web_demo 描述更新为静态前端模板库，保留网站和社交联系入口。
- 更新现有回归测试，校验链接、状态及本地 SVG 可访问性。

## Capabilities

### New Capabilities

- `profile-portfolio`: 定义以已核实公开项目为依据的个人作品集展示及静态资产要求。

### Modified Capabilities

无。当前 openspec/specs 尚无已归档规范；此前展示变更保留为历史记录。

## Impact

涉及 README.md、五张展示卡片及 tests/test_profile.py；新增 GiwaIntent 卡片。没有运行时依赖或公共 API 变更。个人网站保留原链接，网站可用性尚未核实。本次先完成本地可审阅版本。

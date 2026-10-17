# 个人作品集首页更新实施计划

> 使用 TDD 和 verification-before-completion 技能逐项执行；由当前 Codex 独立完成。

**Goal:** 保留 Captain 风格，准确展示近期 AI × Web3 公开作品。

**Architecture:** README 使用本地 SVG 卡片与项目表格。卡片直接链接公开仓库，表格提供能力与阶段，联系方式保留既有内容。

**Tech Stack:** Markdown、静态 SVG、Python unittest、OpenSpec。

### 任务 1：先更新回归断言

文件：tests/test_profile.py。

1. 用五个真实仓库替换过期模板锚点及空仓库入口，断言卡片点击目标正确。
2. 断言测试网阶段、中文能力说明以及兼容模板锚点。
3. SVG 检查覆盖所有卡片，引用集合使用新的 GiwaIntent 卡片。
4. 运行 `python3 -m unittest discover -s tests -v`，确认因 GiwaIntent 卡片、具体能力与仓库链接尚未实现而失败。

### 任务 2：更新作品展示

文件：README.md、assets/card-giwa-intent.svg、assets/card-arcpredict.svg、assets/card-predictarena.svg、assets/card-web-demo.svg、assets/card-llm-template.svg。

1. 第一排 ArcPredict、GiwaIntent、PredictArena；第二排 web_demo、ai-config-templates。
2. 用中文描述作品，补充阶段和链接，保留旧模板锚点。
3. 使用已核实 README 中的能力描述，不声称生产上线；联系方式和品牌资产保留。
4. 复用现有卡片图形与配色，提供中文字体回退、标题和无障碍说明。

### 任务 3：验证与交付

1. 运行完整 unittest，期望零失败；运行 `git diff --check`，期望退出码 0。
2. 运行 `openspec validate refresh-profile-portfolio --strict`，期望校验通过。
3. 检查卡片布局与 README 预览，并让 tasks.md 状态与实际结果一致。
4. 打开本地 README 供用户审阅，说明远程发布状态。

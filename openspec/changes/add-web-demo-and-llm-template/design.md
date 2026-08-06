## Context

当前仓库是一个 GitHub profile 展示项目，核心产物是 `README.md` 和 `assets/` 下的静态 SVG。现有测试已经约束 README 必须使用本地资产、避免动态徽章和远程资源，并验证主要品牌文案与项目链接。

本次需求是把前端网站、`web_demo` 项目和大模型模板补进展示内容。为了保持 profile 渲染稳定，新增内容应延续现有静态 HTML/Markdown + SVG 卡片方式。

## Goals / Non-Goals

**Goals:**
- 在 README 中明确展示前端网站、`web_demo` 项目和大模型模板。
- 新增本地 SVG 卡片资产，保证 GitHub README 不依赖远程图片、脚本或构建流程。
- 扩展测试覆盖新增文案、链接和资产集合。

**Non-Goals:**
- 不搭建新的前端应用或构建系统。
- 不引入 npm、Python 或远程渲染依赖。
- 不修改现有三张项目卡片的语义。

## Decisions

1. 使用 README 静态展示，而不是新增站点目录。
   - 原因：当前仓库定位是 profile 展示，测试也围绕 README 资产完整性展开。
   - 备选：创建独立 `web_demo/` 应用目录。该方案会引入构建、部署和测试复杂度，超出当前请求的展示目的。

2. 为 `web_demo` 和大模型模板新增 SVG 卡片。
   - 原因：保持与 ArcPredict、captain-dock、PredictArena 一致的视觉入口，且可被现有 SVG 静态检查复用。
   - 备选：只加文字链接。该方案可用但视觉层级低，不能体现“也加进来”的同等展示意图。

3. 用测试锁定新增展示项。
   - 原因：现有项目已经采用测试保护 README 内容和资产引用；新增行为应先通过失败测试表达，再实现。
   - 备选：手动检查 README。该方案缺少回归保护。

## Risks / Trade-offs

- 链接目标可能与实际远程仓库名称不一致 → 使用与现有 GitHub 链接一致的 `https://github.com/fangTiger/web_demo`，大模型模板使用可读锚点入口，后续若有独立仓库可替换。
- SVG 卡片数量增加会让 README 首屏更密 → 第二组展示采用两张卡片并控制宽度，避免挤压现有三项目卡片。

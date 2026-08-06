## Why

当前 README 已经展示 AI x Web3 身份和三个核心项目，但还没有把前端网站、`web_demo` 项目与大模型模板作为同等入口呈现。补齐这些入口可以让访客更快理解项目组合：既有智能体与预测系统，也有可直接查看的前端作品和可复用的大模型模板。

## What Changes

- 在 README 中新增前端网站与 `web_demo` 项目的展示入口。
- 在 README 中新增大模型模板的展示入口，说明其面向智能体、提示词和工作流复用。
- 增加对应的本地 SVG 卡片资产，保持当前 profile 的静态、无远程依赖展示风格。
- 扩展现有测试，锁定新增 README 文案、链接和资产引用。

## Capabilities

### New Capabilities
- `profile-showcase`: 定义 profile README 展示项目、网站和模板入口时应满足的内容、链接和静态资产要求。

### Modified Capabilities

无。

## Impact

- 影响 `README.md`、`assets/` 下的 SVG 卡片资源、`tests/test_profile.py`。
- 不新增运行时依赖，不改变公共 API，不影响现有 GitHub profile 的静态渲染方式。

## 1. 回归保护

- [x] 1.1 扩展仓库、卡片、能力、阶段及两排三列布局测试
- [x] 1.2 运行 unittest，确认新增要求因展示缺失而失败

## 2. 主页更新

- [x] 2.1 更新 README 简介、游戏入口、表格文案及布局
- [x] 2.2 新增游戏 SVG 卡片，保留青橙配色和中文无障碍描述

## 3. 验证交付

- [x] 3.1 运行完整 unittest、OpenSpec 严格校验及 diff 检查
- [x] 3.2 检查卡片渲染，核对规范与任务状态，打开 README 供审阅

验证记录：新增断言首次运行产生 14 个预期失败，无测试异常；实现后 `python3 -m unittest discover -s tests -v` 的 8 项测试全部通过。`openspec validate add-arc-dungeon-showcase --strict` 和 `git diff --check` 通过。Quick Look 已渲染新 SVG，中文、标题及像素拱门显示完整且无重叠。README 已请求在 Codex 打开。规范三个需求及场景与实现一致；游戏仓库查询时仍为空，未添加试玩地址。本次未提交或推送。

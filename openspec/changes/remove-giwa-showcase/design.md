## Context

首页为 README 与本地 SVG，现有测试要求六张卡片并强制展示 GIWA。

## Goals / Non-Goals

目标是删除 GIWA 展示并保持其他五个项目、品牌和联系入口。历史图片和历史变更记录不清理。

## Decisions

第一排放 ArcPredict、PredictArena、ARC Dungeon，第二排放两个模板项目，统一保留 31% 宽度，避免首排空缺。只隐藏链接会保留不再需要的介绍，因此卡片、表格行和总览文案同步删除。

## Risks / Trade-offs

旧测试固定要求六张卡片 → 先修改断言并观察预期失败，再修改 README。

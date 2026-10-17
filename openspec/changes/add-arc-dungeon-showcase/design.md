## Context

主页已有五个作品及本地 SVG 卡片。新游戏位于相邻工作区 rialo-rpg/arc-rpg，名称为 ARC Dungeon；本地 origin 为尚不存在的 arc-rpg 地址，而 GitHub 已创建公开 Arc-Dungeon 仓库且内容查询返回空仓库。

## Goals / Non-Goals

**Goals:** 沿用 Captain 配色展示游戏的可核实玩法、钱包及战绩功能，保留五个已有作品。

**Non-Goals:** 修改游戏、上传游戏代码、部署网站、调整主页获奖或联系方式。

## Decisions

1. 第一排保留 ArcPredict、GiwaIntent、PredictArena，第二排放 ARC Dungeon、web_demo、ai-config-templates，统一为 31% 宽度。替换已有项目会丢失作品；独立第三排增加页面长度；两排三张符合现有结构。
2. 使用已有 SVG 卡片结构，绘制像素拱门、地砖和星点，继承深色背景及青橙配色。无需引入截图或远程图片依赖。
3. 以本地 README 与验证记录描述能力，仓库入口使用 GitHub 已证实存在的 Arc-Dungeon；表格说明代码待上传、真实钱包发布待验证，避免将模拟钱包结果写成公开链成功。
4. 扩展现有测试的仓库、卡片及能力断言；中文无障碍断言同时覆盖游戏卡片与 GiwaIntent。

## Risks / Trade-offs

- 仓库尚无代码 → 当前明确标注代码待上传；上传后可删去该说明。
- 尚无试玩网址 → 仅提供仓库入口，不推测 Vercel 域名。
- 小尺寸中文可能过密 → 卡片仅展示两行核心能力，阶段及限制在表格说明，并进行渲染检查。

## Migration Plan

先增加回归断言并确认失败，再更新 README 和 SVG，运行 unittest、OpenSpec 严格校验及 diff 检查，检查卡片排版。本次不发布。

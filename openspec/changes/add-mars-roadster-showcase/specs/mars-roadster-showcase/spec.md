## ADDED Requirements

### Requirement: 新作直接试玩入口

首页 SHALL 在 Arc 主网作品区之前展示 Mars Roadster 独立新作区，卡片与文字试玩入口 MUST 指向 https://mars-roadster.vercel.app/。介绍 SHALL 包含沙漠公路、推进器升空、空中翻滚及轨道再入，且不把该游戏描述为 Arc 主网产品。

#### Scenario: 访客发现新游戏
- **WHEN** 访客查看品牌介绍后的作品内容
- **THEN** 首先看到 Mars Roadster 新作卡片，可点击卡片或文字进入试玩
- **THEN** 现有 Arc 主网作品、精选项目和联系方式继续展示，GIWA 仍不展示

### Requirement: 游戏主题静态卡片

新作卡片 MUST 使用本地 assets/card-mars-roadster.svg，viewBox 为 0 0 1200 360；包含中文 title 和 desc，以跑车、公路及太空轨道传达主题。SVG MUST 不含脚本、foreignObject 或外部资源。

#### Scenario: 首页加载新作卡片
- **WHEN** 检查资源与渲染效果
- **THEN** 标题、中文说明、试玩提示清晰，图文无重叠，卡片使用现有深色品牌配色

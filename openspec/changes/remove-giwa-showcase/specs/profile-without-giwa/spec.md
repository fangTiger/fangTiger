## ADDED Requirements

### Requirement: 首页移除 GIWA 展示

首页 MUST 不含 GiwaIntent、GIWA 仓库或卡片引用及“链上付款请求”介绍。首页 SHALL 保留 ArcPredict、PredictArena、ARC Dungeon、web_demo 和 ai-config-templates 的卡片及项目说明，保留品牌、网站和联系方式。

#### Scenario: 浏览精简作品
- **WHEN** 访客查看首页
- **THEN** 五个项目均有卡片和表格说明，GIWA 名称、链接及付款请求介绍均不可见
- **THEN** 品牌、网站及联系方式仍可访问

### Requirement: 五张卡片布局

首页 SHALL 第一排展示 ArcPredict、PredictArena、ARC Dungeon，第二排展示 web_demo、ai-config-templates；各卡片宽度 MUST 为 31%，图片 MUST 使用现有本地 SVG。

#### Scenario: 检查作品排布
- **WHEN** 检查首页卡片分组
- **THEN** 两排卡片数分别为三张和两张，链接与图片均有效

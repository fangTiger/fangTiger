## ADDED Requirements

### Requirement: 公开作品与直接入口

首页 SHALL 展示 ArcPredict、GiwaIntent、PredictArena、web_demo、ai-config-templates，且各项目卡片和项目说明 MUST 链接其真实公开仓库。首页 SHALL 保留个人网站及社交联系方式；空 captain-dock 仓库 MUST 不作为核心作品入口。

#### Scenario: 浏览作品
- **WHEN** 访客查看首页
- **THEN** 五个项目均有卡片和文字介绍，且链接到对应公开仓库
- **THEN** 网站入口仍为 https://www.captain-dock.xyz/，核心作品不链接空 captain-dock 仓库

#### Scenario: 兼容模板锚点
- **WHEN** 访客访问 #large-model-template
- **THEN** 页面保留该锚点，并提供 ai-config-templates 仓库入口

### Requirement: 具体能力与真实阶段

首页 SHALL 用中文介绍具体能力，标明 ArcPredict 的测试网原型、PredictArena 的测试网演示、GiwaIntent 的测试网 MVP，并展示 web_demo 的静态模板库与 ai-config-templates 的 OpenSpec 编码工作流定位。

#### Scenario: 理解项目成熟度
- **WHEN** 访客阅读作品表格
- **THEN** 三个链上项目的测试网阶段可见，GiwaIntent 说明部署于 GIWA Sepolia
- **THEN** ArcPredict 说明 AI Lens 概率参考，PredictArena 说明智能体对决，模板项目说明真实用途

### Requirement: 保留静态品牌资产

首页 MUST 保留 CAPTAIN // FANGTIGER、AI × WEB3 BUILDER、深浅色横幅及品牌标志，并使用青色和橙色本地 SVG 卡片。所有 SVG MUST 有 viewBox、title、desc，不含 script、foreignObject 或远程资源引用。新卡片 SHALL 用中文提供无障碍说明。

#### Scenario: 加载视觉资产
- **WHEN** 检查首页资产引用
- **THEN** 所有引用都解析为存在的本地 SVG，并包含 GiwaIntent 卡片
- **THEN** 新卡片有中文 title 和 desc，静态安全检查通过

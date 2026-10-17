## ADDED Requirements

### Requirement: 游戏入口及布局

主页 SHALL 在保留已有五个作品的基础上增加 ARC Dungeon 卡片与文字介绍，均链接 https://github.com/fangTiger/Arc-Dungeon。主页 SHALL 使用两排三张等宽卡片，保留所有品牌和联系入口。

#### Scenario: 浏览新游戏
- **WHEN** 访客查看精选作品
- **THEN** 六个项目均有卡片和表格说明，ARC Dungeon 入口指向已存在的公开仓库
- **THEN** 两排各有三张 31% 宽度卡片

### Requirement: 准确表达游戏能力和阶段

主页 SHALL 描述像素地牢、职业战斗、钱包连接及 Arc 测试网战绩发布。主页 MUST 明确奖励、门票与皮肤为本地模拟资产，真实钱包发布待验证及仓库代码待上传；未核实的试玩地址 MUST 不展示。

#### Scenario: 理解游戏成熟度
- **WHEN** 访客阅读 ARC Dungeon 项目说明
- **THEN** 可区分游戏玩法、测试网战绩与本地模拟资产
- **THEN** 阶段为 Arc 测试网游戏原型，包含当前验证和仓库内容边界

### Requirement: 游戏卡片静态资产

游戏卡片 MUST 使用本地 assets/card-arc-dungeon.svg，包含 viewBox、中文 title 和 desc，并沿用青色、橙色及深色背景。卡片 MUST 不含脚本、foreignObject 或远程资源。

#### Scenario: 加载新卡片
- **WHEN** 检查主页引用与游戏 SVG
- **THEN** 资源存在，中文无障碍描述完整，静态安全检查通过

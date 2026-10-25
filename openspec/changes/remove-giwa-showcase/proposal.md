## Why

用户不再需要在首页展示 GIWA 项目，需删除对应入口和介绍。

## What Changes

- 移除 GiwaIntent 卡片、表格行及“链上付款请求”介绍。
- 剩余五张卡片采用第一排三张、第二排两张的布局。
- 同步首页测试；保留未引用的历史 SVG。

## Capabilities

### New Capabilities

- `profile-without-giwa`：定义移除 GIWA 后的首页内容与布局。当前没有已归档的主规范，此规范覆盖此前变更中要求展示 GIWA 和六张卡片的约束。

### Modified Capabilities

无。

## Impact

涉及 README.md、tests/test_profile.py；没有公共 API、依赖或运行时配置变更。

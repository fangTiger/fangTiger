## 1. 测试与修改

- [x] 1.1 更新首页断言，确认删除 GIWA 和五张卡片布局的测试先失败
- [x] 1.2 删除 README 的 GIWA 卡片、说明行和相关总览文案，调整卡片分组

## 2. 验证

- [x] 2.1 运行完整单元测试、OpenSpec 严格校验与差异检查，核对规范场景

验证记录：测试先出现 3 个预期失败；修改后 `python3 -m unittest discover -s tests -v` 的 9 项测试全部通过（0.004 秒）。`openspec validate remove-giwa-showcase --strict` 与 `git diff --check` 均通过。核对卡片顺序、五行项目介绍、品牌及联系入口符合规范。未提交或推送。

# ChatCI

ChatCI 是 ChatArch 的 CI workflow package shell。当前公开 CLI surface 是 root-only，用于保留 PyPI package / console command 的规范入口。

## 安装

```bash
pip install ChatCI
```

## CLI

```bash
chatci --help
chatci --version
chatci --tree
```

当前命令树：

```text
chatci  # ChatCI command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## 维护规则

- `chatci --tree` 必须从真实 Click command registry 生成，不手写假树。
- 新增真实业务命令时，必须同步测试、README、双语 docs 与 release report。
- MkDocs Material 站点必须启用 Material emoji renderer，避免 Material 图标简写语法泄漏到生产页面。

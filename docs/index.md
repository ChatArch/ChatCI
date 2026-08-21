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
chatci --tree-brief
```

当前命令树：

```text
chatci
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 维护规则

- `chatci --tree` 必须通过 ChatStyle 共享 runtime 从真实 Click command registry 生成，并默认显示参数签名。
- `chatci --tree-brief` 必须保留命令节点和描述，同时省略参数签名。
- 新增真实业务命令时，必须同步测试、README、双语 docs 与 release report。
- MkDocs Material 站点必须启用 Material emoji renderer，避免 Material 图标简写语法泄漏到生产页面。

# CLI 树

`chatci --tree` 输出当前真实注册的 Click command surface，并为每个节点提供简短用途注释。

```text
chatci  # ChatCI command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

当前 `ChatCI` 没有真实业务二级命令；只有 root options。后续新增命令时，必须先让测试锁定新的 command surface，再更新本文档。

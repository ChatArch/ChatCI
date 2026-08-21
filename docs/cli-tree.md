# CLI 树

`chatci --tree` 通过 ChatStyle 共享 Click tree runtime 输出当前真实注册的 command surface，默认包含参数签名，并为每个节点提供简短用途注释。

```text
chatci
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatci --tree-brief` 保留命令节点和描述，但省略参数签名。当前 `ChatCI` 没有真实业务二级命令，且 root options 都是 flag，因此 full 与 brief 输出目前包含相同节点。后续新增命令时，必须先让测试锁定两种 command surface，再更新本文档。

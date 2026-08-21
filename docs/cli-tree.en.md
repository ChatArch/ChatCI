# CLI Tree

`chatci --tree` uses the shared ChatStyle Click tree runtime to print the registered command surface with parameter signatures by default and compact purpose comments for each node.

```text
chatci
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatci --tree-brief` keeps command nodes and descriptions while omitting parameter signatures. `ChatCI` currently has no real second-level business command and all root options are flags, so full and brief currently contain the same nodes. When a new command is added, update tests for both surfaces first and then synchronize this document.

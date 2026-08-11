# CLI Tree

`chatci --tree` prints the currently registered Click command surface with compact purpose comments for each node.

```text
chatci  # ChatCI command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

`ChatCI` currently has no real second-level business command; it exposes root options only. When a new command is added, update the tests first and then synchronize this document.

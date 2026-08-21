# ChatCI

ChatCI is the ChatArch CI workflow package shell. Its current public CLI surface is root-only, keeping the PyPI package and console command entrypoint compliant.

## Install

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

Current command tree:

```text
chatci
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Maintenance rules

- `chatci --tree` must use the shared ChatStyle runtime to generate output from the real Click command registry, including parameter signatures by default.
- `chatci --tree-brief` must keep command nodes and descriptions while omitting parameter signatures.
- Any new real business command must update tests, README, bilingual docs, and the release report.
- The MkDocs Material site must enable the Material emoji renderer so Material icon shorthand never leaks to production pages.

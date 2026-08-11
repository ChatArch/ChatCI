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
```

Current command tree:

```text
chatci  # ChatCI command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## Maintenance rules

- `chatci --tree` must be generated from the real Click command registry, not maintained as a hand-written fake tree.
- Any new real business command must update tests, README, bilingual docs, and the release report.
- The MkDocs Material site must enable the Material emoji renderer so Material icon shorthand never leaks to production pages.

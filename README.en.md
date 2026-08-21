<div align="center">
    <a href="https://pypi.python.org/pypi/ChatCI">
        <img src="https://img.shields.io/pypi/v/ChatCI.svg" alt="PyPI version" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatCI/">
        <img src="https://img.shields.io/badge/docs-ChatArch-blue" alt="Docs" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatCI

ChatCI is the ChatArch CI workflow package shell. It keeps the PyPI package and console command entrypoint compliant.

- Docs: https://arch.gh.wzhecnu.cn/ChatCI/
- PyPI: https://pypi.org/project/ChatCI/

## Quick Start

```bash
pip install ChatCI
chatci --help
chatci --version
chatci --tree
chatci --tree-brief
```

Development environment:

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
python -m twine check dist/*
```

## CLI Contract

Current command-tree readback:

```text
chatci
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatci --tree` is generated from the real registry by the shared ChatStyle Click tree runtime and includes command parameter signatures by default. `chatci --tree-brief` keeps command nodes and descriptions while omitting parameter signatures. `ChatCI` currently has a root-options-only surface whose public options are all flags, so both modes currently contain the same nodes. When a command is added, tests, README, MkDocs docs, and the release report must be synchronized.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: bilingual MkDocs Material documentation

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.

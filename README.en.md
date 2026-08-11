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
chatci  # ChatCI command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

`ChatCI` currently has a root-options-only surface; it has no real second-level business command. When a command is added, `chatci --tree` must be generated from the real Click registry and tests, README, MkDocs docs, and the release report must be synchronized.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: bilingual MkDocs Material documentation

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.

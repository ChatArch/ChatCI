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

ChatCI 是 ChatArch 的 CI workflow package shell，用于保留 PyPI package / console command 的规范入口。

- 文档：https://arch.gh.wzhecnu.cn/ChatCI/
- PyPI：https://pypi.org/project/ChatCI/

## 快速开始

```bash
pip install ChatCI
chatci --help
chatci --version
chatci --tree
```

开发环境：

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
python -m twine check dist/*
```

## CLI 规范

当前可回读命令树：

```text
chatci  # ChatCI command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

当前 `ChatCI` 是 root-options-only surface；没有真实业务二级命令。后续新增命令时，必须从真实 Click registry 生成 `chatci --tree`，并同步测试、README、MkDocs 文档和 release report。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：MkDocs Material 双语文档

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。

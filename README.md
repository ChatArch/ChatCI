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
chatci --tree-brief
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
chatci
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatci --tree` 由 ChatStyle 共享 Click tree runtime 从真实 registry 生成，并默认显示命令参数签名；`chatci --tree-brief` 保留命令节点和描述，但省略参数签名。当前 `ChatCI` 是 root-options-only surface，所有公开选项都是 flag，因此两种输出目前包含相同节点。后续新增命令时，必须同步测试、README、MkDocs 文档和 release report。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：MkDocs Material 双语文档

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。

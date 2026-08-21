from pathlib import Path


def test_mkdocs_material_i18n_public_domain_and_icon_renderer():
    mkdocs = Path("mkdocs.yml").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    readme = Path("README.md").read_text(encoding="utf-8")
    readme_en = Path("README.en.md").read_text(encoding="utf-8")

    assert "site_url: https://arch.gh.wzhecnu.cn/ChatCI/" in mkdocs
    assert "repo_url: https://github.com/ChatArch/ChatCI" in mkdocs
    assert "name: material" in mkdocs
    assert "- i18n:" in mkdocs
    assert "docs_structure: suffix" in mkdocs
    assert "mkdocs-static-i18n" in pyproject
    assert "mkdocs-material>=9.5,<10.0" in pyproject
    assert "pymdownx.emoji" in mkdocs
    assert "material.extensions.emoji.twemoji" in mkdocs
    assert "material.extensions.emoji.to_svg" in mkdocs
    assert "Documentation = \"https://arch.gh.wzhecnu.cn/ChatCI/\"" in pyproject
    assert "https://arch.gh.wzhecnu.cn/ChatCI/" in readme
    assert "https://arch.gh.wzhecnu.cn/ChatCI/" in readme_en


def test_cli_tree_docs_are_bilingual_and_use_public_command():
    zh = Path("docs/cli-tree.md").read_text(encoding="utf-8")
    en = Path("docs/cli-tree.en.md").read_text(encoding="utf-8")

    assert "chatci --tree" in zh
    assert "chatci --tree" in en
    assert "chatci --tree-brief" in zh
    assert "chatci --tree-brief" in en
    assert "参数签名" in zh
    assert "parameter signatures" in en
    assert "python -m chatci.cli" not in zh
    assert "python -m chatci.cli" not in en

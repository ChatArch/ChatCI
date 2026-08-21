from pathlib import Path


def test_publish_workflow_uses_oidc_with_release_guards():
    workflow = Path(".github/workflows/publish.yml").read_text(encoding="utf-8")

    assert "id-token: write" in workflow
    assert "pypa/gh-action-pypi-publish@release/v1" in workflow
    assert "Check tag matches package version" in workflow
    assert "Check release commit is on default branch" in workflow
    assert "git fetch --no-tags origin main:refs/remotes/origin/main" in workflow
    assert "Check PyPI version" in workflow
    assert "is already on PyPI" in workflow
    assert "environment: pypi" not in workflow


def test_ci_builds_docs_smokes_installed_cli_and_checks_distributions():
    workflow = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert ".[dev,docs]" in workflow
    assert "mkdocs build --strict" in workflow
    assert "chatci --version" in workflow
    assert "chatci --tree" in workflow
    assert "chatci --tree-brief" in workflow
    assert "python -m twine check dist/*" in workflow


def test_docs_workflows_exist_and_use_chatarch_public_domain():
    deploy = Path(".github/workflows/deploy.yaml").read_text(encoding="utf-8")
    preview = Path(".github/workflows/preview.yaml").read_text(encoding="utf-8")

    assert "mkdocs gh-deploy --force" in deploy
    assert "mike deploy" not in deploy
    assert "mike set-default" not in deploy
    assert "site_url" in preview
    assert "CHATARCH_PREVIEW_URL" in preview
    assert "${site_url}/dev/" in preview
    assert "github.io" not in preview

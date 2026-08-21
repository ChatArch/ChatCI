import click
from click.testing import CliRunner

from chatci import __version__
from chatci.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatci, version {__version__}" in result.output


def test_help_mentions_tree_option():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0, result.output
    assert "--tree" in result.output
    assert "--tree-brief" in result.output
    assert "Print the registered CLI tree" in result.output


def test_tree_shows_registered_top_level_surface_with_purposes():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert result.output.startswith("chatci\n")
    assert not result.output.startswith("main\n")
    assert "├── --help  # Show this message and exit." in result.output
    assert "├── --version  # Show the version and exit." in result.output
    assert "├── --tree  # Print the registered CLI tree and exit." in result.output
    assert (
        "└── --tree-brief  # Print the registered CLI tree without parameter "
        "signatures and exit."
    ) in result.output
    assert "#" in result.output


def test_tree_defaults_to_signatures_and_brief_omits_them(monkeypatch):
    @click.command("inspect")
    @click.argument("target")
    @click.option("--format", "output_format", metavar="FORMAT")
    def inspect_command(target: str, output_format: str | None) -> None:
        """Inspect a CI target."""

    monkeypatch.setitem(main.commands, "inspect", inspect_command)

    full = CliRunner().invoke(main, ["--tree"])
    brief = CliRunner().invoke(main, ["--tree-brief"])

    assert full.exit_code == 0, full.output
    assert brief.exit_code == 0, brief.output
    full_line = next(line for line in full.output.splitlines() if "# Inspect a CI target." in line)
    brief_line = next(line for line in brief.output.splitlines() if "# Inspect a CI target." in line)
    assert "<TARGET>" in full_line
    assert "[--format OUTPUT-FORMAT]" in full_line
    assert brief_line == "└── inspect  # Inspect a CI target."
    assert "<TARGET>" not in brief_line
    assert "--format" not in brief_line


def test_template_hello_command_is_not_registered():
    result = CliRunner().invoke(main, ["hello"])

    assert result.exit_code != 0
    assert "No such command" in result.output

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
    assert "Print the registered command tree" in result.output


def test_tree_shows_registered_top_level_surface_with_purposes():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert "chatci  # ChatCI command-line interface." in result.output
    assert "├── --help  # Show this help message." in result.output
    assert "├── --version  # Show the installed package version." in result.output
    assert "└── --tree  # Print the registered command tree." in result.output
    assert "#" in result.output


def test_template_hello_command_is_not_registered():
    result = CliRunner().invoke(main, ["hello"])

    assert result.exit_code != 0
    assert "No such command" in result.output

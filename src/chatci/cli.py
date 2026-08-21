"""CLI entrypoint for chatci."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatci import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
)
@click.version_option(__version__, prog_name="chatci")
@add_tree_option(renderer_options={"root_name": "chatci"})
def main() -> None:
    """ChatCI command-line interface."""


if __name__ == "__main__":
    main()

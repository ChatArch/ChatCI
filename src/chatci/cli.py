"""CLI entrypoint for chatci."""

from __future__ import annotations

from collections.abc import Iterable

import click

from chatci import __version__


def _purpose(command: click.Command) -> str:
    """Return a compact one-line purpose for a Click command."""
    help_text = command.help or command.short_help or ""
    line = " ".join(help_text.strip().split())
    if not line:
        return "No description."
    return line if line.endswith(".") else f"{line}."


def _format_param(param: click.Parameter) -> str | None:
    """Render a compact command-tree signature fragment for one parameter."""
    if isinstance(param, click.Option):
        if param.hidden:
            return None
        names = [name for name in param.opts if name.startswith("--")]
        if not names:
            names = list(param.opts)
        if not names:
            return None
        name = names[0]
        if param.is_bool_flag:
            return f"[{name}]"
        metavar = param.metavar or param.name.upper().replace("_", "-")
        return f"[{name} <{metavar}>]"
    if isinstance(param, click.Argument):
        metavar = param.metavar or param.name.upper().replace("_", "-")
        token = f"<{metavar}>"
        if not param.required:
            return f"[{token}]"
        return token
    return None


def _signature(command: click.Command) -> str:
    parts = [part for part in (_format_param(param) for param in command.params) if part]
    return " ".join(parts)


def _iter_visible_commands(command: click.Command) -> Iterable[tuple[str, click.Command]]:
    if not isinstance(command, click.Group):
        return []
    ctx = click.Context(command)
    commands: list[tuple[str, click.Command]] = []
    for name in command.list_commands(ctx):
        child = command.get_command(ctx, name)
        if child is not None and not child.hidden:
            commands.append((name, child))
    return commands


def render_cli_tree(command: click.Command, *, root_name: str = "chatci") -> str:
    """Render the registered Click command tree with compact purpose comments."""
    lines = [f"{root_name}  # {_purpose(command)}"]
    pseudo_leaves = [
        ("--help", "Show this help message."),
        ("--version", "Show the installed package version."),
        ("--tree", "Print the registered command tree."),
    ]
    children = list(_iter_visible_commands(command))
    entries: list[tuple[str, str, click.Command | None]] = []
    entries.extend((name, purpose, None) for name, purpose in pseudo_leaves)
    entries.extend((name, _purpose(child), child) for name, child in children)

    def visit(entries: list[tuple[str, str, click.Command | None]], prefix: str = "") -> None:
        for index, (name, purpose, child) in enumerate(entries):
            is_last = index == len(entries) - 1
            branch = "└──" if is_last else "├──"
            if child is None:
                lines.append(f"{prefix}{branch} {name}  # {purpose}")
                continue
            signature = _signature(child)
            label = f"{name} {signature}" if signature else name
            lines.append(f"{prefix}{branch} {label}  # {purpose}")
            grand_children: list[tuple[str, str, click.Command | None]] = [
                (child_name, _purpose(grand_child), grand_child)
                for child_name, grand_child in _iter_visible_commands(child)
            ]
            if grand_children:
                child_prefix = prefix + ("    " if is_last else "│   ")
                visit(grand_children, child_prefix)

    visit(entries)
    return "\n".join(lines)


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
)
@click.version_option(__version__, prog_name="chatci")
@click.option(
    "--tree",
    is_flag=True,
    is_eager=True,
    expose_value=True,
    help="Print the registered command tree and exit.",
)
@click.pass_context
def main(ctx: click.Context, tree: bool) -> None:
    """ChatCI command-line interface."""
    if tree:
        click.echo(render_cli_tree(ctx.command, root_name="chatci"))
        ctx.exit()


if __name__ == "__main__":
    main()

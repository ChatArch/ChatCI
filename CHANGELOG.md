# Changelog

## 0.1.3 - 2026-08-21

### Changed
- Migrate the top-level Click tree options to the shared ChatStyle runtime with the public `chatci` root name.
- Add `chatci --tree-brief` for command-tree readback without parameter signatures while keeping signatures in `chatci --tree`.
- Raise runtime bounds to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.

## 0.1.2 - 2026-08-12

### Added
- Add MkDocs Material bilingual documentation under the ChatArch docs domain.
- Add Preview Docs and Deploy Docs workflows for public docs publishing.
- Add docs/workflow contract tests for the ChatArch CLI/docs/release surface.

### Changed
- Enable MkDocs Material emoji rendering via `pymdownx.emoji` with Material `twemoji`/`to_svg`.
- Add docs extras and PyPI Documentation metadata for https://arch.gh.wzhecnu.cn/ChatCI/.
- Harden tag-driven PyPI publishing with tag/package-version, default-branch, and exact PyPI version guards.
- Add installed CLI smoke checks and docs build to CI.
- Publish the production docs site directly to the `gh-pages` root so `https://arch.gh.wzhecnu.cn/ChatCI/` returns content instead of a version redirect.

## 0.1.1 - 2026-08-10

### Added
- Add top-level `chatci --tree` generated from the registered Click command tree.

### Changed
- Update README quickstart and version tests for the `0.1.1` patch release.
- Tighten ChatArch internal dependency lower bounds to `chatstyle>=0.1.1,<0.2.0` and `chatenv>=0.2.3,<0.3.0`.

## 0.1.0 - 2026-07-05

### Added
- First tag-driven release through GitHub Actions and PyPI Trusted Publisher.

## 0.0.1 - 2026-07-05

### Added
- Placeholder release for PyPI name registration.

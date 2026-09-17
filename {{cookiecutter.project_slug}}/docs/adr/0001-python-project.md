# 1. Python project

Date: 2026-09-17

## Status

Accepted

## Context

A new project is being started that will be implemented in Python.

## Decision

Use a standard layout for the project with the following details:
- Use [uv](https://docs.astral.sh/uv/) as the package manager.
- Use [pytest](https://docs.pytest.org/en/stable/) as the test framework (with coverage).
- Use [adr-tools](https://github.com/npryce/adr-tools) to document architectural decisions.
- Use [ast-grep](https://ast-grep.github.io/) rules (in `.ast-grep/rules/`) to disallow comments and docstrings.

Use the following layout for the python project:

```plaintext
project-root/
├── {{cookiecutter.package_name}}/
├── tests/
└── docs/
```

### Working with coding agents (and humans)

Much of the code in this project is configured to make working with LLM coding agents easier (and humans too!).
Agents often produce a common problems (stray comments, dead code, near-duplicate code, imports buried inside functions, sprawling functions), so tooling is chosen to catch at CI time:

- **No comments or docstrings** ([ast-grep](https://ast-grep.github.io/) rules in `.ast-grep/rules/`).
  Code is expected to be self-documenting. `make lint` flags them and `make fix` strips them. Motivated by
  [Inside Out: Uncovering How Comment Internalization Steers LLMs for Better or Worse](https://arxiv.org/pdf/2512.16790),
  which shows LLMs lean heavily on comments and that this steers their output in
  unpredictable, model- and task-dependent ways. A small allowlist for exceptional cases: 
  `# noqa`, `# type: ignore`, `# pragma`, and `# WHY:` prefixed comments.
- **Dead code is rejected immediately** ([vulture](https://github.com/jendrikseipp/vulture)). Unused code is not allowed by default.
  Agents tend to leave behind unused functions, arguments, and variables; vulture fails CI
  on them so they are removed in the same change that created them.
- **Duplicate code is surfaced** ([treepeat](https://github.com/dsummersl/treepeat)). `make treepeat` lets us find and refactor duplicate/similar code. It is advisory (not part of `make ci`); run it when looking for refactors. We expect to lower the `--similarity` threshold (default 100, exact matches only) as the project grows, to catch near-duplicates more aggressively.
- **Keep imports at the top of the file** (ruff `B`, `PLR`, `PLC`, `TID` rule sets).
  Agents often add imports inside the function that needs them; prevent it.
- **Size and complexity limits** ([radon](https://radon.readthedocs.io/) via
  `.github/scripts/check_radon.sh`). Cyclomatic complexity and maintainability index must stay at grade A, and functions must be under 80 lines, to prevent overly long/complex functions.
- **Strict typing** (mypy `strict = true`). Use typing to enforce code boundaries.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.

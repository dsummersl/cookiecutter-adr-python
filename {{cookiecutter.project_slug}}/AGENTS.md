# Agent Guidelines

This file provides guidance when working with code in this repository.

## Project Overview

See this projects README.md for an overview of the project, and ADR documents in docs/adr/ for architectural decisions.

## Development Commands

**IMPORTANT**: Always use the Makefile commands for development tasks.

### Setup
```bash
make setup  # Set up venv and sync dependencies with uv
```

### Testing
```bash
make test                                    # Run all tests with pytest and coverage
uv run pytest tests/test_hello.py             # Run specific test file
uv run pytest tests/test_hello.py::test_name  # Run specific test
uv run pytest -v                             # Verbose output
```

### Code Quality
```bash
make lint   # Check code with ruff
make fix    # Auto-fix ruff issues
make type   # Type check with mypy (strict mode)
make radon  # Check cyclomatic complexity and maintainability
make ci     # Run all CI checks (lint + type + test + radon)
```

**Before completing any feature**, run `make ci` to ensure all checks pass.

## Code Quality Requirements

Writing guidance:

- Only include a brief description of the thing in docstrings (no arguments or return types)
- Do not use docstrings at the beginning of files.

## Project Structure

```
{{cookiecutter.package_name}}/       # Main package source code
tests/          # Test files (mirror treepeat/ structure)
docs/adr/       # Architecture Decision Records
```

## Pull request workflow

### Opening a PR
- Add or update an automated test that exercises the feature or fix.
- Fill in the PR template's "Post-merge verification" section with concrete
  steps someone could run on a fresh checkout of main: commands, URLs,
  locations to check, and what a pass looks like.
- After opening the PR, subscribe to its activity and fix CI failures.
- Never merge unless I explicitly say to.

### When I say "approved, merge and verify"
1. Merge the PR (enable auto-merge if checks are still running).
2. Wait for the CI run on main for the merge commit. If it fails, say so
   and open a fix PR.
3. Check out main fresh, follow the README setup exactly as written, and
   note any step that doesn't work as documented.
4. Run each step in the PR's "Post-merge verification" section.
   Take screenshots where a visual check is needed.
5. Comment the results on the merged PR: what you ran, pass or fail for
   each step, and anything that needs my judgment.
6. If something fails, open a fix PR or issue. Do not edit main directly.

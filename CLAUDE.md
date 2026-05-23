# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Set up environment
python3 -m venv .venv
source .venv/bin/activate
pip install pytest

# Run tests
.venv/bin/pytest test_password_checker.py -v

# Run a single test
.venv/bin/pytest test_password_checker.py::test_strong_password -v

# Run the checker interactively (hidden input)
python3 password_checker.py

# Pass a password directly (for scripting)
python3 password_checker.py "MyP@ssw0rd!"
```

Exit code is `0` when the password scores ≥ 40 (Fair or better), `1` when too weak — useful for shell scripting.

## Architecture

Everything lives in two files:

- **`password_checker.py`** — logic + CLI. `check_strength(password) -> StrengthResult` is the core function. It scores 0–100 across five criteria (length, character variety, common-password list, sequential patterns, repeated characters) and returns a label and actionable feedback list. `main()` handles the CLI: reads via `getpass` by default, or accepts a positional argument.
- **`test_password_checker.py`** — pytest tests for `check_strength`.

## Scoring

| Criterion | Points |
|---|---|
| Length < 8 | +0 (penalty feedback) |
| Length 8–11 | +10 |
| Length 12–15 | +20 |
| Length ≥ 16 | +30 |
| Lowercase present | +10 |
| Uppercase present | +10 |
| Digit present | +10 |
| Special char present | +20 |
| All four types present | +10 bonus |
| Common password | score capped at 10 |
| Sequential run (≥ 3) | −10 |
| Repeated run (≥ 3) | −10 |

Strength labels: Very Weak (<20), Weak (<40), Fair (<60), Strong (<80), Very Strong (≥80).

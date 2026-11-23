# AGENTS.md – GPA Calculator

Instructions for AI coding agents (and humans) working in this repository.

## Purpose
A small console GPA calculator. The user adds courses (name, credits, score 0–100).
The program converts the score to a letter grade and calculates GPA on a 4.0 scale.
Courses are saved in `courses.json`.

## Architecture
- `main.py` – entry point: console menu, user input, saving/loading `courses.json`.
- `gpa.py` – business logic only: `score_to_letter()`, `letter_to_points()`, `calculate_gpa()`.
  No `input()` or `print()` here.
- `tests/test_gpa.py` – automated tests (pytest).
- `courses.json` – local user data. Never committed (listed in `.gitignore`).

## Setup
    python -m venv venv
    venv\Scripts\activate          (Windows)
    pip install -r requirements.txt
    pip install ruff mypy

Tested with Python 3.13.1, pytest 9.2.0, ruff 0.17.6.

## Safe commands (allowed without asking)
- `pytest -v` – run tests
- `ruff check .` – lint
- `mypy .` – type check
- `python main.py` – run the program
- `git status`, `git diff`, `git log` – read-only git commands

## Coding conventions
- Follow PEP 8. Use clear names and small functions.
- Keep business logic in `gpa.py`, keep input/output in `main.py`.
- Add type hints to every new or changed function.
- Do not change the grading scale (score -> letter -> points) without human approval.

## Test expectations
- Every bug fix or new feature must have a test in `tests/`.
- `pytest` must show 0 failed before any commit.
- Acceptance criteria that must always stay true:
  - AC1: score 96 -> A (4.0), score 81 -> B (3.0)
  - AC2: GPA is weighted by credits (96 with 5 cr + 81 with 3 cr -> 3.62)
  - AC3: courses stay in `courses.json` after restart
  - AC4: all tests pass

## Forbidden actions
- Do NOT read, create or commit secrets, passwords, tokens or `.env` files.
- Do NOT commit real personal data (`courses.json` must stay ignored).
- Do NOT deploy anything or push directly to `main` without human review.
- Do NOT run destructive commands: `rm -rf`, `del /s`, `git push --force`,
  `git reset --hard`, or delete files that are not part of the task.
- Do NOT add, remove or upgrade dependencies without human approval.
- Do NOT edit or delete tests just to make them pass.

## Review gates
- The agent works in a separate branch and proposes a diff.
- A human reads the diff, runs `pytest -v` and `ruff check .`, and approves before merge.
- If any test fails, the change is not merged.

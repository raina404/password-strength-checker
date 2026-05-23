# BUILD_LOG — Password Strength Checker

## Task 1 — Scaffold repo and CLAUDE.md
- Brief: Create repo, clone it, write CLAUDE.md with project conventions.
- What Claude proposed: Full project scaffold including password_checker.py and tests.
- What I changed before approving: Hand-edited CLAUDE.md to add project description, tech stack, conventions, and things Claude should not do.
- Verification: Repo exists on GitHub with CLAUDE.md committed on main.
- One thing I learned: Claude will build the whole project if you don't use plan mode first.

## Task 2 — Core scoring and tips functions
- Brief: Write check_strength() that scores a password 0-100 and returns tips.
- What Claude proposed: Full implementation with common password list, sequential/repeated detection, and color CLI output.
- What I changed before approving: Nothing — plan was already implemented before I could review it.
- Verification: pytest passes on all 16 tests.
- One thing I learned: Claude writes more than you ask for when given no constraints.

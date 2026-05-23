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

## Task 3 — Web interface
- Brief: Add Flask routes and HTML templates on top of the existing check_strength() function.
- What Claude proposed: app.py with GET / and POST /check routes, index.html form, result.html with color-coded score and tips.
- What I changed before approving: Nothing, plan looked correct and all 16 tests still passed.
- Verification: Ran .venv/bin/pytest — all 16 tests pass. Smoke tested GET / and POST /check with weak and strong passwords.
- One thing I learned: Claude can wire a web interface onto existing functions cleanly when you tell it exactly which function to use and what not to touch.

## Task 4 — Web route tests
- Brief: Write two tests myself for the web routes.
- What Claude proposed: Nothing — I wrote these myself.
- What I changed before approving: Moved test file to root directory to fix import error.
- Verification: .venv/bin/pytest test_web.py -v — both tests pass.
- One thing I learned: pytest needs to be run from the same directory as the files it imports.

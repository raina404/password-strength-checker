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

## Task 5 — Manual end-to-end verification
- Brief: Run the app and test 3 different passwords in the browser.
- What Claude proposed: N/A — manual step.
- What I changed before approving: N/A.
- Verification: Ran python3 app.py, tested "abc" (red/Very Weak), "Hello1!" (amber/Fair), "K@9mVz#2Lp!wQr8&" (green/Very Strong). All showed correct colors and tips.
- One thing I learned: The color coding makes it immediately obvious how weak most common passwords are.

## Task 6 — Tag v0.1 release
- Brief: Tag the final working commit as v0.1.
- What Claude proposed: N/A — git command.
- What I changed before approving: N/A.
- Verification: git tag v0.1 exists and git push --tags succeeded.
- One thing I learned: Tagging releases makes it easy to point someone to exactly what you shipped.

## Reflection

With the agentic workflow I was able to ship a full working web app in a few hours that I would not have been able to build on my own in that time. The scoring logic, the web routes, the templates, and the tests were all created faster than I could have typed them myself. Without Claude Code I would have spent most of my time looking up syntax and debugging import errors instead of actually thinking about what I was building. The biggest time saver was that Claude already knew the patterns — I just had to describe what I wanted, review the plan, and verify the output.

I did have to override Claude more than I expected. The biggest moment was when Claude tried to handle the GitHub push itself and kept failing because it could not figure out the WSL authentication setup on my machine. I knew the fix right away — just run git push manually in the terminal — but Claude kept spinning and trying to install extra tools. I also had to stop Claude early on because it built the whole project before I even got to review a plan. That taught me that plan mode is not optional. If you skip it, Claude just runs.

This project showed me gaps I did not know I had. I do not fully understand how Python imports work across different folders, which is why my test file broke when I put it in a subfolder. I fixed it by moving the file to the root but I still do not know the proper way to structure it. I also realized I was relying on Claude to catch security issues I was missing myself, like the fact that the password input had no length limit. That is a problem because Claude does not always catch those things either. The only reason it got flagged was because I specifically asked chat to do a security review. If I had skipped that step the bug would have shipped. That is the gap I want to close — I want to build my own mental checklist of common security issues so I catch them before I even ask Claude.

At my internship I will use this same four lane workflow on every feature. Planning in chat, executing in Claude Code, polishing with Copilot, and reviewing in chat before anything merges. On day one the first thing I will do is write a CLAUDE.md for whatever codebase I am working in. That single habit made the biggest difference in this whole cohort. Every time I gave Claude clear context and conventions upfront it worked well. Every time I skipped that step it went off track and I had to clean up the mess.

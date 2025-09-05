import os
import subprocess
import sys


YN = {
'y': True,
'yes': True,
'n': False,
'no': False,
}


INIT_GIT = YN.get('{{ cookiecutter.init_git|lower }}', True)
USE_PRECOMMIT = YN.get('{{ cookiecutter.use_precommit|lower }}', True)
INIT_ADR = YN.get('{{ cookiecutter.init_adr|lower }}', True)


ROOT = os.path.abspath(os.curdir)




def run(cmd, check=True):
print('> ' + ' '.join(cmd))
try:
return subprocess.run(cmd, check=check)
except FileNotFoundError:
print(f"! Skipping: command not found: {cmd[0]}")
return subprocess.CompletedProcess(cmd, 0)




# 1) git init
if INIT_GIT:
run(["git", "init", "-b", "main"]) # falls back if -b unsupported
run(["git", "add", "."])
run(["git", "commit", "-m", "chore: scaffold from cookiecutter"])


# 2) uv sync (creates venv + installs)
# If you prefer to avoid creating a venv here, comment this out.
run(["uv", "sync"]) # installs prod + dev groups


# 3) pre-commit
if USE_PRECOMMIT:
run(["uv", "run", "pre-commit", "install"])


# 4) ADR init into docs/adr
if INIT_ADR:
adr_dir = os.path.join(ROOT, "docs", "adr")
os.makedirs(adr_dir, exist_ok=True)
# Try nat pryce adr-tools (shell) first
ret = run(["adr", "init", "docs/adr"], check=False)
if ret.returncode != 0:
# Try adr-tools-python (pip) variant if available
ret2 = run(["uv", "run", "adr", "init", "docs/adr"], check=False)
if ret2.returncode != 0:
print("! Could not initialize ADR. Install 'adr-tools' (shell) or 'adr-tools-python' and run:\n"
" adr init docs/adr")


print("\nDone. Next steps:\n 1) uv run pytest\n 2) uv run ruff check .\n 3) uv run adr new 'Record architecture decision'\n")

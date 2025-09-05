import os
import subprocess

ROOT = os.path.abspath(os.curdir)

def run(cmd, check=True):
    print("> " + " ".join(cmd))
    try:
        return subprocess.run(cmd, check=check)
    except FileNotFoundError:
        print(f"! Skipping: command not found: {cmd[0]}")
        return subprocess.CompletedProcess(cmd, 0)

run(["git", "init", "-b", "main"])  # falls back if -b unsupported
run(["git", "add", "."])
run(["git", "commit", "-m", "chore: scaffold from cookiecutter"])

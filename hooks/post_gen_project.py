import os
import subprocess


YN = {
    "y": True,
    "yes": True,
    "n": False,
    "no": False,
}


INIT_GIT = YN.get("{{ cookiecutter.init_git|lower }}", True)

ROOT = os.path.abspath(os.curdir)


def run(cmd, check=True):
    print("> " + " ".join(cmd))
    try:
        return subprocess.run(cmd, check=check)
    except FileNotFoundError:
        print(f"! Skipping: command not found: {cmd[0]}")
        return subprocess.CompletedProcess(cmd, 0)


if INIT_GIT:
    run(["git", "init", "-b", "main"])  # falls back if -b unsupported
    run(["git", "add", "."])
    run(["git", "commit", "-m", "chore: scaffold from cookiecutter"])

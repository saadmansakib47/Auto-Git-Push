import os
import subprocess
from datetime import datetime


def git_auto_push(repo_path):
    try:
        os.chdir(repo_path)

        status_process = subprocess.run\
        (
            ["git", "status", "--short"], capture_output=True, text=True, check=True
        )

        staged_files = [
            line.split()[1] for line in status_process.stdout.splitlines() if line.startswith("A") or line.startswith("M")
        ]

        if not staged_files:
            print("No new or modified problems solved. Exiting.")
            return

        commit_message = staged_files[0]

        subprocess.run(["git", "add", "."], check=True)

        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        subprocess.run(["git", "push", "origin", "main"], check=True)

        print(f"Changes have been successfully pushed to GitHub with commit message: '{commit_message}'")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing Git commands: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    repo_path = r"C:\Codeforces_Solved_Problems"  

    git_auto_push(repo_path)

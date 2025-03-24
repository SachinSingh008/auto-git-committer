import os
import random
import time
from datetime import datetime

# List of multiple Git repositories
repo_path = [
    r"C:/Users/rites/Desktop/Python AIML/auto-git-committer",
    r"C:/Users/rites/Desktop/Python AIML/laptop-price-predictor-regression-project-main",
    r"C:/Users/rites/Desktop/Python AIML/Price Predictor"
]

# Random commit messages
commit_messages = [
    "Minor update", "Fixed bug", "Improved performance", "Updated README",
    "Refactored code", "Code cleanup", "Added new feature", "Optimized logic"
]

# Generate a random number of commits (between 12-20)
total_commits = random.randint(12, 20)

def make_commit(repo_path):
    """Commits a random update to the selected repo."""
    os.chdir(repo_path)  # Change directory to the repo
    print(f"📌 Making a commit in: {repo_path} at {datetime.now()}...")

    filename = os.path.join(repo_path, "auto_commit_log.txt")
    with open(filename, "a") as f:
        f.write(f"Commit at {datetime.now()}\n")

    os.system("git add .")
    commit_message = random.choice(commit_messages)
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push origin main")

# Distribute commits across repositories
for _ in range(total_commits):
    selected_repo = random.choice(repo_path)  # Pick a random repo
    make_commit(selected_repo)
    time.sleep(random.randint(1, 5))  # Add slight delay for randomness

print("✅ Commits distributed across repositories successfully!")

    

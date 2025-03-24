import os
import random
import time
from datetime import datetime

# Set your repository path (update this)
repo_path = "/path/to/your/repository"

# Load commit messages from a file
with open("commit_messages.txt", "r") as f:
    commit_messages = f.readlines()
commit_messages = [msg.strip() for msg in commit_messages]

def make_commit():
    os.chdir(repo_path)
    
    # Modify a file (log file to track commits)
    filename = "auto_commit_log.txt"
    with open(filename, "a") as f:
        f.write(f"Commit at {datetime.now()}
")

    # Git commands
    os.system("git add .")
    commit_message = random.choice(commit_messages)
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push origin main")

# Generate random commit times (12-20 times a day)
commit_count = random.randint(12, 20)
intervals = sorted(random.sample(range(24 * 60 * 60), commit_count)) # Random times in a day

for interval in intervals:
    time.sleep(interval)  # Sleep until next commit
    make_commit()

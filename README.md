# Auto Git Committer

## Description
This script automates random GitHub commits 12-20 times per day.

## Setup
1. Install Git and Python (if not installed).
2. Clone or initialize your Git repository.
3. Update `repo_path` in `auto_commit.py` with your repo path.
4. Run the script:
   ```
   python auto_commit.py
   ```
5. To automate the script on reboot:
   - **Linux/macOS:** Add `@reboot python3 /path/to/auto_commit.py &` to `crontab -e`.
   - **Windows:** Use Task Scheduler to run it daily.

## Notes
- Ensure your Git credentials are saved (`git config --global credential.helper store`).
- The script logs commits in `auto_commit_log.txt`.

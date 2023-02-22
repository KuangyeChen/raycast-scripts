#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title List All Windows
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 
# @raycast.packageName System Utils

# Documentation:
# @raycast.description List all windows' name
# @raycast.author Kuangye Chen
# @raycast.authorURL https://github.com/KuangyeChen

import subprocess


def main():
    script = """
        tell application "System Events"
            set res to title of every window of every process
            log res
        end tell
    """
    p = subprocess.run(
        [
            "osascript",
            "-e",
            script,
        ],
        capture_output=True,
        text=True,
    )
    windows = [w.strip() for w in p.stderr.split(",")]
    print("All Windows:")
    for w in windows:
        if w == "":
            continue
        print(w)


if __name__ == "__main__":
    main()

import os
import sys

# FFmpeg fix
os.environ["PATH"] += os.pathsep + r'C:\ffmpeg\bin'

# Apne UI module ko call karein
from ui.cli_ui import start_ui

if __name__ == "__main__":
    try:
        start_ui()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        sys.exit()
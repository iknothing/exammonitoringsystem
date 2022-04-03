import wmi
import time
  
# Initializing the wmi constructor
f = wmi.WMI()
  

while True:
    flag = 0
    # Iterating through all the running processes
    for process in f.Win32_Process():
        if "chrome.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
        elif "msedge.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
        elif "brave.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
        elif "firefox.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
        elif "opera.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
        elif "Opera.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
        elif "operaGx.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
        elif "safari.exe" == process.Name:
            print("browser detected, pls close it for test to continue")
            flag = 1
            time.sleep(15)
            break
    if flag == 0:
        print("No browser detected, you may continue the test")
        time.sleep(15)

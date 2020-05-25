import subprocess
import wget
import time

try:
    wget.download('https://github.com/pbatard/rufus/releases/download/v3.9/rufus-3.9p.exe', r'C:\\')
    time.sleep(5)
    subprocess.call(["C:\\rufus-3.9p.exe"], shell=True)
except NotADirectoryError and FileNotFoundError and PermissionError:
    pass

    try:
        wget.download('https://github.com/pbatard/rufus/releases/download/v3.9/rufus-3.9p.exe', r'D:\\')
        time.sleep(5)
        subprocess.call(["D:\\rufus-3.9p.exe"], shell=True)
    except NotADirectoryError and FileNotFoundError and PermissionError:
        pass

        try:
            wget.download('https://github.com/pbatard/rufus/releases/download/v3.9/rufus-3.9p.exe', r'E:\\')
            time.sleep(5)
            subprocess.call(["E:\\rufus-3.9p.exe"], shell=True)
        except NotADirectoryError and FileNotFoundError and PermissionError:
            pass









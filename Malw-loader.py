import subprocess
import wget
import time
import winreg as ws
import os

#Author:Syed Sadam Hussain Shah

try:
    location = r'C:\\'
    wget.download('https://github.com/pbatard/rufus/releases/download/v3.9/rufus-3.9p.exe',location)
    if True:
        file_loc = location
    time.sleep(5)
    subprocess.call(["C:\\rufus-3.9p.exe"], shell=True)
except NotADirectoryError and FileNotFoundError and PermissionError:
    pass

    try:
        location = r'D:\\'
        wget.download('https://github.com/pbatard/rufus/releases/download/v3.9/rufus-3.9p.exe', location)
        if True:
            file_loc = location
        time.sleep(5)
        subprocess.call(["D:\\rufus-3.9p.exe"], shell=True)
    except NotADirectoryError and FileNotFoundError and PermissionError:
        pass

        try:
            location = r'E:\\'
            wget.download('https://github.com/pbatard/rufus/releases/download/v3.9/rufus-3.9p.exe',location)
            if True:
                file_loc = location
            time.sleep(5)
            subprocess.call(["E:\\rufus-3.9p.exe"], shell=True)
        except NotADirectoryError and FileNotFoundError and PermissionError:
            pass

def startup ():
    try:
        file_path = os.path.dirname(os.path.realpath(file_loc))
        file_name ="rufus-3.9p.exe"
        address1=os.path.join(file_path, file_name)
        HKEY = ws.HKEY_CURRENT_USER
        key ="Software\Microsoft\Windows\CurrentVersion\Run"
        open = ws.OpenKey(HKEY,key,0,ws.KEY_ALL_ACCESS)
        ws.SetValueEx(open,"any_name",0,ws.REG_SZ,address1)
        ws.CloseKey(open)
    except:
        pass

if __name__ == "__main__":
    startup()



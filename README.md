# Malw-loader
THis program is coded purely for educational purposes and I bear no responsibility for any misuse of Malw-loader. 

How it works:
Malw-loader is written in Python. It starts with directory listing, and then auto-downloads and executes malware in the target computer. It also edits registry and place your malware in startup, for persistence.

Usage:
You need to change the defualtdownload link from "https://github.com/pbatard/rufus/releases/download/v3.9/rufus-3.9p.exe" to your own link.
You also need to change the defualt file name from "D:\\rufus-3.9p.exe" to your own file hosted on a server, web-host etc.
You can convert this python file into exe by using pyinstaller or any other related python modules.
As far as dependencies are concerned you need to have subprocess, time, and wget module pre-installed.
You can install these modules by simply using pip command, i.e. pip install wget.

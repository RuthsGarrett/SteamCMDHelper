#!/usr/bin/python

#SHBANG!!
import sys
import os
import argparse
# import json
# import subprocess
from zipfile import ZipFile
import urllib
# import urllib.parse as url_parse


parser = argparse.ArgumentParser(description="Python based Tool for using the SteamCMD")
parser.add_argument('-d', '--dry-run', action='store_true', dest='dry_run', help="Dont execute downloads or modify files, just prints what would happen")


def main():
    print("\n---------------------------\n")
    print("Welcome to the SeamCMDHelper")
    print("\n---------------------------\n")
    #download
    downloadCMD("SteamCMD")

    #print(sys.platform)
    return 0

def downloadCMD(install_location):
    #always make the folder, if it already exists I doubt itll fail
    if not os.path.exists(install_location):
        os.mkdir(install_location)
    install_location = install_location + "/" #hope this doesnt screw up windows

    url = "null"
    if sys.platform == 'win32' or sys.platform == 'win64':
        print("I AM WINDOWS")
        url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
        urllib.urlretrieve(url, install_location+"steamcmd.zip")

    if sys.platform == 'linux2':
        print("I AM LINUX")
        url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
        urllib.urlretrieve(url, install_location+"steamcmd_linux.tar.gz")

    


if __name__ == '__main__':
    sys.exit(main())
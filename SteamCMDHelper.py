#!/usr/bin/python3

#SHBANG!!
import sys
import os
import argparse
# import json
# import subprocess
from zipfile import ZipFile

import urllib.request
# import urllib.parse as url_parse

level_all = 0
level_verbose = 1
level_debug = 2
# log_level = 0

parser = argparse.ArgumentParser(description="Python based Tool for using the SteamCMD")
# parser.add_argument('-d', '--dry-run', action='store_true', dest='dry_run', help="Dont execute downloads or modify files, just prints what would happen") #todo, all the things
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help="Enable verbose logging")
parser.add_argument('-D', '--debug', action='store_true', dest='debug', help="Enable debug logging. This should only be used if there are problems.")

args = parser.parse_args()
def main():
    #GLOBAL STUFF
    global log_level
    log_level = 0

    #END GLOBAL
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3") #not sure how you even would get to this point since im trying to import a python 3 module above

    #ARG stuff
    if args.verbose:
        log_level = 1
        d_print(level_verbose, "Verbose Logging Enabled")
    
    if args.debug:
        log_level = 2
        d_print(level_debug, "Debug Logging Enabled")


    d_print(level_all, "\n---------------------------\n")
    d_print(level_all, "Welcome to the SeamCMDHelper")
    d_print(level_all, "\n---------------------------\n")

    
    #download
    downloadCMD("SteamCMD")

    #print(sys.platform)
    return 0

def downloadCMD(install_location):
    #always make the folder, if it already exists I doubt itll fail
    if not os.path.exists(install_location):
        os.mkdir(install_location)
    install_location = install_location + "/" #hope this doesnt screw up windows

    d_print(level_all, "Downloading SteamCMD into folder: " + install_location)
    url = "null"
    if sys.platform == 'win32' or sys.platform == 'win64':
        d_print(level_debug, "I THINK I AM WINDOWS, SO I WILL DOWNLOAD A ZIP")
        url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
        urllib.request.urlretrieve(url, install_location+"steamcmd.zip")

    if sys.platform == 'linux':
        d_print(level_debug, "I THINK I AM LINUX, SO IM GOING TO TRY TO DOWNLOAD A TAR")
        url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
        urllib.request.urlretrieve(url, install_location+"steamcmd_linux.tar.gz")

    
def d_print(level, text):
    #Debug levels
    #0: base level - default value
    #1: extra logging - verbose option
    #2: full debug - to be used if stuff isnt working
    if log_level >= level:
        print(text)



if __name__ == '__main__':
    sys.exit(main())

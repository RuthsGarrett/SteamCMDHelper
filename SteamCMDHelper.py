#!/usr/bin/python3

#SHBANG!!
import sys
import os
import argparse
import json
# import subprocess
from zipfile import ZipFile

import urllib.request

class Settings:
    install_dir = ""
    installed_games =	{
        "example_game": 123 #Once im done working on this i will command this line out
    }



#Would put this in an enum but I cant think of a good reason to, its only 3 levels
level_all = 0
level_verbose = 1
level_debug = 2

parser = argparse.ArgumentParser(description="Python based Tool for using the SteamCMD")
parser.add_argument('-dr', '--dry-run', action='store_true', dest='dry_run', help="Dont execute downloads or modify files, just prints what would happen") #todo, all the things
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help="Enable verbose logging")
parser.add_argument('-D', '--debug', action='store_true', dest='debug', help="Enable debug logging. This should only be used if there are problems.")

args = parser.parse_args()
def main():
    #GLOBAL VARIABLES
    
    #global logging level
    global log_level
    log_level = 0
    #global dry run flag
    global dryrun
    dryrun = False

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

    if args.dryrun:
        d_print(level_all, "Dry Run Enabled - No files will be downloaded and no commands will be passed to the SteamCommandLine")
        dryrun = True


    #USER SETTINGS JSON - not sure how large this will end up being
    #But for now itll at least be steamcmd install location and a list of the games installed so far


    d_print(level_all, "\n---------------------------\n")
    d_print(level_all, "Welcome to the SeamCMDHelper")
    d_print(level_all, "\n---------------------------\n")


    #MAIN USER INPUT LOOP




    
    #download
    downloadCMD("SteamCMD")

    #print(sys.platform)
    return 0

def LoadJSON():
    import json #why do i have to do this here?
    d_print(level_debug, "Loading UserSettings JSON")
    json = json.loads(open("UserSettings.json"))
    userSettings = Settings()
    return 

def SaveJSON():
    d_print(level_debug, "Saving UserSettings JSON")


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
        if(not dryrun):
            urllib.request.urlretrieve(url, install_location+"steamcmd.zip")

    if sys.platform == 'linux':
        d_print(level_debug, "I THINK I AM LINUX, SO IM GOING TO TRY TO DOWNLOAD A TAR")
        url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
        if(not dryrun):
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

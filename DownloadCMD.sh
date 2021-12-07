#!/usr/bin/bash
echo "Making Install Folder - \"SeamCMD\""
mkdir SteamCMD
cd SteamCMD
curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

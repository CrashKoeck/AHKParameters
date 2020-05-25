#!/usr/bin/python
# -*- coding: utf-8 -*-



#---------------------------
#   Import Libraries
#---------------------------

import sys
import json
import codecs
import os
import clr

clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")



#---------------------------
#   [Required] Script Information
#---------------------------

ScriptName = "AutoHotkey Parameters"
Website = "CrashKoeck.com"
Description = "Run AutoHotkey scripts with or without parameters"
Creator = "CrashKoeck" 
Version = "1.0.0"



#---------------------------
#   Define Global Variables
#---------------------------

script_path = os.path.join(os.path.dirname(__file__), "AHKPScripts")
ReadMeFile = os.path.join(os.path.dirname(__file__), "ReadMe.txt")
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")



#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------

def Init():
    global ScriptSettings
    ScriptSettings = Settings(SettingsFile)
    return



#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------

def Execute(data):
    return



#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------

def Tick():
    return



#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------

def Parse(parseString, userid, username, targetid, targetname, message):
    if "$AHKP" in parseString:
        start = '$AHKP('
        end = ')'
        guts = (parseString.split(start))[1].split(end)[0]
        if "," in guts:
            script = guts.split(",", 1)
            args = guts.split(",")
            args.pop(0)
            RunAHKP(script[0],args)
        else:
            RunAHKP(guts,"")
        
        ahkp = "$AHKP({})".format(guts)
        return parseString.replace(ahkp,"")
    
    return parseString



#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------

def ReloadSettings(jsondata):

    # Reload newly saved settings and verify
    ScriptSettings.Reload(jsondata)

    # End of ReloadSettings
    return



#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------

def Unload():
    return



#---------------------------
#	Script Classes
#---------------------------

class Settings(object):
    """ Load in saved settings file if available else set default values. """
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            self.AHKPPath = "C:\Program Files\AutoHotkey"

    def Reload(self, jsondata):
        """ Reload settings from Streamlabs user interface by given json data. """
        self.__dict__ = json.loads(jsondata, encoding="utf-8")

    def Save(self, settingsfile):
        """ Save settings contained within to .json and .js settings files. """
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8", ensure_ascii=False)
            with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8', ensure_ascii=False)))
        except:
            Parent.Log(ScriptName, "Failed to save settings to file.")



#---------------------------
#	Custom Functions
#---------------------------

def RunAHKP(script,params):
    AHKPScript = os.path.join(script_path, "{}.ahk").format(script)
    if not params:
        os.startfile(AHKPScript)
    else:
        AHKPexe = os.path.join(ScriptSettings.AHKPPath, "{}.exe").format("AutoHotkey")
        params.insert(0,AHKPScript)
        params.insert(0,script)
        os.spawnv(os.P_NOWAIT, AHKPexe, params)
    
    return



#---------------------------
# Script UI Button Functions
#---------------------------

def OpenReadMe():
    """ Open the script readme file in users default .txt application. """
    os.startfile(ReadMeFile)
    return

def OpenAHKPScripts():
    """Open AHKPScripts folder"""
    os.startfile(os.path.join(os.path.dirname(__file__), "AHKPScripts"))

def VisitWebiste():
    """ Open Crash's website in users default browser. """
    os.system("start \"\" https://www.CrashKoeck.com")
    return

def JoinDiscord():
    """ Open Discord invite link in users default browser. """
    os.system("start \"\" https://discord.gg/zyS2jbJ")
    return
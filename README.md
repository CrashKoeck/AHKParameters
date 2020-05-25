# AHKParameters for Streamlabs Chatbot

<p align="center">AHKParameters allows you to run AutoHotkey scripts from <a href="https://streamlabs.com/chatbot">Streamlabs Chatbot</a> in commands and also allows you to pass custom parameters directly to your AutoHotkey scripts.</p>

<p align="center"><i><b>
  Crash on the interwebs<br>
  <a href="https://twitter.com/CrashKoeck">Twitter</a> |
  <a href="https://twitch.tv/CrashKoeck">Twitch</a> |
  <a href="https://youtube.com/Crashkoeck">YouTube</a> |
  <a href="https://patreon.com/Crashkoeck">Patreon</a> |
  <a href="https://discord.gg/zyS2jbJ">Discord</a>
</b></i></p>

***

## Setup
- Download the latest release of <b>AHKParameters.zip</b> from <a href="https://github.com/CrashKoeck/AHKParameters/releases">this page</a>
- Install and setup Python in Streamlabs Chatbot if you haven't already (Read the <a href="https://cdn.streamlabs.com/chatbot/Documentation_Twitch.pdf">Streamlabs Chatbot documentation</a> to see how to set up Python)
- Import the script into Streamlabs Chatbot (Read the <a href="https://cdn.streamlabs.com/chatbot/Documentation_Twitch.pdf">Streamlabs Chatbot documentation</a> to see how to import scripts)
- Right click on <b>AHKParameters</b> in the Streamlabs Chatbot script list and "Insert API key"
- Install <a href="https://www.autohotkey.com/">Autohotkey</a>
- Put your .ahk scripts into the <i>AHKPScripts</i> folder (open the scripts folder by clicking on the <b>Open Scripts Folder</b> button when the AHKParameters script is selected in Streamlabs Chatbot)
- Set the AutoHotkey install directory. It's usually ```C:\Program Files\AutoHotkey``` (already set by default).

***

## How to use
To trigger a script with no parameters, simply use ```$AHKP(scriptname)```. 

If you want to pass parameters to your script, separate everything with
commas. Start with your script name, then add as many parameters as you'd
like separated by commas.
```$AHKP(scriptname,paramter1,parameter2,parameter3)```

In your AutoHotkey script, you can access the parameters using ```A_Args```.
To get the first parameter, you'd use ```A_Args[1]```. Second parameter would be ```A_Args[2]```
	
```A_Args``` loads all of the parameters into an array. You can take a look at
the included <b>example.ahk</b> to get an idea of how it works.

***

## Warning
- Try to avoid special characters if possible as some will not properly pass
through Chatbot. Characters that will definitely <i>not</i> work are double quotes,
parentheses, and commas. ```"" () ,,```

***

## Future Plans
- None. Let me know if there is something that should be added.

***

## Support
- Be sure to join the <a href="https://discord.gg/zyS2jbJ">CrashPad Discord</a> for direct support

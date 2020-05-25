#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetKeyDelay, 50,100 ; This helps with reliability.

theObjects := ""

if(A_Args.Length() > 0){
	for key, value in A_Args {
		theObjects := theObjects . "Parameter number " . key . " is " . value . "`n"
	}
	MsgBox % theObjects
} else {
	MsgBox % "No parameters present"
}

ExitApp ; exits script so there are not multiple instances that start.
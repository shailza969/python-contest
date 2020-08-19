import os
import pyttsx3

pyttsx3.speak("Welcome")
print("The applications which you can run:")
print("1.	Vlc media player")
print("2.	Windows media player")
print("3.	morzilla firefox")
print("4.	google chrome")
print("5.	notepad")



p=input("Enter your query: ")
p = p.lower();
if("run" in p or "execte" in p or "launch" in p or "start" in p or "open" in p) and ("vlc" in p or ("media" in p and "player" in p and "vlc" in p) or ("vlc" in p and "player" in p)):
	pyttsx3.speak("opening vlc media player")
	os.system("vlc")

elif("run" in p or "execte" in p or "launch" in p or "start" in p or "open" in p) and ("wmplayer" in p or ("media" in p and "player" in p and "windows" in p) or ("windows" in p and "player" in p)):
	pyttsx3.speak("opening windows media player")
	os.system("wmplayer")

elif("run" in p or "execte" in p or "launch" in p or "start" in p or "open" in p) and ("firefox" in p or ("morzilla" in p and "firefox" in p)):
	pyttsx3.speak("opening morzilla firefox")
	os.system("firefox")

elif("run" in p or "execte" in p or "launch" in p or "start" in p or "open" in p) and ("chrome" in p or ("google" in p and "chrome" in p) or ("google" in p and "browser" in p)):
	pyttsx3.speak("opening chrome")
	os.system("chrome")

elif("run" in p or "execte" in p or "launch" in p or "start" in p or "open" in p) and ("notepad" in p or ("text" in p and "editor" in p and "notepad" in p) or ("text" in p and "editor" in p) or ("editor" in p)):
	pyttsx3.speak("opening notepad")
	os.system("notepad")

else:
	print("doesn't support")





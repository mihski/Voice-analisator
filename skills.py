import os,sys,webbrowser,requests,pyttsx3,subprocess

#иницилизация звук. движка:

engine =pyttsx3.init()
engine.setProperty('rate',100) # скорость речи

def speaker(text):
    engine.say(text)
    engine.runAndWait()


def vpn():
    subprocess.Popen("D:\Program Files\hiddify\HiddifyNext.exe")

def offpc():
    os.system("shutdoun /s")    

def weather():
    print()

def browser():
    print()
    webbrowser.open("https://www.youtube.com",new=2)

def offBot():
    sys.exit()

def pasive():
    pass



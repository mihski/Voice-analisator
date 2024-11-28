import os,sys,webbrowser,requests,pyttsx3,subprocess
from pprint import pprint

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
    open_weather_token = "9d215a832d490c71ce1544ee58aaf85e"
    city = "bon"
    code_smile = {'Clouds': "облачно \U00002601",
                    'Clear': "ясно \U00002600",
                    "Snow": "снег \U00001f328",
                    "Raine": "дождь \U00002614"
                    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        

        city = data["name"]
        temperature = data["main"]["temp"]
        wind = data["wind"]["speed"]
        wind_gradient = data["wind"]["deg"]
        pprint(temperature,wind)

    except Exception as ex:
        print(ex)
        print("проверте назание города")
        
def browser():
    print()
    webbrowser.open("https://www.youtube.com",new=2)

def offBot():
    sys.exit()

def passive():
    pass



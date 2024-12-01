import os,sys,webbrowser,requests,pyttsx3,subprocess
from pprint import pprint

#иницилизация звук. движка:

engine =pyttsx3.init()
engine.setProperty('rate',150) # скорость речи

def speaker(text):
    try:
        print("speaker вызван")
        engine.say(text)
        engine.runAndWait()
    except Exception as  e:
       print(f"Ошибка в speaker: {e}")
    



def vpn():
    subprocess.Popen("D:\Program Files\hiddify\HiddifyNext.exe")

def offpc():
    os.system("shutdoun /s")    


def weather():
    open_weather_token = "9d215a832d490c71ce1544ee58aaf85e"
    city = "санкт петербург"
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
        wind = int(data["wind"]["speed"])
        wind_gradient = data["wind"]["deg"]        

        if 0 < wind_gradient <= 22 or 338 < wind_gradient <= 360:
            wg = "С."
            wg_voce= "север"
        elif 22 < wind_gradient <= 67:
            wg = "СВ"
            wg_voce= "северовосток"
        elif 67 < wind_gradient <= 112:
            wg = "В"
            wg_voce= "восток"
        elif 112 < wind_gradient <= 157:
            wg = "ЮВ"
            wg_voce= "юговосток"            
        elif 157 < wind_gradient <= 202:
            wg = "Ю"
            wg_voce= "юг"
        elif 202 < wind_gradient <= 247:
            wg = "ЮЗ"
            wg_voce= "югозапад"
        elif 247 < wind_gradient <= 292:
            wg = "З"
            wg_voce= "запад"
        elif 292 < wind_gradient <= 338:
            wg = "СЗ"
            wg_voce= "северозапад"

        weather_description = data["weather"][0]["main"]

        if weather_description in code_smile:
            wd = code_smile[weather_description]
        else:
            wd = "не знаю"
       # pprint(f" температура {temperature} градусов")
        print(f'погода в городе :  {city}\nТемпература: {temperature} C, {wd}\nВетер: {wg},  {wind} m/c')
        text_for_audio = "температура"+str(int(temperature))+ (wd)+"градусов"+"ветер"+ str(wg_voce)+ str(wind)+ "метров всекунду"
        speaker(text_for_audio)

    except Exception as ex:
        print(ex)
        print("проверьте назание города")
        
def browser():
    print()
    webbrowser.open("https://www.youtube.com",new=2)

def offBot():
    sys.exit()

def passive():
    pass

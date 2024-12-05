import queue
import sounddevice as sd  
import vosk
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *
from tts import speaker_m
 
q= queue.Queue()  
device = sd.default.device = 1, 3

samplerate = int(sd.query_devices(device[0],'input')["default_samplerate"])

model = vosk.Model("model_small")


def callback(indata,frames,time,status):
    q.put(bytes(indata))

def recognize(data,vectorizer,clf):
    '''
    Анализ распознанной речи
    '''

    #проверяем есть ли имя бота в data, если нет, то return
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return
    print("погоняло услышано")
    #удаляем имя бота из текста
    data=data.replace(list(trg)[0], '')
    print(f"услышанный текст: {data}")

    if not data:
        print("Триггер услышан, но текст после него отсутствует. Ожидание нового ввода.")
        return
    #получаем вектор полученного текста
    #сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    print(f"answer  {answer}")

    #получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    #озвучка ответа из модели data_set    
    speaker_m(answer.replace(func_name, ''))
    print(f"answer  {answer}")

    #запуск функции из skills
    exec(func_name + '()')    

def main():
    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''
    print("БОТ ЗАПУЩЕН")
    speaker_m("бот запущен")
  
    #Обучение матрицы на data_set модели
    vectorizer =CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))
    del words.data_set

    with sd.RawInputStream(samplerate=samplerate,blocksize=44100,device=device[0],dtype="int16",
                            channels=1,callback=callback):    
        rec= vosk.KaldiRecognizer(model,samplerate)
        while True:            
            data = q.get()          
            if rec.AcceptWaveform(data):                    
                data = json.loads(rec.Result())["text"]
                if not data:
                    continue

                print("=> "+(data))             
                recognize(data,vectorizer,clf)
                
           
            #     partial = rec.PartialResult()  # Промежуточный результат в формате JSON
            #     print(partial)    

if __name__=="__main__":
    main()
import queue
import sounddevice as sd  
import vosk
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from pyttsx3 import voice
 
q= queue.Queue()  

device = sd.default.device = 1, 3

samplerate = int(sd.query_devices(device[0],'input')["default_samplerate"])

model = vosk.Model("model_small")

stop_flag =False
def callback(indata,frames,time,status):
    q.put(bytes(indata))

def recognize(data, vectorizer, clf):
    '''
    Анализ распознанной речи
    '''

    #проверяем есть ли имя бота в data, если нет, то return
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    #удаляем имя бота из текста
    data.replace(list(trg)[0], '')

    #получаем вектор полученного текста
    #сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    #получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    #озвучка ответа из модели data_set
    voice.speaker(answer.replace(func_name, ''))

    #запуск функции из skills
    exec(func_name + '()')    

def main():
    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''
    global stop_flag
    print("запуск")

    #Обучение матрицы на data_set модели
    vectoraizer =CountVectorizer()
    vectors = vectoraizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set


    with sd.RawInputStream(samplerate=samplerate,blocksize=48000,device=device[0],dtype="int16",
                            channels=1,callback=callback):    
        rec= vosk.KaldiRecognizer(model,samplerate)
        while not stop_flag:            
            data = q.get()
            if rec.AcceptWaveform(data):        
                result= rec.Result()  # результат в формате json          
                result_dict = json.loads(result)
                text = result_dict.get("text", "")#из словоря извлекается по ключу "text"
                                                # если ключа нет возвращается "" пустая строка
                print((result_dict)['text'])
                
                if "стой" in text.lower():
                    print("Команда 'stop' получена. Завершение программы.")
                    stop_flag = True                     
            # else:
            #     partial = rec.PartialResult()  # Промежуточный результат в формате JSON
            #     print(partial)    

if __name__=="__main__":
    main()
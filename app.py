import queue
import sounddevice as sd 
import vosk
import json

q= queue.Queue()

device = sd.default.device = 1, 3

samplerate = int(sd.query_devices(device[0],'input')["default_samplerate"])

model = vosk.Model("model_small")

stop_flag =False
def callback(indata,frames,time,status):
    q.put(bytes(indata))


with sd.RawInputStream(samplerate=samplerate,blocksize=48000,device=device[0],dtype="int16",
                         channels=1,callback=callback):
    
    rec= vosk.KaldiRecognizer(model,samplerate)
    while not stop_flag:
        data = q.get()
        if rec.AcceptWaveform(data):
        #    result =rec.Result()
            result_json = rec.Result()
        #    print(result_json)
  
            result_dict = json.loads(result_json)
            text = result_dict.get("text", "")
            print(result_dict)
            print(type(result_dict))
            if "жучка стоп" in text.lower():
                print("Команда 'stop' получена. Завершение программы.")
                stop_flag = True  
                   
        else:
            partial_json = rec.PartialResult()  # Промежуточный результат в формате JSON
            print(partial_json)    

print("прграмма завершена")            
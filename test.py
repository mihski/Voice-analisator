from pvrecorder import PvRecorder
import pvporcupine
import os
from playsound import playsound
#import app
#import asis

devices = PvRecorder.get_available_devices()
for i, device in enumerate(devices):
    print(f"[{i}] {device}")

KEYWORD_FILE_PATH= "./jarvis_en_windows_v3_0_0.ppn"

if not os.path.exists(KEYWORD_FILE_PATH):
    raise FileNotFoundError(f"Keyword file not found at '{KEYWORD_FILE_PATH}'")
else:
    print("файл найден")

porcupine= pvporcupine.create(access_key="X90Q/wuy7KB5VPHxFtsbGcdPuCaDZdX4Jwp8n0bGfnCXw3syOuRvnA==",                               
                                keywords=["jarvis","alexa"]
                                )

recorder = PvRecorder(device_index= -1 ,frame_length=porcupine.frame_length)
recorder.start()
count=0
try:   
    while True: 
        count+=1
        if count % 100 == 0:
            print(int(count/100), end='',flush=True)       
        voice = recorder.read()        
        keyord_index  = porcupine.process(voice)          
        #print("слушаю")          
        if keyord_index>=0:
            print("погоняло услышано")
            recorder.stop()
            print("мicr. off")
            playsound("./voices/jiglov-moya-familiya.wav")
            recorder.start()
            print("мicr. on")
            continue
      #     asis.main()  
      #        
              
except KeyboardInterrupt:
     print("Stopped by user.")


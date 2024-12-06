import sounddevice as sd
import time
import torch
import num2words



language="ru"
model_id = "v4_ru"
sample_rate =48000
speaker = "baya"
put_accent = True
put_yo = True
text = "привет "
device  = torch.device("cpu")


model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                        model='silero_tts',
                        language=language,
                        speaker=model_id,
                        put_accent=put_accent,
                        put_yo=put_yo)
model.to(device)

def speaker_m(text):
    print("speaker_m вызван")
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,)                        
    print(text)                        

    sd.play(audio, sample_rate* 1.05 )
    time.sleep((len(audio) / sample_rate + 1))
    sd.stop()


# sd.play(audio, sample_rate)
# time.sleep(len(audio) / sample_rate)
# sd.stop()
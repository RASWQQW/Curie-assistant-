import torch
import sounddevice as sd
import time


def Speaker(text):
    ln = 'en'
    model_id = 'v3_en'
    sample_rate = 48000
    speaker = 'en_10'  # en_5 #en_10
    accente = True
    yoo = True
    device = torch.device('cpu')
    text = text

    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=ln,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=accente,
                            put_yo=yoo)


    print(len(audio))
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / (sample_rate / 2.5))
    sd.stop()

# Speaker("Hello friend I am glad to see you again")
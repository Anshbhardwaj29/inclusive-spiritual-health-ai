import whisper
import torch
import os
import sounddevice as sd
import scipy.io.wavfile as wav

os.environ["PATH"] += os.pathsep + r'C:\ffmpeg\bin'

# GPU Force: RTX 3050
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("tiny", device=device)

def listen():
    fs = 16000
    seconds = 5
    filename = "input.wav"
    
    print(f"\n🎤 Listening... ({device}) [Speak now]")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, recording)
    
    # Transcribe directly in English
    result = model.transcribe(filename, language="en")
    user_text = result["text"]
    lang_code = "en"
    
    if os.path.exists(filename):
        os.remove(filename)
        
    return user_text, lang_code
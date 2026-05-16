import pyttsx3

def speak(text, lang_code='en'):
    try:
        engine = pyttsx3.init()
        # Set female voice if available and a comfortable speaking rate
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
            
        engine.setProperty('rate', 170)
        
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Voice Error: {e}")
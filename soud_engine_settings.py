import pyttsx3

def settings_sound():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 165)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
from gtts import gTTS
import playsound
def speak(text, language='en'):
    tts = gTTS(text=text, lang=language)
    filename = 'voice1.mp3'
    tts.save(filename)
    playsound.playsound(filename)

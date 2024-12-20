import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') #to check how much voices in your computer
    engine.setProperty('voice', voices[1].id) #to change voice, initial voice start from 0
    engine.setProperty('rate', 160)
    print(voices)
    engine.say(text)
    engine.runAndWait()
    
def takecommand():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)
        
    try:
        print('recognizing')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'user said: {query}')
    except Exception as e:  
        return ""
    
    return query.lower()

text = takecommand()

speak(text)
    
def recognize_google():
    
    text = sr.recognize_google("", language="en-in")  # 

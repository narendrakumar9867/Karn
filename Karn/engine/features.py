from playsound import playsound
import eel


eel.expose
def playAssistantsound():
    music_dic = "www\\assest\\audio\\start_sound.mp3"
    playsound(music_dic)
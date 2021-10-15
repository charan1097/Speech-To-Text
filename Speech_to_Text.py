from gtts import gTTS
from playsound import playsound
audio ='speech.mp3'
language = 'en'
name = input()
sp = gTTS(text ="How Are you "+name,lang = language,slow = False)
sp.save(audio)
playsound(audio)

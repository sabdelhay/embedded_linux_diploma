#!/usr/bin/python3

from gtts import gTTS
import vlc

#vlc_instance = vlc.Instance()

voice = gTTS(text="Good morning Sir, how can I help you?", lang='en', slow=False)

voice.save("welcome.mp3")

p = vlc.MediaPlayer("./welcome.mp3")
p.play()

while True:
    pass
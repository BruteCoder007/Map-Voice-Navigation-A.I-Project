from gtts import gTTS
import os
from speech_to_text import speech_recognition
def textToSpeech(myText):
    language="en"
    output=gTTS(text=myText,lang=language,slow=True)
    output.save("output.mp3")
    os.system("start output.mp3")
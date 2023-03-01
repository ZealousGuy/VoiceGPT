# Note - Before Running, change the api key ''on line 24'' with your own API key
# Here's how to find your Key : https://www.educative.io/answers/how-to-get-api-key-of-gpt-3
def getPromptFromMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))
    forwardPromptToOpenAI(text)

def getPromptFromInput():
    text=input("Write you Prompt here:- ")
    forwardPromptToOpenAI(text)

def forwardPromptToOpenAI(text):
    #Change this to your own API key 
    # How to get your API key? -> https://www.educative.io/answers/how-to-get-api-key-of-gpt-3
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-002",
        # Prompt Here
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(response["choices"][0]["text"])
    convertTextToSpeech(response)

def convertTextToSpeech(response):
    mytext =response["choices"][0]["text"]
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    # os.system("mpg321 welcome.mp3")
    # os.system("start welcome.mp3")

    filename = 'file://' + os.path.abspath("welcome.mp3")
    webbrowser.open(filename)


import openai
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import os
mic=int(input("Do you have a mic? Type '0' if NoMic else '1' :- "))
if mic==0:
    getPromptFromInput()
else:
    getPromptFromMic()
#END
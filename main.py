import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sp_to_text():
    recognizer = sr.Recognizer()
    with  sr.Microphone() as source:
        print('Listening.....')
        recognizer.adjust_for_ambient_noise(source=source)
        audio = recognizer.listen(source)
        try:
            print('Recognizing....') 
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print('Not Understand !! ')


sp_to_text()


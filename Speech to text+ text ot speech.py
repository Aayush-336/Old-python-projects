import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def speak(command):
    eng = pyttsx3.init()
    eng.say(command)
    eng.runAndWait()


# while 1:
try:
    with sr.AudioFile("test1.wav") as source2:
        # r.adjust_for_ambient_noise(source2,duration=1)
        audio2 = r.listen(source2)
        text = r.recognize_google(audio2)
        text = text.lower()
        print("Did you say :" + text)
        speak(text)
except sr.RequestError as e:
    print(f"Couldn't request result : {0}".format(e))
except sr.UnknownValueError:
    print("Unknown error")

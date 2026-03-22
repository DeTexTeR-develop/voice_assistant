import speech_recognition as sr
import webbrowser as wb
import pyttsx3

recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Aurr bhaijii kyaaa scene...")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Voice Assitant Working!")
        audio = r.listen(source, timeout=2)

    # recognize speech using Sphinx
    print("recognizing")
    try:
        command = r.recognize_google(audio)
        print(command)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))



import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import music 

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def execute_command(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in command:
        speak("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com/feed/")

    elif "open chat gpt" in command:
        speak("Opening Chat GPT")
        webbrowser.open("https://chatgpt.com/")

    elif "play music" in command:
        speak("what song you want to play?")
        print("what song you want to play? ")
        audio = r.listen(source)
        language = r.recognize_google(audio).lower()
        print(f"you choose {language}")
        if "english" in language:
            webbrowser.open(music.songs["english"])
        elif "hindi" in language: 
            webbrowser.open(music.songs["hindi"])
        elif "bairan" or "barrem" in language:
            webbrowser.open(music.songs["bairan"])
        else:
            print("failed to recognize")


if __name__ == "__main__":
    speak("Aurr bhaijii kyaaa scene...")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  #improves accuracy
        print("Voice Assistant Working!")

        while True:
            try:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=5)
                print("Recognizing...")
                command = r.recognize_google(audio)
                print("You said:", command)

                # exit condition
                if any(word in command.lower() for word in ["exit", "stop", "quit"]):
                    speak("Goodbye")
                    time.sleep(1)
                    break

                # always execute command
                execute_command(command)

            except sr.WaitTimeoutError:
                print("No speech detected")
            
            except sr.UnknownValueError:
                print("Could not understand audio")
            
            except sr.RequestError as e:
                print(f"Error: {e}")
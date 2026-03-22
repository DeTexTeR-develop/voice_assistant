import speech_recognition as sr
import pyttsx3
import time

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Aurr bhaijii kyaaa scene...")

    with sr.Microphone() as source:
        print("Voice Assistant Working!")

        while True:
            try:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=5)

                print("Recognizing...")
                command = r.recognize_google(audio)
                print("You said:", command)

                # exit condition
                if command.lower() in ["exit", "stop", "quit"]:
                    speak("Goodbye")
                    time.sleep(1)
                    break

            except sr.WaitTimeoutError:
                print("No speech detected")
            
            except sr.UnknownValueError:
                print("Could not understand audio")
            
            except sr.RequestError as e:
                print(f"Error: {e}")
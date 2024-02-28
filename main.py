import pyttsx3
import speech_recognition as sr


class SpeechAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Please speak...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Sorry, I couldn't understand what you said."
            except sr.RequestError:
                return "Sorry, there was an issue with the speech recognition service."


if __name__ == "__main__":
    assistant = SpeechAssistant()
    assistant.speak("Hello there! How are you?")
    recognized_text = assistant.recognize_speech()
    print("You said:", recognized_text)


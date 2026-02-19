import speech_recognition as sr
import pyttsx3
from time import ctime
import webbrowser
import wikipedia
from tkinter import *

r = sr.Recognizer()
speaker = pyttsx3.init()


class VirtualAssistant:
    def __init__(self):
        self.root = Tk()
        self.root.title('Storm - Virtual Assistant')
        self.root.geometry('520x320')

        self.userText = StringVar()
        self.userText.set('Hello! I am Storm 🤖')

        frame = LabelFrame(self.root, text='Storm', font=('Railways', 24, 'bold'))
        frame.pack(fill='both', expand=True)

        self.message = Message(
            frame, textvariable=self.userText,
            bg='black', fg='white', width=480
        )
        self.message.config(font=("Century Gothic", 15, 'bold'))
        self.message.pack(fill='both', expand=True)

        Button(
            self.root, text='🎤 Speak',
            font=('railways', 10, 'bold'),
            bg='red', fg='white',
            command=self.clicked
        ).pack(fill='x')

        Button(
            self.root, text='❌ Close',
            font=('railways', 10, 'bold'),
            bg='yellow', fg='black',
            command=self.root.destroy
        ).pack(fill='x')

        self.speak('How can I help you?')
        self.root.mainloop()

    def speak(self, text):
        self.userText.set(text)
        speaker.say(text)
        speaker.runAndWait()

    def record_audio(self, prompt=None):
        with sr.Microphone() as source:
            if prompt:
                self.speak(prompt)
            try:
                audio = r.listen(source)
                return r.recognize_google(audio).lower()
            except sr.UnknownValueError:
                return ""
            except Exception:
                self.speak("Microphone error.")
                return ""

    def clicked(self):
        command = self.record_audio()

        if not command:
            self.speak("I didn't catch that. Please try again.")
            return

        if 'who are you' in command:
            self.speak('I am Storm, your virtual assistant.')

        elif 'search' in command:
            query = self.record_audio('What should I search for?')
            webbrowser.open(f'https://google.com/search?q={query}')
            self.speak(f'Here is what I found for {query}')

        elif 'open youtube' in command:
            webbrowser.open('https://www.youtube.com')
            self.speak('Opening YouTube')

        elif 'youtube channel' in command:
            channel = self.record_audio('Which channel?')
            webbrowser.open(
                f'https://www.youtube.com/results?search_query={channel.replace(" ", "+")}'
            )
            self.speak(f'Searching YouTube for {channel}')

        elif 'wikipedia' in command:
            topic = self.record_audio('What topic?')
            try:
                summary = wikipedia.summary(topic, sentences=2)
                self.speak(summary)
            except:
                self.speak("Sorry, I couldn't find that on Wikipedia.")

        elif 'location' in command:
            location = self.record_audio('Which location?')
            webbrowser.open(f'https://www.google.com/maps/place/{location}')
            self.speak(f'Here is the location of {location}')

        elif 'time' in command:
            self.speak(f'The current time is {ctime()}')

        elif 'exit' in command or 'quit' in command:
            self.speak('Goodbye!')
            self.root.destroy()

        else:
            self.speak("Sorry, I don't understand that yet.")


if __name__ == '__main__':
    VirtualAssistant()

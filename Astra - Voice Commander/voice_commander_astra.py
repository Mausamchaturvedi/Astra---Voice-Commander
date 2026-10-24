import time
from datetime import datetime


def safe_init_tts():
    try:
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        return engine
    except Exception as exc:
        print('TTS init failed:', exc)

        class _DummyVoice:
            def __init__(self, id='default'):
                self.id = id

        class _DummyEngine:
            def __init__(self):
                self._voices = [_DummyVoice()]
                self._props = {'rate': 170, 'voice': self._voices[0].id}

            def init(self):
                return self

            def getProperty(self, name):
                if name == 'voices':
                    return self._voices
                return self._props.get(name)

            def setProperty(self, name, value):
                self._props[name] = value

            def say(self, text):
                print('[TTS-FALLBACK]', text)

            def runAndWait(self):
                pass

        return _DummyEngine()


def speak(engine, text):
    print('Speaking:', text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as exc:
        print('TTS speak failed:', exc, text)


engine = safe_init_tts()

hour = datetime.now().hour

if hour < 12:
    greeting = "Good Morning, and welcome back sir!"
elif hour < 17:
    greeting = "Good Afternoon, and welcome back sir!"
else:
    greeting = "Good Evening, and welcome back sir!"

now = datetime.now().strftime("%I:%M %p")
today = datetime.now().strftime("%A, %d %B %Y")

print("Today is", today)
print("The time is", now)

full_message = (
    f"{greeting} "
    "I hope you have a wonderful day. "
    f"Today is {today}. "
    f"The time is {now}."
)

speak(engine, full_message)

time.sleep(0.5)
import pyttsx3 as tts
from datetime import datetime as d

t = d.now()
h = t.hour

engine = tts.init()

if h < 12:
    engine.say('Good Morning.')
    engine.runAndWait()
elif 12 < h < 17:
    engine.say('Good Afternoon.')
    engine.runAndWait()
elif 17 < h < 21:
    engine.say('Good Evening.')
    engine.runAndWait()
else:
    engine.say('Good Night.')
    engine.runAndWait()


def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


def sort(*args):
    items = map(int, args)
    return list(sorted(items))

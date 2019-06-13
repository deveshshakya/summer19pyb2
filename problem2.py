from googlesearch import search
import speech_recognition as sr

def topic_search(topic):
    url = []
    for i in search(topic, stop=10):
        url.append(i)
    with open('Links.txt', 'w') as f:
        for i in url:
            f.write(i)
            f.write('\n')
    print('\nResult:')
    print(*url, sep='\n')

if __name__ == "__main__":
    print('Input method:\n1. Text\n2. Speech\n')
    choice = input()

    if choice is '1':
        topic = input("Enter topic: ")
        topic_search(topic)
        
    if choice is '2':
        print("Speech topic: ")
        try:
            r = sr.Recognizer()
            mic = sr.Microphone()
        
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=2)
                topic = r.listen(source)
            topic_search(r.recognize_google(topic))
        except sr.UnknownValueError:
            print('Error occured.')
    else:
        print('Wrong choice.')
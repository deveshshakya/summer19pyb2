import os
import shlex, subprocess
from gtts import gTTS 

text = 'Command was previously given, not do this again.'
obj = gTTS(text=text, lang='en', slow=False)
obj.save("audio.mp3")

cmds = []

while True:
    bashCommand = input("Enter: ")
    try:
        if bashCommand in cmds:
            os.system("mpg321 audio.mp3")
            continue
        cmds.append(bashCommand)
        with open('commands.txt', 'a') as f:
            f.write(bashCommand)
            f.write('\n')
        process = subprocess.Popen(shlex.split(bashCommand), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, error = process.communicate()
        print(output.decode('utf-8'))
    except FileNotFoundError:
        os.system(bashCommand)
        print()
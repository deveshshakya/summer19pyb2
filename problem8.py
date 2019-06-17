import os
import shlex, subprocess
import pyttsx3

cmds = []

while True:
    bashCommand = input("Enter: ")
    try:
        if bashCommand in cmds:
            engine = pyttsx3.init()
            engine.say("Command was previously given, not do this again.")
            engine.runAndWait()
            engine.stop()
            continue
        cmds.append(bashCommand)
        with open('commands.txt', 'a') as f:
            f.write(bashCommand)
            f.write('\n')
        process = subprocess.Popen(shlex.split(bashCommand), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, error = process.communicate()
        print(output.decode('utf-8'))
    except Exception:
        os.system(bashCommand)
print()
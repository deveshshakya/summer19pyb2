import os, sys
import time

"""
Usage: argv[0] [OPTIONS] [FILE]
-n, --number             number all output lines
-E, --show-ends          display $ at end of each line
-T, --show-tabs          display TAB characters as ^I    
"""


print(len(sys.argv))

if len(sys.argv) == 2:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], 'r') as file:
            print(file.read())
    else:
        print("File doesn't exist.")

else:
    if sys.argv[1] == '-n':
        with open(sys.argv[2], 'r') as file:
            if len(file.read()) == 0:
                print(file.read())
            else:
                t = 1
                file.seek(0)
                print(str(t), end=' ')
                for i in file.read():
                    if i == '\n':
                        t = t + 1
                        print()
                        print(str(t), end=' ')
                    else:
                        print(i, end='')
    elif sys.argv[1] == '-E':
        with open(sys.argv[2], 'r') as file:
            if len(file.read()) == 0:
                print(file.read())
            else:
                t = 1
                file.seek(0)
                for i in file.read():
                    if i == '\n':
                        print('$')
                    else:
                        print(i, end='')
    elif sys.argv[1] == '-t':
        with open(sys.argv[2], 'r') as file:
            if len(file.read()) == 0:
                print(file.read())
            else:
                t = 1
                file.seek(0)
                for i in file.read():
                    if i == '\t':
                        print('^I', end='')
                    else:
                        print(i, end='')

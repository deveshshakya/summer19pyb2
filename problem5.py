from datetime import datetime as d

user = input("Enter name: ")

t = d.now()
h = t.hour

if h < 12:
    print('Good Morning ' + user + '.')
elif 12 < h < 17:
    print('Good Afternoon ' + user + '.')
elif 17 < h < 21:
    print('Good Evening ' + user + '.')
else:
    print('Good Night ' + user + '.')

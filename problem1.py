import datetime

a, b = input("Enter your name and age: ").split()
print("Hey {}, You'll turn 95 in ".format(a) + str(datetime.date.today().year + 95 - int(b)) + '.')

# this program should be run from root.
import os

username = input("Enter username: ")

if username.isalpha():
    password = 'hello' + username
    os.system('sudo useradd -p $(openssl passwd -1 {}) {}'.format(password, username))
    print('User created.')
else:
    print('Username must contain only alphabets.')

import socket
import os

recv_ip = "localhost"
recv_port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((recv_ip, recv_port))


t = input("1. Text Messages\n2. File Sending\n3. Exit\n")
if t is '1':
    message = input('Message (exit for close): ')
    if message == 'exit':
        s.close()
        exit(0)
    s.sendto(message.encode(), (recv_ip, recv_port))
    bytes, address = s.recvfrom(255)
    print("Reply from Recv: " + str(bytes.decode()) + "\n")
    s.close()
elif t is '2':
    path = input('Enter file path: ')
    try:
        if os.path.exists(path):
            with open(path, 'rb') as f:
                packet = f.read(1024)
                while packet:
                    s.send(packet)
                    packet = f.read(1024)
    except FileNotFoundeError:
        print('File Path is not correct.\n')
    s.close()
else:
    s.close()
    exit(0)

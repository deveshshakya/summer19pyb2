import socket

recv_ip = "127.0.0.1"
recv_port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((recv_ip, recv_port))

while True:
    data = s.recvfrom(255)
    print("Message: " + str(data[0]) + "\nIP: " + str(data[1]))
    s.sendto("Got it.", data[1])

s.close()

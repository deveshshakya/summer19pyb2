import socket

recv_ip = "127.0.0.1"
recv_port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = raw_input()
    s.sendto(msg, (recv_ip, recv_port))
    reply = s.recvfrom(255)
    print("Reply from Recv: " + str(reply[0]))

s.close()

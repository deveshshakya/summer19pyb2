import socket

recv_ip = "172.17.0.2"
recv_port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input('Message (exit for close): ')
    if len(message) > 150:
        print("Length must not exceed 150 character.")
        continue
    if message == 'exit':
        s.close()
        exit(0)
    s.sendto(message.encode(), (recv_ip, recv_port))
    reply = s.recvfrom(255)
    if reply == 'exit' or reply == 'Exit':
        s.close()
        exit(0)
    print("Reply from Recv: " + str(reply[0].decode()))
s.close()

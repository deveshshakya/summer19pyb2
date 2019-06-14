import socket

recv_ip = "172.17.0.2"
recv_port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((recv_ip, recv_port))

while True:
    data = s.recvfrom(255)
    print("Message: " + str(data[0].decode()) + "\nIP: " + str(data[1].decode()))
    reply = input('Reply (exit for close): ')
    if len(reply) > 150:
        print("Length must not exceed 150 character.")
        continue
    if reply == 'exit':
        s.close()
        exit(0)
    s.sendto(reply.encode(), data[1])
s.close()

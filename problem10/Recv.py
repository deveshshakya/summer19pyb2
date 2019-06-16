import socket
import time

def recieve_file(filename, conn):
    with open(filename, 'wb') as f:
        packet, address = conn.recvfrom(1024)
        while packet:
            f.write(packet)
            packet = conn.recvfrom(1024)
    conn.close()

if __name__ == "__main__":
    recv_ip = "localhost"
    recv_port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((recv_ip, recv_port))
    s.connect((recv_ip, recv_port))

    t = input("1. Text Messages\n2. File Sending\n3. Exit\n")
    if t is '1':
        bytes, address = s.recvfrom(255)
        print("Message Recieved: " + str(bytes.decode()))
        reply = input('\nReply: ')
        s.sendto(reply.encode(), address)
        s.close()
    elif t is '2':
        time.sleep(1)
        conn, address = s.accept()
        i = 0
        recieve_file('file_'+ str(i), conn)
        i = i + 1
        print('File Recieved.\n')
        s.close()
    else:
        print('Enter correct choice.')
        s.close()

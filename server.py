import socket
import time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))


Exit = False
print("Server Started")

while not Exit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        currentTime = time.strftime("Data: %d.%m.%Y Time: %H:%M:%S", time.localtime())

        print("[" + addr[0] + "] [" + str(addr[1]) + "] [" + currentTime + "] ", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print("\n Server Stopped")
        Exit = True

s.close()



import socket, threading, time

shutdown = False
join = False


def receving(self, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))

                time.sleep(0.2)
        except:
            pass


host = "192.168.56.1"
port = 0

server = (host, 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

username = input("Name: ")

T = threading.Thread(target=receving, args=("RecvThread", s))
T.start()


while shutdown == False:
    if join == False:
        s.sendto(("[" + username + "] :: join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            if message != "":
                s.sendto(("[" + username + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + username + "] :: left chat ").encode("utf-8"), server)
            shutdown = True

T.join()
s.close()



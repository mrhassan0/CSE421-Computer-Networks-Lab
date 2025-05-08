import socket

FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MSG = "TERMINATED"

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1461

ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


msg = f"The HOSTNAME of client is {socket.gethostname()} and IP is {SERVER}"
send(msg)
send(DISCONNECT_MSG)

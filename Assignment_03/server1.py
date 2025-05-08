import socket

FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MSG = "TERMINATED"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1461
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print("SERVER IS STARTING")

server.listen()
print("SERVER IS LISTENING", SERVER)

while True:
    conn, addr = server.accept()
    print("CONNECTED TO ", addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
                print(f"Terminating the connection with {addr}")
                conn.send("CONNECTION CLOSED".encode(FORMAT))
            else:
                print(msg)
                conn.send("MESSAGE RECEIVED".encode(FORMAT))
    conn.close()

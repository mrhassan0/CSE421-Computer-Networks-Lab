import socket
import threading

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

def count_vowels(msg):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in msg:
        if char in vowels:
            count += 1
    return count

def handler(conn, addr):
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
                conn.send("CONNECTION TERMINATED".encode(FORMAT))
            else:
                vowel_count = count_vowels(msg)
                if vowel_count == 0:
                    conn.send("Not enough vowels".encode(FORMAT))
                elif vowel_count > 2:
                    conn.send("Too many vowels".encode(FORMAT))
                else:
                    conn.send("Enough vowels I guess".encode(FORMAT))
    conn.close()

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handler, args=(conn, addr))
    thread.start()

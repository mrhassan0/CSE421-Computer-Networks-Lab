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


def calculate_payment(hours_worked):
    if hours_worked > 40:
        return (40 * 200) + ((hours_worked - 40) * 300)
    return hours_worked * 200


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
                conn.send("CONNECTION TERMINATED".encode(FORMAT))
            else:
                salary = calculate_payment(int(msg))
                conn.send(f"Salary of this employee is: {salary}".encode(FORMAT))
    conn.close()

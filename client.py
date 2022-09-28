from email import message
import socket

HOST = socket.gethostname()
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        msg = s.recv(100)
        print(msg.decode("utf-8"))

        send_message = input('Client:')
        s.send(bytes(send_message, "utf=8"))

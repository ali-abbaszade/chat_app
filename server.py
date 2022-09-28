from email import message
import socket

HOST = socket.gethostname()
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    client, address = s.accept()
    print(f"Client is connected and has the address {address}")

    while True:
        message = input("Server:")
        client.send(
            bytes(message, "utf-8"))
        rec_msg = client.recv(100)
        print(rec_msg.decode("utf-8"))

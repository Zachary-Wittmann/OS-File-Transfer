#! /usr/bin/env python3

import socket, sys, re, time

def receive_file(connection, filename):
    with open(filename, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data or data == b'EOF':
                break
            file.write(data)

def frame_and_send_ack(connection, ack_message):
    ack_message = ack_message.encode()
    connection.sendall(ack_message)

def main():
    host = '127.0.0.1'
    port = 50000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)

    print(f"Server is listening on {host}:{port}")

    connection, address = server_socket.accept()
    print(f"Connection from {address}")

    received_filename = connection.recv(1024).decode()
    print(f"Receiving file: {received_filename}")

    receive_file(connection, received_filename)
    print("File has been successfully received.")

    ack_message = "Successfully received. Acknowledgement sent"
    frame_and_send_ack(connection, ack_message)
    print("Acknowledgement sent")

    connection.close()
    server_socket.close()

if __name__ == "__main__":
    main()

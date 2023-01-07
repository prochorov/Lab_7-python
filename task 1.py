import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
groupmates = {
    "Иванов": "Иван",
    "Петров": "Петр",
    "Прохоров": "Артем"
}
while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    message = request.strip().split('\n')[-1].strip()
    if message in groupmates.keys():
        bytesToSend = str.encode(f"Привет, {groupmates[message]}")
    else:
        bytesToSend = str.encode("Такого пользователя нет в нашей группе! Изыди демон!")
    client_connection.sendall(bytesToSend)
    client_connection.close()
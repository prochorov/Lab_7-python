import socket

localIP = "127.0.0.1"
localPort = 33333
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
groupmates = {
    "Иванов": "Иван",
    "Петров": "Петр",
    "Прохоров": "Артем"
}
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode('UTF-8').strip()
    address = bytesAddressPair[1]
    if message in groupmates.keys():
        bytesToSend = str.encode(f"Привет, {groupmates[message]}")
    else:
        bytesToSend = str.encode("Такого пользователя нет в нашей группе! Изыди демон!\nВведите фамилию пользователя: ")
    UDPServerSocket.sendto(bytesToSend, address)

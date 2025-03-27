from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
 message, clientAddress = serverSocket.recvfrom(2048)
 if message.decode() != "":
    print("Receive: " + message.decode() + "\n")
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("Replied\n")

import socket
import threading

ip = "localhost"
port = 1234


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 and TCP

server.bind((ip, port))
server.listen(1)  # the number of unaccepted connections that the system will allow before refusing new connections 
print("Listening....")

def client_handler(client_socket):
    request = client_socket.recv(2048).decode()
    print("Receicved message: " + str(request))
    client_socket.send("Received message".encode())
    client_socket.close()

while True:
    client, address = server.accept()
    serv_client = threading.Thread(target=client_handler, args=(client,))
    serv_client.append()
    serv_client.start()


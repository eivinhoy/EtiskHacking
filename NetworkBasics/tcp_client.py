import socket


target_host = "localhost"
target_port = 1234


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 and TCP
client.connect((target_host, target_port))

try:
    message = "This is socket programming"
    client.send(message.encode())
    response = client.recv(2048)
    print("Response from server: " + str(response))
finally:
    client.close()
    print("TCP connection closed")


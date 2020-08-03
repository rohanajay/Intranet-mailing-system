from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = ''
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        addresses[client] = client_address
        username = client.recv(BUFSIZ).decode("utf8")
        clients[client]=username
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  # Takes client socket as argument.
	"""Handles a single client connection."""
	r_packet = client.recv(BUFSIZ).decode("utf8")
	ar_packet = r_packet
	r_packet = r_packet.split("~")

	for sock in clients:
		if(clients[sock] == r_packet[0]):
			sock.send(bytes(ar_packet,"utf8"))

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()

SERVER.close()

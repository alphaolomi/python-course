import socket
import threading

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('127.0.0.1', 12345)

# Bind the server socket to the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print("Chat server is listening on", server_address)

# List to store connected clients
connected_clients = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in connected_clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send message
                remove_client(client)

# Function to remove a client from the list
def remove_client(client_socket):
    if client_socket in connected_clients:
        connected_clients.remove(client_socket)

# Function to handle a client's connection
def client_handler(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
                broadcast(message, client_socket)
            else:
                # Remove the client if no data received
                remove_client(client_socket)
        except:
            continue

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    connected_clients.append(client_socket)
    print(f"Connected to {client_address}")
    # Create a thread to handle the client
    client_thread = threading.Thread(target=client_handler, args=(client_socket,))
    client_thread.start()

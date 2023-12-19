import socket
import threading

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('127.0.0.1', 12345)

# Connect to the server
client_socket.connect(server_address)

# Function to receive and display messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
        except:
            print("Connection to server lost.")
            client_socket.close()
            break

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))

import socket

def start_server():
    # 1. Create a socket object (IPv4, TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind the socket to an address and port
    host = '127.0.0.1'  # Localhost
    port = 12345        # Make sure this port is not in use
    server_socket.bind((host, port))
    
    # 3. Listen for incoming connections (max 1 queued connection)
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}...")
    
    # 4. Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to client at {client_address}")
    
    # 5. Receive data from the client (up to 1024 bytes)
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Client says: {message}")
    
    # 6. Send a response back to the client
    response = "Message received loud and clear!"
    client_socket.send(response.encode('utf-8'))
    
    # 7. Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
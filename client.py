import socket

def start_client():
    # 1. Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Connect to the server
    host = '127.0.0.1'
    port = 12345
    
    print(f"Connecting to server at {host}:{port}...")
    client_socket.connect((host, port))
    
    # 3. Send data to the server
    message = "Hello, Server! I am the client."
    client_socket.send(message.encode('utf-8'))
    
    # 4. Receive the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server replied: {response}")
    
    # 5. Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
import socket
import ssl
import threading

# Server Configuration
VPN_HOST = '0.0.0.0'  # Listen on all available interfaces
VPN_PORT = 8888       # Port for the VPN server

# Buffer size for data transfer
BUFFER_SIZE = 4096

# Target server (replace with the server you want to forward traffic to)
TARGET_HOST = 'example.com'  # Example target server
TARGET_PORT = 80             # Example target port

def handle_client(client_socket):
    """Handles the client's connection and forwards traffic to the target server."""
    try:
        # Wrap the client socket with SSL for encryption
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        client_conn = context.wrap_socket(client_socket, server_side=True)

        # Connect to the target server
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((TARGET_HOST, TARGET_PORT))

        # Forward data between client and target server
        while True:
            # Receive data from client
            client_data = client_conn.recv(BUFFER_SIZE)
            if not client_data:
                break

            # Send data to target server
            target_socket.sendall(client_data)

            # Receive response from target server
            target_data = target_socket.recv(BUFFER_SIZE)
            if not target_data:
                break

            # Send response back to client
            client_conn.sendall(target_data)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()
        target_socket.close()

def start_vpn_server():
    """Starts the VPN server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((VPN_HOST, VPN_PORT))
    server_socket.listen(5)
    print(f"VPN server started on {VPN_HOST}:{VPN_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    try:
        start_vpn_server()
    except KeyboardInterrupt:
        print("\nShutting down the VPN server...")
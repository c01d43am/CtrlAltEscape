import socket
import threading
import random

# List of proxy servers (host, port)
PROXIES = [
    ('proxy1.example.com', 8080),
    ('proxy2.example.com', 8080),
    ('proxy3.example.com', 8080),
]

# Buffer size for data transfer
BUFFER_SIZE = 4096

# VPN Server Configuration
VPN_HOST = '0.0.0.0'
VPN_PORT = 8888

def forward_traffic(source_socket, destination_socket):
    """Forward traffic between two sockets."""
    try:
        while True:
            data = source_socket.recv(BUFFER_SIZE)
            if not data:
                break
            destination_socket.sendall(data)
    except Exception as e:
        print(f"Error in forwarding traffic: {e}")
    finally:
        source_socket.close()
        destination_socket.close()

def handle_client(client_socket):
    """Handles client connections and routes traffic through a random proxy chain."""
    try:
        # Randomly shuffle the proxies
        random_proxies = random.sample(PROXIES, len(PROXIES))

        # Create a socket chain through the proxies
        current_socket = client_socket
        for proxy_host, proxy_port in random_proxies:
            proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_socket.connect((proxy_host, proxy_port))
            print(f"Connected to proxy: {proxy_host}:{proxy_port}")

            # Forward traffic between the current socket and the proxy
            threading.Thread(target=forward_traffic, args=(current_socket, proxy_socket)).start()
            current_socket = proxy_socket

        # Finally, route traffic to the destination (example target server)
        target_host = 'example.com'
        target_port = 80
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((target_host, target_port))
        print(f"Connected to target server: {target_host}:{target_port}")

        # Forward traffic between the last proxy and the target server
        threading.Thread(target=forward_traffic, args=(current_socket, target_socket)).start()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

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
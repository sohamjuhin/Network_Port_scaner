import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()

# Example usage
target_ip = "127.0.0.1"  # Replace with the IP address or hostname of the target
start_port = 1
end_port = 100  # Specify the range of ports to scan

scan_ports(target_ip, start_port, end_port)

#PORTSCAN USING PYTHON 
import socket

def port_scanner(target_ip, ports):
    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    ports = input("Enter the ports to scan (comma-separated): ").split(',')
    ports = [int(port.strip()) for port in ports]

    open_ports = port_scanner(target_ip, ports)

    print(f"Open ports on {target_ip}: {open_ports}")

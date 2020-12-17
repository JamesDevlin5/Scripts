import socket
import argparse

parser = argparse.ArgumentParser(
    description="Scans all the ports on the target host to determine if any are open."
)
parser.add_argument("target", help="The host to scan all ports of.")
args = parser.parse_args()

try:
    ports = []
    for port in range(1, 65535):
        socket.setdefaulttimeout(1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((args.target, port)):
                print(f"open port:\t{port}")
                ports.append(port)
except KeyboardInterrupt:
    print("Exiting Program...")
    exit(1)
except socket.gaierror:
    print("Hostname could not be resolved!")
    exit(1)
except socket.error:
    print("Server not responding!")
    exit(1)

import socket
from concurrent.futures import ThreadPoolExecutor

open_ports = []


def scan_port(target_ip, port):
    global open_ports

    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((target_ip, port))
        print(f"[OPEN] Port {port}")
        open_ports.append(port)
    except:
        pass

    s.close()


def scan_ports(target, ports):
    global open_ports
    open_ports = []

    print(f"\n[+] Scanning target: {target}\n")

    # Resolve domain to IP
    try:
        target_ip = socket.gethostbyname(target)
        print(f"[~] Resolved IP: {target_ip}\n")
    except socket.gaierror:
        print("[ERROR] Could not resolve target\n")
        return

    # Run scan
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda port: scan_port(target_ip, port), ports)

    # Show results
    print("\n[+] Scan Results")
    print("-" * 25)

    if open_ports:
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found")

    print("\n[✔] Scan Complete\n")

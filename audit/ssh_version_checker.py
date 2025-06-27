import socket

def get_ssh_banner(host, port=22, timeout=5):
    """
    Connect to an SSH server and retrieve its banner (version info).
    """
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            banner = sock.recv(1024).decode().strip()
            return banner
    except socket.timeout:
        return "[!] Connection timed out."
    except Exception as e:
        return f"[!] Error: {e}"

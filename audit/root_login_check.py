
def check_root_login(sshd_config_path="/etc/ssh/sshd_config"):
    """
    Parse the sshd_config file to check if root login is allowed.
    Returns: string ("yes", "no", "prohibit-password", "not found", etc.)
    """
    try:
        with open(sshd_config_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("PermitRootLogin"):
                    value = line.split()[1].lower()
                    return value
        return "[!] PermitRootLogin directive not found."
    except FileNotFoundError:
        return "[!] sshd_config file not found."
    except Exception as e:
        return f"[!] Error: {e}"

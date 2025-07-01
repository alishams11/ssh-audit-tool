import os
import stat
import base64

def check_key_permissions(path):
    """
    Check that the authorized_keys file has secure permissions (600)
    """
    try:
        st = os.stat(path)
        if oct(st.st_mode)[-3:] != "600":
            return f"[!] Warning: File permission is {oct(st.st_mode)[-3:]}, expected 600"
        return "[+] Permissions are secure (600)"
    except FileNotFoundError:
        return "[!] authorized_keys file not found."
    except Exception as e:
        return f"[!] Error: {e}"


def check_keys(path):
    """
    Check each key in authorized_keys for type and approximate strength.
    """
    try:
        with open(path, 'r') as f:
            lines = f.readlines()

        if not lines:
            return "[!] No keys found in authorized_keys."

        warnings = []
        for i, line in enumerate(lines, start=1):
            if line.startswith("ssh-dss"):
                warnings.append(f"[!] Key #{i}: DSA keys are weak (ssh-dss)")
            elif line.startswith("ssh-rsa"):
                try:
                    key_parts = line.strip().split()
                    key_data = base64.b64decode(key_parts[1] + "==")
                    key_len = len(key_data) * 8
                    if key_len < 2048:
                        warnings.append(f"[!] Key #{i}: RSA key appears short (<2048 bits)")
                except Exception:
                    warnings.append(f"[!] Key #{i}: Unable to analyze key size.")

        return warnings if warnings else "[+] All keys seem strong."
    except FileNotFoundError:
        return "[!] authorized_keys file not found."
    except Exception as e:
        return f"[!] Error: {e}"

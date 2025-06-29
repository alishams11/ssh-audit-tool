import os
from audit.ssh_version_checker import get_ssh_banner
from audit.root_login_check import check_root_login
from audit.key_audit import check_key_permissions, check_keys


def main():
    print("=== SSH Audit Tool ===")
    host = input("Enter target IP or hostname: ").strip()
    banner = get_ssh_banner(host)
    print(f"[+] SSH Banner: {banner}")
    
    root_login_status = check_root_login()
    print(f"[+] Root login permission: {root_login_status}")

    key_file = os.path.expanduser("~/.ssh/authorized_keys")
    print(check_key_permissions(key_file))
    key_check = check_keys(key_file)
    if isinstance(key_check, list):
        for warning in key_check:
            print(warning)
    else:
        print(key_check)

if __name__ == "__main__":
    main()

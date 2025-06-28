from audit.ssh_version_checker import get_ssh_banner
from audit.root_login_check import check_root_login


def main():
    print("=== SSH Audit Tool ===")
    host = input("Enter target IP or hostname: ").strip()
    banner = get_ssh_banner(host)
    print(f"[+] SSH Banner: {banner}")
    
    root_login_status = check_root_login()
    print(f"[+] Root login permission: {root_login_status}")

if __name__ == "__main__":
    main()

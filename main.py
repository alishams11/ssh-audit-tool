from audit.ssh_version_checker import get_ssh_banner


def main():
    print("=== SSH Audit Tool ===")
    host = input("Enter target IP or hostname: ").strip()
    banner = get_ssh_banner(host)
    print(f"[+] SSH Banner: {banner}")
    

if __name__ == "__main__":
    main()

import os
import json
from datetime import datetime
from audit.ssh_version_checker import get_ssh_banner
from audit.root_login_check import check_root_login
from audit.key_audit import check_key_permissions, check_keys

def save_report(report, output_path="outputs/report.json"):
    """
    Save the audit report as JSON.
    """
    try:
        with open(output_path, "w") as f:
            json.dump(report, f, indent=4)
        print(f"[+] Report saved to {output_path}")
    except Exception as e:
        print(f"[!] Failed to save report: {e}")


def main():
    print("=== SSH Audit Tool ===")
    host = input("Enter target IP or hostname: ").strip()
    banner = get_ssh_banner(host)
    print(f"[+] SSH Banner: {banner}")
    
    root_login_status = check_root_login()
    print(f"[+] Root login permission: {root_login_status}")

    key_file = os.path.expanduser("~/.ssh/authorized_keys")
    perm_status = check_key_permissions(key_file)
    print(perm_status)

    print(check_key_permissions(key_file))
    key_check = check_keys(key_file)

    if isinstance(key_check, list):
        for warning in key_check:
            print(warning)
    else:
        print(key_check)

    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target": host,
        "ssh_banner": banner,
        "root_login": root_login_status,
        "permission_issue": perm_status,
        "key_issues": key_check if isinstance(key_check, list) else [key_check]
    }
    
    save_report(report)

if __name__ == "__main__":
    main()

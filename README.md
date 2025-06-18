# 🔐 SSH Audit Tool

A lightweight Python tool for auditing SSH servers, checking version banners, root login permissions, and weak keys.

---

## ✅ Features

- Detect SSH version and banner
- Check if root login is allowed
- Analyze authorized_keys file for weak or duplicate keys
- Export audit result as structured JSON

---

## 📁 Structure

audit/
├── ssh_version_checker.py
├── root_login_check.py
└── key_audit.py


---

## 📦 Requirements

- Python 3.x
- paramiko

Install with:

```bash
pip3 install -r requirements.txt



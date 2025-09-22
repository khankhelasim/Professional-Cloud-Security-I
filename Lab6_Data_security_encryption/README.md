# Lab 6: Data Security & Encryption Practices

This lab covers disk encryption (LUKS), secure data transmission (SSL/TLS), and key management (GPG).  
All scripts are provided for automation.

## Contents
- `luks_encrypt.py` → Automates LUKS disk encryption + mount
- `generate_ssl.py` → Automates SSL certificate generation
- `gpg_automate.py` → Automates GPG encryption/decryption
- `steps.md` → Detailed step-by-step instructions

## Quick Start
```bash
chmod +x luks_encrypt.py generate_ssl.py gpg_automate.py
sudo ./luks_encrypt.py       # Run disk encryption automation
./generate_ssl.py            # Create SSL certs
python3 gpg_automate.py      # Run GPG encryption/decryption

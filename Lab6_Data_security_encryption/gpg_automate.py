#!/usr/bin/env python3
# gpg_automate.py — Automates GPG file encryption/decryption

import gnupg, os, sys

gpg = gnupg.GPG()
RECIPIENT = "your-email@example.com"   # Change to your GPG key email
INFILE = "sensitive_file.txt"
OUT_ENC = "sensitive_file.txt.gpg"
OUT_DEC = "decrypted_file.txt"

def encrypt_file(infile, outfile):
    with open(infile, "rb") as f:
        status = gpg.encrypt_file(f, recipients=[RECIPIENT], output=outfile)
    print("Encrypt:", status.status)

def decrypt_file(infile, outfile):
    with open(infile, "rb") as f:
        status = gpg.decrypt_file(f, output=outfile)
    print("Decrypt:", status.status)

if __name__ == "__main__":
    if not os.path.exists(INFILE):
        print(f"{INFILE} missing — create it first.")
        sys.exit(1)
    encrypt_file(INFILE, OUT_ENC)
    decrypt_file(OUT_ENC, OUT_DEC)

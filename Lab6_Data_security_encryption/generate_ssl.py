#!/usr/bin/env python3
# generate_ssl.py — Automates SSL certificate generation

import subprocess

def run(cmd):
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

def main():
    run(["openssl", "genpkey", "-algorithm", "RSA", "-out", "server.key", "-pkeyopt", "rsa_keygen_bits:2048"])
    run(["openssl", "req", "-new", "-key", "server.key", "-out", "server.csr"])
    run(["openssl", "x509", "-req", "-days", "365", "-in", "server.csr", "-signkey", "server.key", "-out", "server.crt"])
    print("✅ Certificates created: server.key, server.csr, server.crt")

if __name__ == "__main__":
    main()

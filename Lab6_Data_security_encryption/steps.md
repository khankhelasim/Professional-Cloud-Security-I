
---

## 5️⃣ `steps.md`
```markdown
# Lab 6 — Step-by-Step Instructions

## 1. Enable Storage Encryption with LUKS
1. List disks:
   ```bash
   lsblk
Identify your extra disk (e.g. /dev/nvme1n1).

Run the Python script:

sudo ./luks_encrypt.py


Verify:

sudo cryptsetup status encrypted_disk

2. Implement SSL/TLS for Secure Transmission

Generate certs:

./generate_ssl.py


Run HTTPS server:

sudo python3 -m http.server 4443 --bind 0.0.0.0 --directory /mnt/encrypted_disk --certfile server.crt --keyfile server.key


Test:

curl -vk https://localhost:4443/ --insecure

3. Automate Key Management with GPG

Generate a GPG key:

gpg --full-generate-key


Prepare a test file:

echo "secret lab data" > sensitive_file.txt


Run Python script:

python3 gpg_automate.py


Verify decrypted file:

cat decrypted_file.txt


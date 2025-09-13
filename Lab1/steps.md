# Lab 1 - Step-by-Step Instructions

## Prerequisites
- Ubuntu with sudo privileges.
- Packages: `cryptsetup`, `auditd`.

---

## 1. Install required tools
```bash
sudo apt update
sudo apt install -y cryptsetup auditd
2. Check existing swap

swapon --show
cat /etc/fstab | grep -i swap || true
lsblk
free -h
3. Create encrypted swapfile

sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo swapoff -a
sudo cryptsetup close cryptswap 2>/dev/null || true
sudo cryptsetup open --type plain --cipher aes-xts-plain64 --key-size 256 --hash sha256 -d /dev/urandom /swapfile cryptswap
sudo mkswap /dev/mapper/cryptswap
sudo swapon /dev/mapper/cryptswap
4. Verify swap

swapon --show
lsblk
free -h
5. Make swap persistent (optional)
Edit /etc/crypttab:


cryptswap /swapfile /dev/urandom swap,cipher=aes-xts-plain64,size=256
Edit /etc/fstab:


/dev/mapper/cryptswap none swap sw 0 0
6. Setup auditd monitoring

sudo systemctl enable --now auditd
echo "initial secret" | sudo tee /etc/secret_config
sudo chmod 600 /etc/secret_config
sudo auditctl -w /etc/secret_config -p wa -k secretwatch
7. Trigger event

echo "unauthorized change at $(date)" | sudo tee -a /etc/secret_config
8. Check audit logs

sudo ausearch -k secretwatch
sudo aureport --file --summary
9. Cleanup

sudo swapoff -a
sudo cryptsetup close cryptswap || true
sudo rm -f /swapfile
sudo rm -f /etc/audit/rules.d/99-secretwatch.rules
sudo rm -f /etc/secret_config
bash
Copy code

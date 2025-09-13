
---

### `Lab1/commands.sh`
```bash
#!/bin/bash
# Lab 1 - Commands Script

# Install tools
sudo apt update
sudo apt install -y cryptsetup auditd

# Check existing swap
swapon --show
cat /etc/fstab | grep -i swap || true
lsblk
free -h

# Create swapfile
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo swapoff -a
sudo cryptsetup close cryptswap 2>/dev/null || true

# Open encrypted swap
sudo cryptsetup open --type plain --cipher aes-xts-plain64 --key-size 256 --hash sha256 -d /dev/urandom /swapfile cryptswap
sudo mkswap /dev/mapper/cryptswap
sudo swapon /dev/mapper/cryptswap

# Verify
swapon --show
lsblk
free -h

# Setup auditd
sudo systemctl enable --now auditd
echo "initial secret" | sudo tee /etc/secret_config
sudo chmod 600 /etc/secret_config
sudo auditctl -w /etc/secret_config -p wa -k secretwatch

# Trigger event
echo "unauthorized change at $(date)" | sudo tee -a /etc/secret_config

# Check logs
sudo ausearch -k secretwatch
sudo aureport --file --summary

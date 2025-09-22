#!/usr/bin/env python3
# luks_encrypt.py — Automates LUKS disk setup
# WARNING: luksFormat will ERASE all data on target disk

import subprocess, os, sys

DEVICE = "/dev/nvme1n1"        # <<< Change if different
MAPPER_NAME = "encrypted_disk"
MOUNT_POINT = "/mnt/encrypted_disk"

def run(cmd, check=True):
    print("RUN:", " ".join(cmd))
    subprocess.run(cmd, check=check)

def ensure_unmounted(dev):
    run(["sudo", "umount", dev], check=False)

def luks_format(dev):
    print(f"*** WARNING: About to LUKS-format {dev}. THIS WILL ERASE DATA! ***")
    answer = input("Type YES to continue: ")
    if answer != "YES":
        print("Aborting.")
        sys.exit(1)
    run(["sudo", "cryptsetup", "luksFormat", dev])

def luks_open(dev, name):
    run(["sudo", "cryptsetup", "luksOpen", dev, name])

def make_fs_and_mount(name, mount_point):
    mapper = f"/dev/mapper/{name}"
    run(["sudo", "mkfs.ext4", mapper])
    run(["sudo", "mkdir", "-p", mount_point])
    run(["sudo", "mount", mapper, mount_point])
    run(["sudo", "chown", f"{os.getlogin()}:{os.getlogin()}", mount_point])

def main():
    if not os.path.exists(DEVICE):
        print(f"Device {DEVICE} not found.")
        sys.exit(1)
    ensure_unmounted(DEVICE)
    luks_format(DEVICE)
    luks_open(DEVICE, MAPPER_NAME)
    make_fs_and_mount(MAPPER_NAME, MOUNT_POINT)
    print("✅ Done — encrypted and mounted:", MOUNT_POINT)

if __name__ == "__main__":
    main()

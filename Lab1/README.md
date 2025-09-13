# Lab 1 - Encrypted Swap and Auditd Monitoring

This lab demonstrates two key Linux security practices:

1. Creating and enabling an **encrypted swapfile** using `cryptsetup` with a random key.
2. Configuring **auditd** to watch a sensitive file (`/etc/secret_config`) for changes.

## Objectives
- Secure temporary data in memory using encrypted swap.
- Detect unauthorized modifications using auditd.

## Files
- `steps.md` → Full step-by-step instructions.
- `commands.sh` → All commands used in the lab.
- `outputs.txt` → Expected outputs of commands.
- `notes.md` → Key takeaways and troubleshooting notes.

# Lab 1 Notes

- Always run `swapoff -a` and `cryptsetup close cryptswap` before re-creating or formatting encrypted swap.
- Use `/dev/urandom` in `/etc/crypttab` for maximum security (new random key every boot).
- Audit rules added with `auditctl` are temporary — use `/etc/audit/rules.d/` to persist.
- Test with multiple users modifying `/etc/secret_config` to see auditd log entries.
- Troubleshooting:
  - "Device busy" → swap still active, run `sudo swapoff -a`.
  - "cryptswap already exists" → close old mapping with `sudo cryptsetup close cryptswap`.

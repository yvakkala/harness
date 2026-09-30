# Infrastructure Review

## Containers and services

- Pin material base-image versions or digests and use minimal maintained images.
- Run with the least privileges, files, capabilities, network access, and writable storage required.
- Define health, restart, shutdown, resource, and persistent-state behavior.
- Verify configuration injection without printing secrets.

## DNS and TLS

- Identify the authoritative zone, existing records, TTLs, certificate ownership, renewal path, and propagation expectations.
- Lower TTL before a planned migration only when lead time makes it useful, and restore the intended value afterward.
- Verify resolution from relevant networks and certificate name, chain, validity, and renewal behavior.

## Reverse proxies and web servers

- Validate configuration before reload and preserve the previous working configuration.
- Define upstream timeouts, body limits, forwarding headers, client identity, TLS policy, and health behavior deliberately.
- Confirm graceful reload and representative HTTP, streaming, and upgrade behavior where applicable.

## Firewalls and remote hosts

- Preserve an independently verified management path before changing remote access rules.
- Use explicit least-privilege rules and confirm both intended access and intended denial.
- Avoid flushing a working ruleset before a replacement is validated and recoverable.

## Recovery evidence

- Record the prior state, applied change, resulting identifiers, verification evidence, and rollback or forward-recovery command.
- For irreplaceable state, confirm a recent restorable backup before a destructive operation.

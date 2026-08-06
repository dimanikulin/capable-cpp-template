---
description: "Use when working on authentication, authorization, secrets, input validation, dependency risk, secure defaults, or security-sensitive code paths."
applyTo: "**/*"
---

# Security Instructions

- Do not introduce hardcoded secrets, tokens, passwords, private keys, or sample credentials.
- Prefer secure defaults and fail-closed behavior for configuration, permissions, and feature toggles.
- Validate and sanitize untrusted input at boundaries, including CLI arguments, file paths, environment variables, and network data.
- Avoid unsafe shell execution patterns and command construction from untrusted input.
- Keep filesystem operations explicit and bounded; avoid path traversal risks when joining or normalizing paths.
- Minimize dependency additions. If a new dependency is necessary, prefer well-maintained packages with a clear security posture.
- When changing build, packaging, or CI workflows, avoid expanding privileges or exposing secrets in logs and artifacts.
- Flag security-relevant tradeoffs in the final response, especially when a safer design would require a larger follow-up change.

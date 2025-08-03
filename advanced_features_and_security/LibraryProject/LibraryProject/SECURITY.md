# Django Application Security Review

## Configured Settings
- `SECURE_SSL_REDIRECT`: Enforces all HTTP requests to be redirected to HTTPS.
- `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`: Enables HSTS for strong browser enforcement of HTTPS.
- `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`: Ensures cookies are transmitted over secure channels only.
- `X_FRAME_OPTIONS`: Prevents clickjacking by denying iframe usage.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents browsers from guessing MIME types.
- `SECURE_BROWSER_XSS_FILTER`: Enables browser-based XSS filtering.

## Deployment Setup
- Configured Nginx to redirect HTTP to HTTPS and serve over SSL.
- SSL/TLS certificates obtained via Let’s Encrypt using Certbot.

## Recommendations
- Regularly update Django and dependencies.
- Use HTTPS-only third-party resources (JS, CSS).
- Monitor logs for unusual activity or failed login attempts.

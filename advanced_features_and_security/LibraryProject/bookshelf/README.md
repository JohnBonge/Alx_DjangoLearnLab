## Security Measures Implemented

- DEBUG disabled for production.
- CSRF protection enabled via Django middleware and `{% csrf_token %}` in forms.
- Secure cookie settings: `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`.
- Browser protections: XSS Filter, content type nosniff, frame blocking.
- SQL injection prevented by using Django ORM.
- XSS attacks mitigated via Content Security Policy using django-csp.

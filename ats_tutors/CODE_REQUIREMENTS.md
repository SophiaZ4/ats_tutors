# Code Requirements

[x] RQ-001 | Core | Basic Flask application. Core Flask setup with routing and template rendering.
[x] RQ-002 | Contact | Contact form with email functionality. Form to send emails via SMTP using Flask-Mail.
[ ] RQ-003 | Auth | User authentication. Registration, Login, and Session management.
[ ] RQ-004 | Blog | Blog section. CMS functionality for posting and viewing updates.
[ ] RQ-005 | Schedule | Tutoring session scheduling. Calendar and booking system for sessions.
[x] RQ-006 | Security | Disable Debug Mode. Ensure the application runs with `debug=False` to prevent exposing stack traces.
[x] RQ-007 | Security | CSRF Protection. Implement Cross-Site Request Forgery protection (e.g., via Flask-WTF) for all forms.
[x] RQ-008 | Security | Rate Limiting. Implement rate limiting (e.g., via Flask-Limiter) to prevent spam and abuse, especially on the contact form.
[x] RQ-009 | Security | HTTP Headers. Implement security headers (HSTS, X-Frame-Options, etc.) to protect against common attacks.
[x] RQ-010 | Security | Secret Key. Ensure a strong, persistent `FLASK_SECRET_KEY` is loaded from the environment and not hardcoded.
[x] RQ-011 | Debug | Smart Debugging. Show detailed errors only to developers based on IP; public sees generic 500 page.
[x] RQ-D01 | UX | Mobile view of page fonts look too small. Fix page so view on all size screens is readable.
[ ] RQ-D02 | UX | create a nice '500.html' template utilising our logo and themes. The page should feature an actual simple snake like game that runs around the screen controlled by the user.

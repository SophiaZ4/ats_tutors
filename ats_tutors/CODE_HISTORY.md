# Code History

### 2026-01-05: Smart Debug & Crash Test (RQ-011)
*   **Added:** New "Smart Debug" configuration in `app.py`.
    *   Shows detailed stack traces only to developers (`TRUSTED_IPS`).
    *   Public users see a generic 500 error page.
*   **Added:** A new `/crash` route to intentionally trigger a `ZeroDivisionError` for testing the debug configuration.
*   **Modified:** `app.py`

### 2026-01-05: Mobile Responsiveness (RQ-D01)
*   **Modified:** `static/css/style.css`
*   **Details:** Added media queries for mobile devices (max-width: 768px). 
    *   Adjusted font sizes for better readability.
    *   Stacked navigation items, hero elements, and grid cards vertically.
    *   Optimized padding and spacing for smaller screens.

## 2026-01-05

*   **Security Hardening (RQ-006 to RQ-010):**
    *   Disabled debug mode for production safety.
    *   Implemented CSRF protection using `Flask-WTF` on the contact form.
    *   Added rate limiting (5 requests/minute) on the message sending endpoint using `Flask-Limiter`.
    *   Configured security headers (HSTS, X-Frame-Options, X-Content-Type-Options, etc.).
    *   Ensured secure `FLASK_SECRET_KEY` management via `.env`.
*   **Infrastructure:** Updated project documentation (`GEMINI.md`) to reflect the single-environment deployment strategy.
*   **Dependencies:** Added `Flask-WTF` and `Flask-Limiter` to `requirements.txt`.

## 2024-07-29

*   Initial project setup.
*   Created `app.py` with basic Flask application.
*   Added contact form functionality with Flask-Mail.
*   Created `GEMINI.md` for project context.
*   Cleaned up unnecessary files and directories.

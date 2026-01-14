# Code Test Cases

| Status | Test Case |
| --- | --- |
| [x] | Send a message through the contact form and verify that the email is received. |
| [ ] | Test user registration and login. |
| [ ] | Test creating a new blog post. |
| [ ] | Test scheduling a tutoring session. |
| [ ] | **Security**: Verify that submitting the contact form without a CSRF token fails. |
| [ ] | **Security**: Verify that sending more than 5 messages per minute from the same IP triggers a rate limit error (429). |
| [ ] | **Security**: Verify that security headers (HSTS, X-Frame-Options, etc.) are present in responses. |
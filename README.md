Aim To Soar (ATS) Tutors Website

Aim To Soar Tutors is a professional web platform built to connect K-12 students with high-achieving HSC tutors. This project showcases a full-stack implementation featuring a Python Flask backend, integrated email services, and a mobile-first responsive design.

🛠️ Tech Stack
Backend: Python / Flask

Frontend: HTML5, CSS3 (Modern Flexbox & CSS Grid), JavaScript

Deployment: Docker / Synology SDS (Shared Drive System)

Security: Flask-Limiter (Rate Limiting), CSRF Protection, and Reverse Proxy Header trust

✨ Key Features
Adaptive UI: Responsive tutoring and review grids that dynamically scale from mobile devices to large laptop screens using CSS Grid auto-fit.

Secure Contact System: A validated inquiry form that uses Flask-Mail to deliver customer messages directly to the business inbox.

Anti-Spam Logic: Implemented Flask-Limiter to prevent automated form submissions and double-click prevention via JavaScript to improve user experience.

Production-Ready Logging: Integrated Python logging to track server performance and inquiry success rates.

🚀 Deployment & Development
This application is currently deployed using Docker on a Synology SDS environment.

Local Setup
1. Clone the repository:

Bash

git clone https://github.com/SophiaZ4/ats_tutors.git

2. Install dependencies:

Bash

pip install -r requirements.txt

3. Create a .env file with your credentials:

Plaintext

MAIL_PASS=your_gmail_app_password
FLASK_SECRET_KEY=your_secret_key

4. Run the development server:

Bash

python app.py

📈 Future Road Map

[ ] Automated Scheduling: Integration with a calendar API for lesson bookings.

[ ] Student Dashboard: A portal for students to access HSC STEM and HSIE resources.

Developed by Sophia Zammit (2026).
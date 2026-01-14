# Project Overview

This is a Flask web application that serves as a simple contact form. It allows users to send a message to a predefined email address. The application uses Flask-Mail to send emails via a Gmail SMTP server. The project is structured with a main application file (`app.py`), a `templates` directory for the HTML, and a `static` directory for CSS and images.

This project is being developed by David (System Architect / DevOps) and Sophia (Lead Developer). The goal is to create a functional tutoring website accessible via the public URL `https://atstutors.sitebrief.com.au`.

# Environment & Network

* **Deployment Strategy:** **SINGLE ENVIRONMENT ONLY.** This project operates on a single server that acts as Development, Testing, and Production simultaneously. All changes made to the codebase are **instantly live** and accessible via the public URL. Extreme caution must be exercised when modifying code.
* **OS:** The application runs in a Debian 12 Docker container on a Synology NAS. Development is performed on a Windows machine (win32).
* **Workspace:** The project files are edited on a mapped drive (`X:\Sophia\ATSTutors_webapp\ats_tutors`). These are synced to `/root/workspace` in the container.
* **Remote Access:** Use `ssh sds` to connect to the NAS for remote commands. Most container-specific commands should use `ssh sds sudo docker exec atstutors-dev <command>`.
* **Network:** The application is behind a reverse proxy.
    * The Flask server must listen on `0.0.0.0:8000`.
    * The public URL is `https://atstutors.sitebrief.com.au`.

# Building and Running

* **NO Virtual Environments:** Do NOT create or use `.venv` folders. The Docker container is already an isolated environment.
* **Dependencies:**
    * To add a new dependency, run `ssh sds sudo docker exec atstutors-dev pip install <package_name>`.
    * After installing a new package, you MUST add it to `requirements.txt`.
* **Configuration:** A `.env` file is already configured in the `ats_tutors` directory. It contains sensitive credentials and must NOT be committed to version control.
* **Running the application:**
    * The web server starts automatically when the container boots.
    * Use the soft restart script via SSH if code changes don't apply automatically.

# Development Conventions

* **Code Style:** The code follows the standard PEP 8 style guidelines for Python.
* **Project Folder:** Development-specific files and logs are stored in the `.project` directory (e.g., `restart_server.sh`, `server.log`). This directory is partially ignored by git.
* **Documentation:**
    * Update `CODE_HISTORY.md` for all versioned changes.
    * Update `CODE_REQUIREMENTS.md` for backlog status changes.
    * Update `CODE_TESTCASES.md` when adding or verifying test scenarios.
* **Preferred Commands:**
    * **Python:** Use `python` or `python3`.
    * **Node:** Use `npm` and `node`.
    * **Editor:** The developers are using VS Code.

## Remote Operations & Restarts
Since the agent is running on Windows, Docker commands can now be sent via SSH without interrupting the session.

### 1. SSH Execution
* Always use `ssh sds bash -c "<command>"` to ensure the NAS environment is correctly loaded.

### 2. How to Restart the App (Safe Method)
If you need to reload `app.py`, run the **Soft Restart Script** inside the container via SSH:
  `ssh sds sudo /usr/local/bin/docker exec atstutors-dev /root/restart_server.sh`

### 3. Docker Commands
* You can safely run docker commands via SSH.
* To check container status: `ssh sds sudo docker ps`
* To restart the container: `ssh sds sudo docker restart atstutors-dev`
* To run a command inside the container: `ssh sds sudo docker exec atstutors-dev <command>`

### 4. Logging
* View server logs via the mapped drive or remotely:
  `ssh sds bash -c "tail -f /root/workspace/ats_tutors/.project/server.log"`
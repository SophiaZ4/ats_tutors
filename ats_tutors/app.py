try:
    from flask import Flask, render_template, request, flash, redirect, url_for, make_response
    from flask_mail import Mail, Message
    from flask_wtf.csrf import CSRFProtect
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    from flask import request, redirect
    from werkzeug.middleware.proxy_fix import ProxyFix  # <--- NEW: Required for Docker
    import os
    import traceback  # <--- NEW: To show crash logs
    from dotenv import load_dotenv
    import logging


    # Configure logging
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

    app = Flask(__name__)
    load_dotenv() # Loads the variables from .env
    logging.info('Flask app starting up')

    # --- NEW: PROXY FIX ---
    # This tells Flask to trust the headers sent by your Synology Reverse Proxy.
    # Without this, 'get_remote_address' sees the Docker Gateway IP (172.x.x.x) for everyone.
    # This fixes Rate Limiting (so you don't ban the whole world) and the IP check below.
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default-safe-key-for-dev')

    # Security: CSRF Protection
    csrf = CSRFProtect(app)

    # Security: Rate Limiting
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"],
        storage_uri="memory://"
    )

    @app.before_request
    def force_https():
        # If the proxy says the connection isn't secure, force the redirect
        if not request.is_secure and app.env != 'development':
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)

    # Security: HTTP Headers
    @app.after_request
    def add_security_headers(response):
        logging.info(f"Adding security headers to response for {request.path}")
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'
        return response

    # Gmail Configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'aimtosoartutors@gmail.com'
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASS')
    app.config['MAIL_DEFAULT_SENDER'] = 'aimtosoartutors@gmail.com'

    mail = Mail(app)

    # --- NEW: SMART DEBUG CONFIGURATION ---
    # Add your LAN IP and your External Static IP here.
    # You can find the correct IP by visiting /whoami after deploying.
    TRUSTED_IPS = ['127.0.0.1', '192.168.68.211', '202.130.196.59'] 

    @app.route('/whoami')
    def whoami():
        """Temporary helper to find your IP behind the proxy."""
        logging.info(f"whoami requested by {request.remote_addr}")
        return f"Flask sees your IP as: {request.remote_addr}"

    @app.errorhandler(500)
    def internal_error(exception):
        """Show detailed errors to Developers, generic 500 page to Public."""
        logging.error(f"Internal error: {exception}", exc_info=True)
        user_ip = request.remote_addr
        
        if user_ip in TRUSTED_IPS:
            # If it's YOU, show the crash report
            return f"<h2>👨‍💻 Developer Mode Error</h2><pre>{traceback.format_exc()}</pre>", 500
        
        # If it's the PUBLIC, show a nice generic error
        return render_template('500.html'), 500

    # --- ROUTES ---

    @app.route('/')
    def home():
        logging.info(f"Home page requested by {request.remote_addr}")
        return render_template('index.html')

    @app.route('/send_message', methods=['POST'])
    @limiter.limit("5 per minute")
    def send_message():
        logging.info(f"Send message requested by {request.remote_addr}")
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email') 
            phone = request.form.get('phone')
            message_body = request.form.get('message')

            msg = Message(subject=f"New Inquiry from {name}",
                          recipients=['aimtosoartutors@gmail.com'])
            
            msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message_body}"
            
            try:
                mail.send(msg)
                flash("Success! Your message has been sent. We'll get back to you soon.")
                logging.info("Message sent successfully.")
            except Exception as e:
                flash(f"Error: Could not send message. Please try again later.")
                logging.error(f"Failed to send email: {e}", exc_info=True)

            return redirect(url_for('home', _anchor='contact-section'))
        
    @app.errorhandler(429)
    def ratelimit_handler(e):
        # Instead of a separate page, we flash a message and stay on home
        flash("Too many messages sent. Please wait a minute before trying again.")
        return redirect(url_for('home', _anchor='contact-section'))

    @app.route('/crash')
    def crash_test():
        """Intentionally causes a divide-by-zero error for testing."""
        logging.info(f"Crash test requested by {request.remote_addr}")
        _ = 1 / 0
        return "This will not be returned."

    if __name__ == '__main__':
        logging.info('Starting Flask development server')
        # NEW CONFIGURATION:
        # debug=True: Enables Auto-Reload (Crucial for development)
        # use_debugger=False: Disables the interactive console in the browser (Safety feature)
        app.run(debug=True, host='0.0.0.0', port=8000)
except Exception as e:
    with open("critical_error.log", "w") as f:
        f.write(traceback.format_exc())
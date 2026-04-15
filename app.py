from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'riz-electrics-secret-key'

# Yahoo Mail config
YAHOO_EMAIL = 'irfanali_gk@yahoo.com'
YAHOO_APP_PASSWORD = 'yrmfheshhdbymlht'

def send_email(first_name, last_name, email, phone, service, message):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'New Enquiry from {first_name} {last_name} – {service}'
    msg['From'] = YAHOO_EMAIL
    msg['To'] = YAHOO_EMAIL

    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background:#f4f4f4; padding: 30px;">
      <div style="max-width:600px; margin:0 auto; background:#fff; border-radius:10px; overflow:hidden; box-shadow:0 2px 10px rgba(0,0,0,0.1);">
        <div style="background:#0a1628; padding:24px 30px;">
          <h2 style="color:#f5a623; margin:0; font-size:22px;">New Website Enquiry</h2>
          <p style="color:#aab4c8; margin:6px 0 0; font-size:13px;">Riz Electrics Ltd – Contact Form Submission</p>
        </div>
        <div style="padding:30px;">
          <table style="width:100%; border-collapse:collapse;">
            <tr><td style="padding:10px 0; border-bottom:1px solid #eee; color:#666; width:140px; font-size:14px;"><strong>Name</strong></td><td style="padding:10px 0; border-bottom:1px solid #eee; font-size:14px; color:#1a1a1a;">{first_name} {last_name}</td></tr>
            <tr><td style="padding:10px 0; border-bottom:1px solid #eee; color:#666; font-size:14px;"><strong>Email</strong></td><td style="padding:10px 0; border-bottom:1px solid #eee; font-size:14px; color:#1a1a1a;"><a href="mailto:{email}" style="color:#0a1628;">{email}</a></td></tr>
            <tr><td style="padding:10px 0; border-bottom:1px solid #eee; color:#666; font-size:14px;"><strong>Phone</strong></td><td style="padding:10px 0; border-bottom:1px solid #eee; font-size:14px; color:#1a1a1a;"><a href="tel:{phone}" style="color:#0a1628;">{phone}</a></td></tr>
            <tr><td style="padding:10px 0; border-bottom:1px solid #eee; color:#666; font-size:14px;"><strong>Service</strong></td><td style="padding:10px 0; border-bottom:1px solid #eee; font-size:14px; color:#1a1a1a;">{service}</td></tr>
            <tr><td style="padding:10px 0; color:#666; font-size:14px; vertical-align:top;"><strong>Message</strong></td><td style="padding:10px 0; font-size:14px; color:#1a1a1a;">{message if message else 'No message provided.'}</td></tr>
          </table>
        </div>
        <div style="background:#f8f9fb; padding:16px 30px; text-align:center;">
          <p style="color:#888; font-size:12px; margin:0;">This email was sent from the Riz Electrics website contact form.</p>
        </div>
      </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_body, 'html'))

    with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as server:
        server.login(YAHOO_EMAIL, YAHOO_APP_PASSWORD)
        server.sendmail(YAHOO_EMAIL, YAHOO_EMAIL, msg.as_string())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    service = request.form.get('service', '')
    message = request.form.get('message', '')

    try:
        send_email(first_name, last_name, email, phone, service, message)
        flash(f"Thank you {first_name}! Your message has been sent. We will contact you shortly.", 'success')
    except Exception as e:
        flash("Sorry, there was an issue sending your message. Please call us directly on 07900 117900.", 'danger')

    return redirect(url_for('index') + '#contact')

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms-conditions')
def terms():
    return render_template('terms.html')

@app.route('/complaints-policy')
def complaints():
    return render_template('complaints.html')

if __name__ == '__main__':
    app.run(debug=True)

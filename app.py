from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'riz-electrics-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    flash(f"Thank you {first_name}! We've received your request and will contact you shortly.", 'success')
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

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'riz-electrics-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    service = request.form.get('service')
    message = request.form.get('message')
    flash(f"Thank you {first_name}! We've received your request and will contact you shortly.", 'success')
    return redirect(url_for('index') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)

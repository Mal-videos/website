from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'malvideoz-secret-key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would normally save to database or send email
        # For demo purposes, we'll just redirect with success message
        return redirect(url_for('contact', success=True))
    
    success = request.args.get('success', False)
    return render_template('contact.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)    return render_template('services.html', studio=studio)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', studio=studio)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html', studio=studio)

@app.route('/about')
def about():
    return render_template('about.html', studio=studio)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Placeholder: save or send email logic here
        return redirect(url_for('contact'))
    return render_template('contact.html', studio=studio)

if __name__ == '__main__':
    app.run(debug=True)

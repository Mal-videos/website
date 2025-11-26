from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Studio data (from your stored info)
studio = {
    "name": "MAL VIDEOZ PRODUCTION",
    "phone": "+256743999720",
    "email": "tapencenamugogo@gmail.com",
    "social": {
        "facebook": "MAl Videoz Production",
        "instagram": "@MAlVideozProduction",
        "twitter": "@MAlVideoz"
    },
    "services": [
        "Wedding & Introduction Photography/Videography",
        "Birthday Photography/Videography",
        "Graduation Photography/Videography",
        "Music Videos (Silver Package)",
        "Music Videos (Gold Package)",
        "Portraits"
    ],
    "usps": [
        "Modern aesthetic and style",
        "High-quality photography and videography",
        "Comprehensive coverage for various life milestones",
        "Structured music video packages"
    ]
}

@app.route('/')
def home():
    return render_template('home.html', studio=studio)

@app.route('/services')
def services():
    return render_template('services.html', studio=studio)

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

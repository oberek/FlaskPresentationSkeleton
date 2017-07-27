from flask import Flask, render_template

app = Flask(__name__)

# Prevents Cross-Site Request Forgery Attacks
app.secret_key = 'dev key'

@app.route('/')
def home():
    return render_template('home.html'), 404

@app.route('/about')
def about():
    return render_template('about.html', ), 404

app.run(debug=True)
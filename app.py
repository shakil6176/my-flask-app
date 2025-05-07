from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    emails = [
        {'from': 'example1@domain.com', 'subject': 'Welcome!', 'body': 'Hello, welcome to our service.'},
        {'from': 'example2@domain.com', 'subject': 'Verification', 'body': 'Please verify your email address.'}
    ]
    return render_template('index.html', emails=emails)

if __name__ == '__main__':
    app.run(debug=True)

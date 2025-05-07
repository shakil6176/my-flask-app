from flask import Flask, render_template, jsonify
import os
import random

app = Flask(__name__)

# Dummy global store (তোমার পরে ডাটাবেজে রাখতে পারো)
emails = [
    {'from': 'example1@domain.com', 'subject': 'Welcome!', 'body': 'Hello, welcome to our service.'},
    {'from': 'example2@domain.com', 'subject': 'Verification', 'body': 'Please verify your email address.'}
]

email_domains = ["tempmail.com", "mailjunk.io", "fakemail.org"]

@app.route('/')
def index():
    return render_template('index.html', emails=emails)

@app.route('/generate_email')
def generate_email():
    username = f"user{random.randint(1000, 9999)}"
    domain = random.choice(email_domains)
    new_email = f"{username}@{domain}"
    return jsonify({'email': new_email})

@app.route('/delete_emails')
def delete_emails():
    global emails
    emails = []
    return jsonify({'message': 'Inbox cleared', 'emails': emails})

@app.route('/refresh_emails')
def refresh_emails():
    # Demo ইনবক্স (পরে লাইভ ডেটা দিবে)
    global emails
    return jsonify({'emails': emails})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)

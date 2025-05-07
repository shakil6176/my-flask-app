from flask import Flask, render_template
import os

app = Flask(__name__)  # app ইনস্ট্যান্স তৈরি

# ফাংশনটি ডিফাইন করা
def load_emails():
    # এখানে তোমার ইমেইল লোড করার লজিক থাকবে
    emails = [
        {'from': 'example1@domain.com', 'subject': 'Welcome!', 'body': 'Hello, welcome to our service.'},
        {'from': 'example2@domain.com', 'subject': 'Verification', 'body': 'Please verify your email address.'}
    ]
    return emails

@app.route('/')
def index():
    emails = load_emails()
    bodies = [email['body'] for email in emails]
    return render_template('index.html', emails=emails, bodies=bodies)


if __name__ == "__main__":
    # এখানে প্রথমেই app.run() কল করতে হবে
    port = int(os.environ.get("PORT", 10000))  # পোর্ট নির্ধারণ
    app.run(host="0.0.0.0", port=port, debug=True)  # এই লাইনটি একবার ব্যবহার করো

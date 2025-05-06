from flask import Flask, render_template
import os
import json

app = Flask(__name__)

# Load emails from mock JSON file (you can replace this with real email fetch logic)
def load_emails():
    with open('emails.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

@app.route('/')
def inbox():
    emails = load_emails()
    bodies = [email['body'] for email in emails]
    return render_template('inbox.html', emails=emails, bodies=bodies)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

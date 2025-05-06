from flask import Flask, render_template, send_from_directory
import os
from inbox_parser import get_email_data  # Or however you're fetching mails

app = Flask(__name__)

@app.route('/')
def inbox():
    emails = get_email_data()  # Replace with your actual logic
    subjects = [{'subject': m['subject'], 'from': m['from']} for m in emails]
    bodies = [m['body'] for m in emails]
    return render_template('inbox.html', emails=subjects, bodies=bodies)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, render_template, request
import os

app = Flask(__name__)

# ডেমো ইনবক্স (পরে এটাতে আমরা API বা database ব্যবহার করব)
inbox = [
    {"id": "1", "from": "admin@example.com", "subject": "Welcome!", "content": "Welcome to your inbox."},
    {"id": "2", "from": "noreply@service.com", "subject": "OTP Code", "content": "Your OTP is 123456"}
]

@app.route('/')
def home():
    return "Hello from Flask on Render!"

@app.route("/inbox")
def show_inbox():
    return render_template("inbox.html", emails=inbox)

@app.route("/message/<id>")
def show_message(id):
    for mail in inbox:
        if mail["id"] == id:
            return render_template("message.html", mail=mail)
    return "Message not found", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

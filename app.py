import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ইন-মেমোরি ইনবক্স
inbox = [
    {"subject": "Welcome!", "sender": "admin@example.com"},
    {"subject": "OTP Code", "sender": "noreply@service.com"},
]

@app.route("/")
def home():
    return render_template("inbox.html", inbox=inbox)

@app.route("/send", methods=["POST"])
def send_email():
    subject = request.form.get("subject")
    sender = request.form.get("sender")

    if subject and sender:
        inbox.append({"subject": subject, "sender": sender})

    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

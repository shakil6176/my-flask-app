from flask import Flask, render_template, request
import re
import uuid

app = Flask(__name__)

# ডেমো ইনবক্স ডেটা
emails = [
    {
        "id": str(uuid.uuid4()),
        "subject": "Welcome!",
        "sender": "admin@example.com",
        "body": "Thanks for signing up. Enjoy our service!"
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "OTP Code",
        "sender": "noreply@service.com",
        "body": "Your OTP is 735291. Please do not share it with anyone."
    }
]


@app.route("/")
def inbox():
    return render_template("inbox.html", emails=emails)

@app.route("/message/<msg_id>")
def view_message(msg_id):
    email = next((msg for msg in emails if msg["id"] == msg_id), None)
    if not email:
        return "Email not found", 404

    # OTP বের করি (4 থেকে 8 ডিজিট পর্যন্ত)
    otp_match = re.search(r"\b\d{4,8}\b", email["body"])
    otp = otp_match.group(0) if otp_match else None

    return render_template("message.html", email=email, otp=otp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

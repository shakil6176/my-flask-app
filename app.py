from flask import Flask, render_template, request
import uuid

app = Flask(__name__)

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
        "body": "Your OTP is 735291. Please do not share it with anyone. Verify here: https://example.com/verify"
    }
]

@app.route("/")
def inbox():
    selected_email = None
    selected_id = request.args.get("msg_id")

    if selected_id:
        for email in emails:
            if email["id"] == selected_id:
                selected_email = email
                break

    return render_template("inbox_combined.html", emails=emails, selected_email=selected_email)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

"""
qr_app.py — standalone QR code generator.
Run with: py qr_app.py
No external API keys or .env variables required.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def qr_generator():
    return render_template("qr_generator.html")


if __name__ == "__main__":
    print("QR Code Generator running → http://127.0.0.1:7011")
    app.run(port=7011, debug=True)

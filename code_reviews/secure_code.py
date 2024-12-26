from flask import Flask, request, jsonify
from flask_sslify import SSLify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sqlite3

app = Flask(__name__)
sslify = SSLify(app)

# Example key for AES encryption (must be securely stored in a production system)
key = b"sixteen_byte_key"


@app.route("/get_user", methods=["GET"])
def get_user():
    user_id = request.args.get("user_id")

    # ✅ Validate input
    if not user_id or not user_id.isdigit():
        return jsonify({"error": "Invalid user_id"}), 400

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # ✅ Secure query with parameterized statements to prevent SQL injections
    query = "SELECT * FROM users WHERE id = ?;"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        # ✅ Encrypt the email before returning to the client
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_email = cipher.encrypt(pad(user[2].encode(), AES.block_size))
        return jsonify({"id": user[0], "name": user[1], "email": encrypted_email.hex()})
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc")

from flask import Flask, request, jsonify
import sqlite3

# ❌ Protect Data in Transit, use TLS to encrypt all communication between client and server
app = Flask(__name__)


@app.route("/get_user", methods=["GET"])
def get_user():
    user_id = request.args.get("user_id")
    # ❌ Improper Input Validation - user_id is not validated

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # ❌ Vulnerability: SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        # ❌ Mask/Encrypt Sensitive Data
        return jsonify({"id": user[0], "name": user[1], "email": user[2]})
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

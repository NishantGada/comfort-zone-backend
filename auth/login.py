from flask import request, jsonify

from config.dbconfig import get_connection
from auth.helper_functions import is_duplicate_email
from helper_functions import validate_request, fetch_user_id_from_email
from . import auth_bp

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        validate_request(data)

        user_id = fetch_user_id_from_email(data.get("email"))
        
        if not user_id:
            return jsonify({"success": False, "message": "Invalid user"}), 404
        
        cursor.execute("SELECT password FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()

        if result["password"] != data.get("password"):
            return jsonify({"success": False, "message": "Invalid credentials, check password"}), 400

        return jsonify({"success": True, "message": "Login successful"}), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "An error occurred",
            "error": str(e)
        }), 500
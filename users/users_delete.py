from flask import request, jsonify

from config.dbconfig import get_connection
from helper_functions import fetch_user_id_from_email
from . import users_bp

@users_bp.route("/user", methods=["DELETE"])
def delete_user():
    try: 
        data = request.get_json()
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        user_id = fetch_user_id_from_email(data.get("email"))
        
        if not user_id:
            return jsonify({"success": False, "message": "Invalid user"}), 404

        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "User deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "An error occurred",
            "error": str(e)
        }), 500
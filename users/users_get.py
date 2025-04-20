from flask import request, jsonify

from config.dbconfig import get_connection
from . import users_bp

@users_bp.route("/users", methods=["GET"])
def get_all_users():    
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    return jsonify({
        "success": True, 
        "message": "All users fetched successfully", 
        "data": {
            "users": users
        }
    }), 200
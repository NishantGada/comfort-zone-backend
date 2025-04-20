from flask import request, jsonify
import uuid

from config.dbconfig import get_connection
from auth.helper_functions import is_duplicate_email
from helper_functions import validate_request
from . import auth_bp

@auth_bp.route("/register", methods=["POST"])
def register_new_user():
    data = request.get_json()
    connection = get_connection()
    cursor = connection.cursor()

    validate_request(data)
    
    if is_duplicate_email(data.get("email")):
        return (
            jsonify({"success": False, "message": "Email already registered"}),
            400,
        )
    
    try:
        user_id = str(uuid.uuid4())
        query = "INSERT INTO users (user_id, email, password, phone, dob, gender, address_line_1, address_line_2, city, state, zipcode, first_name, last_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(
            query,
            (
                user_id,
                data.get("email"),
                data.get("password"),
                data.get("phone"),
                data.get("dob"),
                data.get("gender"),
                data.get("address_line_1"),
                data.get("address_line_2"),
                data.get("city"),
                data.get("state"),
                data.get("zipcode"),
                data.get("first_name"),
                data.get("last_name"),
            ),
        )

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "User created successfully"}), 201
    except Exception as e:
        return (
            jsonify({"success": False, "message": e}),
            500,
        )

from flask import request, jsonify
import uuid

from config.dbconfig import get_connection
from helper_functions import validate_request, fetch_user_id_from_email
from . import toilet_bp

@toilet_bp.route("/toilet/comment", methods=["POST"])
def add_comment():
    try:
        data = request.get_json()
        connection = get_connection()
        cursor = connection.cursor()

        validate_request(data)
        user_id = fetch_user_id_from_email(data.get("email"))

        if not user_id:
            return jsonify({"success": False, "message": "Invalid user"}), 404

        comment_id = str(uuid.uuid4())
        print("comment_id: ", comment_id)

        query = """
            INSERT INTO toilet_comments (comment_id, toilet_id, user_id, comment_text)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (comment_id, data.get("toilet_id"), user_id, data.get("comment_text")))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Comment added successfully"})
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "An error occurred",
            "error": str(e)
        }), 500
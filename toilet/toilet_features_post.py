from flask import request, jsonify
import uuid

from config.dbconfig import get_connection
from helper_functions import validate_request, fetch_user_id_from_email
from . import toilet_bp

@toilet_bp.route("/toilet/feature", methods=["POST"])
def add_feature():
    try:
        data = request.get_json()
        connection = get_connection()
        cursor = connection.cursor()

        validate_request(data)

        feature_id = str(uuid.uuid4())
        query = """
            INSERT INTO toilet_features (feature_id, toilet_id, feature_name)
            VALUES (%s, %s, %s)
        """
        cursor.execute(
            query, 
            (
                feature_id,
                data.get("toilet_id"),
                data.get("feature_name"),
            )
        )

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Feature added successfully"})
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "An error occurred",
            "error": str(e)
        }), 500
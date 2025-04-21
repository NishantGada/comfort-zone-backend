from flask import request, jsonify
import uuid

from config.dbconfig import get_connection
from helper_functions import validate_request
from . import toilet_bp

@toilet_bp.route("/toilet", methods=["POST"])
def add_new_toilet():
    try:
        data = request.get_json()
        connection = get_connection()
        cursor = connection.cursor()

        validate_request(data)

        toilet_id = str(uuid.uuid4())

        query = """
        INSERT INTO toilets (
            toilet_id, toilet_name, toilet_description,
            toilet_address_line_1, toilet_address_line_2,
            toilet_city, toilet_state, toilet_zipcode, toilet_gender, toilet_charges,
            toilet_build_date, open_time, close_time
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                toilet_id,
                data.get("toilet_name"),
                data.get("toilet_description"),
                data.get("toilet_address_line_1"),
                data.get("toilet_address_line_2"),
                data.get("toilet_city"),
                data.get("toilet_state"),
                data.get("toilet_zipcode"),
                data.get("toilet_gender"),
                data.get("toilet_charges", 0.0),
                data.get("toilet_build_date"),  # Should be in 'YYYY-MM-DD' format
                data.get("open_time"),
                data.get("close_time")
            ),
        )

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Toilet added successfully"}), 201

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "An error occurred",
            "error": str(e)
        }), 500
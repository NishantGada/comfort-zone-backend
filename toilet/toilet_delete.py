from flask import request, jsonify

from config.dbconfig import get_connection
from . import toilet_bp

@toilet_bp.route("/toilet", methods=["DELETE"])
def delete_toilet():
    try: 
        toilet_id = request.args.get('toilet_id')
    
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM toilets WHERE toilet_id = %s", (toilet_id,))
        toilet = cursor.fetchone()

        if not toilet:
            return jsonify({"success": False, "message": "Toilet not found"}), 404

        cursor.execute("DELETE FROM toilets WHERE toilet_id = %s", (toilet_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Toilet deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "An error occurred",
            "error": str(e)
        }), 500
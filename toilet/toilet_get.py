from flask import request, jsonify

from config.dbconfig import get_connection
from . import toilet_bp

@toilet_bp.route("/toilet", methods=["GET"])
def get_toilet_details():
    toilet_id = request.args.get('toilet_id')
    
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM toilets WHERE toilet_id = %s", (toilet_id,))
    toilet_details = cursor.fetchone()

    if not toilet_details:
        return jsonify({"success": False, "message": "Toilet does not exist, check toilet_id"}), 404
    
    # Fetch all comments for the toilet
    cursor.execute("""
        SELECT tc.comment_text, tc.commented_at, u.first_name, u.last_name 
        FROM toilet_comments tc 
        JOIN users u ON tc.user_id = u.user_id
        WHERE tc.toilet_id = %s
        ORDER BY tc.commented_at DESC
    """, (toilet_id,))
    
    toilet_comments = cursor.fetchall()

    comments_list = [
        {
            "user": f"{row['first_name']} {row['last_name']}",
            "comment": row['comment_text'],
            "timestamp": row['commented_at'].strftime("%Y-%m-%d %H:%M:%S")
        }
        for row in toilet_comments
    ]
    
    # Fetch all features for the toilet
    cursor.execute("SELECT feature_name FROM toilet_features WHERE toilet_id = %s", (toilet_id,))
    features = cursor.fetchall()

    features_list = [row["feature_name"] for row in features]
    
    return jsonify({
        "success": True, 
        "message": "Toilet details fetched successfully", 
        "data": {
            "toilet_details": toilet_details,
            "comments": {
                "comments_list": comments_list,
                "count": len(comments_list)
            },
            "features": {
                "features_list": features_list,
                "count": len(features_list)
            }
        }
    }), 200

@toilet_bp.route("/toilets", methods=["GET"])
def get_all_toilets():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM toilets")
        toilets = cursor.fetchall()

        return jsonify({"success": True, "message": "All toilets fetched successfully", "data": toilets})
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "An error occurred",
            "error": str(e)
        }), 500

from flask import jsonify
from config.dbconfig import get_connection

def validate_request(*args):
    if not all([ args ]):
        print("Request body error!")
        return jsonify({"error": "Error in request body"}), 400
    return None

def validate_update_request(data, fields_not_allowed_to_update):
    print("Inside validate_update_request")
    for request_parameter in data.keys():
        if request_parameter in fields_not_allowed_to_update:
            print("fuck this field: ", request_parameter)
            return jsonify({"error": f"Cannot update field: {request_parameter}"}), 400

    return None

def fetch_user_id_from_email(email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT user_id FROM Users WHERE email = %s", (email,))
    user = cursor.fetchone()
    if not user:
        return False
    user_id = user[0]
    return user_id
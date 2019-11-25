from flask import Response


def generate_error_response(err_msg):
    return Response(err_msg, status=500, mimetype='application/json')

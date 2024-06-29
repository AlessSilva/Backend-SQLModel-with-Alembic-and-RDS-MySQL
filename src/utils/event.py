import decimal
import json


def handle_exception(e):

    status, response = 500, "Internal server error"

    for arg in e.args:
        if isinstance(arg, int):
            status = arg

        if isinstance(arg, str):
            response = {'message': arg}

        if isinstance(arg, dict):
            response = arg

    return status, response

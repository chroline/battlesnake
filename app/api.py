import json
import random
from bottle import HTTPResponse


def ping_response():
    return HTTPResponse(
        status=200
    )


def start_response():

    return {
        "color": random.choice(["#DBAF34", "#739071"]),
        "headType": "dead",
        "tailType": "shac-coffee"
    }


def move_response(move):
    assert move in ['up', 'down', 'left', 'right'], \
        "Move must be one of [up, down, left, right]"

    return {
        "move": move
    }


def end_response():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

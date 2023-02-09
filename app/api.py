import json
import random


def ping_response():
    return 200


def start_response():
    return {
      "apiversion": "1",
      "author": "",  # TODO: Your Battlesnake Username
      "color": "#888888",  # TODO: Choose color
      "head": "default",  # TODO: Choose head
      "tail": "default",  # TODO: Choose tail
  }


def move_response(move):
    assert move in ['up', 'down', 'left', 'right'], \
        "Move must be one of [up, down, left, right]"

    return {
        "move": move
    }


def end_response():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

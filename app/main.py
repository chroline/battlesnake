import io
import json
import os

from flask import Flask
from flask import request

from app.variables import *
from app.board import *
from app.logic import *
from app.api import ping_response, start_response, move_response, end_response


app = Flask("Battlesnake")


@app.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
    <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''


@app.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()


@app.post('/start')
def start():
    data = request.get_json()

    return start_response()


@app.post('/move')
def move():
    data = request.get_json()

    variables = Variables(data)
    board = Board(variables)
    move = decide_move(variables)

    print(f'move: {move}')
    print(f'health: {variables.you_health}')

    # board.print_board()

    return move_response(move)


@app.post('/end')
def end():
    data = request.get_json()

    return end_response()


host = "0.0.0.0"
port = int(os.environ.get("PORT", "8080"))

app.run(host=host, port=port)

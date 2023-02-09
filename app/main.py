import io
import json
import os
from flask import Flask, request
import time

from variables import *
from board import *
from logic import *
from api import ping_response, start_response, move_response, end_response


app = Flask("Battlesnake")


@app.route('/')
def index():
    return start_response()


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
  start_time = time.time()
  
  data = request.get_json()

  start_time = time.time()
  
  variables = Variables(data)

  print(variables.height)

  
  board = Board(variables)

  time1 = (time.time() - start_time)
  print("-1- %s seconds ---" % time1)
  
  start_time = time.time()
  
  move = decide_move(variables)

  print(f'move: {move}')
  print(f'health: {variables.you_health}')

  time2 = (time.time() - start_time)
  print("-2- %s seconds ---" % time2)

  time3 = time1 + time2
  print("-3- %s seconds ---" % time3)

  return move_response(move)


@app.post('/end')
def end():
    data = request.get_json()

    return end_response()


host = "0.0.0.0"
port = int(os.environ.get("PORT", "8080"))

app.run(host=host, port=port)

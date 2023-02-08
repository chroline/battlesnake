from collections import deque
import collections

from point import *


class Board:

    def __init__(self, variables):
        self.variables = variables
        self.create_empty_board()
        self.add_food()
        self.add_you()
        self.add_others()
        self.flood_flow_get_deadends()

        if variables.you_health < 10:
            self.add_food()

    def create_empty_board(self):
        height = self.variables.height
        width = self.variables.width

        board = []
        for h in range(height):
            board.append(['.'] * width)

        self.variables.board = board

    def add_food(self):
        food = self.variables.food
        board = self.variables.board

        for f in food:
            x_coord = f['x']
            y_coord = f['y']
            board[y_coord][x_coord] = 'F'

    def add_you(self):
        you_body = self.variables.you_body
        board = self.variables.board
        coords = set()
        duplicates = False

        for b in you_body:
            x_coord = b['x']
            y_coord = b['y']
            if (x_coord, y_coord) in coords:
                duplicates = True
            coords.add((x_coord, y_coord))
            board[y_coord][x_coord] = 'Y'

        head = you_body[0]
        head_x_coord = head['x']
        head_y_coord = head['y']
        board[head_y_coord][head_x_coord] = 'H'

        if (len(you_body) > 3) and not duplicates:
            tail = you_body[-1]
            tail_x_coord = tail['x']
            tail_y_coord = tail['y']
            board[tail_y_coord][tail_x_coord] = 'T'

    def add_others(self):
        snakes = self.variables.snakes
        you_body = self.variables.you_body
        you_id = self.variables.you_id
        width = self.variables.width
        height = self.variables.height
        board = self.variables.board
        you_size = len(you_body)

        for snake in snakes:
            if snake["id"] == you_id:
                continue

            coords = set()
            duplicates = False

            for b in snake["body"]:
                x_coord = b['x']
                y_coord = b['y']
                if (x_coord, y_coord) in coords:
                    duplicates = True
                coords.add((x_coord, y_coord))
                board[y_coord][x_coord] = 'o'

            head = snake["body"][0]
            head_x_coord = head['x']
            head_y_coord = head['y']
            board[head_y_coord][head_x_coord] = 'h'

            if not duplicates:
                tail = snake["body"][-1]
                tail_x_coord = tail['x']
                tail_y_coord = tail['y']
                board[tail_y_coord][tail_x_coord] = 't'

            if len(snake["body"]) >= you_size:
                for neighbor in Point(self.variables, head_x_coord, head_y_coord).get_neighbors():
                    board[neighbor.y][neighbor.x] = '*'

    def flood_flow_get_deadends(self):
        you_x = self.variables.you_x
        you_y = self.variables.you_y
        you_size = len(self.variables.you_body)
        safe = ['F', '.', 'T', 't', '!', 'h']
        point = Point(self.variables, you_x, you_y, safe)

        for possible_move in point.get_neighbors():
            points = collections.deque([possible_move])
            free_space = 0
            checked = list()
            distance_away = 0
            while len(points) > 0:
                current = points.popleft()
                distance_away += 1
                free_space += 1
                checked.append(current)
                neighbors = current.get_neighbors()
                if (not 'h' in neighbors) or (distance_away == 1):
                    for neighbor in neighbors:
                        if (not neighbor in checked) and (not neighbor in points) and (not neighbor.get_symbol() == 'h'):
                            points.append(neighbor)
                else:
                    free_space -= 1
            if free_space < (you_size + 1):
                if not self.variables.board[possible_move.y][possible_move.x] in ['T', 't']:
                    self.variables.board[possible_move.y][possible_move.x] = '!'

    def print_board(self):
        board = self.variables.board

        x_label = 1
        print("  ", end=" ")
        for coord in board[0]:
            if x_label < 10:
                print(x_label, end="  ")
            else:
                print(x_label, end=" ")
            x_label += 1
        print()

        y_label = 1
        for x in board:
            if y_label < 10:
                print(y_label, end="  ")
            else:
                print(y_label, end=" ")

            for coord in x:
                print(coord, end="  ")
            print()
            y_label += 1

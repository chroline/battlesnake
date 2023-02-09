import random
import collections

from a_star import get_food, chase_tail
from point import Point


def move_to_space(variables, safe=['F', '.', 'T']):
    you_x = variables.you_x
    you_y = variables.you_y
    point = Point(variables, you_x, you_y, safe)
    moves = dict()


    for possible_move in point.get_neighbors():
        points = collections.deque([possible_move])
        print(points)
        free_space = 0
        checked = list()
        while len(points) > 0:
            current = points.popleft()
            free_space += 1
            checked.append(current)
            for neighbor in current.get_neighbors():
                if (not neighbor in checked) and (not neighbor in points):
                    points.append(neighbor)
        moves[possible_move.direction] = free_space

    print(moves)

    best_move = list()
    best = 0
    for value in moves.values():
        if value > best:
            best = value
    for key in moves.keys():
        if moves[key] == best:
            best_move.append(key)
    if len(best_move) == 0:
        return best_move
    return random.choice(best_move)


def avoid_self_and_borders_randomly(variables, safe=['F', '.', 'T', 't']):
    print("avoid_self_and_borders_randomly")
    you_x = variables.you_x
    you_y = variables.you_y
    point = Point(variables, you_x, you_y, safe)
    directions = list()

    for neighbor in point.get_neighbors():
        directions.append(neighbor.direction)

    if len(directions) == 0:
        return directions
    return random.choice(directions)


def favor_chase_tail(variables):
    '''
    # if at top wall, turn in direction of tail
    if variables.you_body[0]['y'] == 0 and variables.you_body[1]['y'] == 1:
        if variables.you_body[-1]['x'] < variables.you_body[0]['x']:
            return "left"
        if variables.you_body[-1]['x'] > variables.you_body[0]['x']:
            return "right"
    # if at left wall, turn in direction of tail
    if variables.you_body[0]['x'] == 0 and variables.you_body[1]['x'] == 1:
        if variables.you_body[-1]['y'] < variables.you_body[0]['y']:
            return "up"
        if variables.you_body[-1]['x'] > variables.you_body[0]['x']:
            return "down"

    # if at bottom wall, turn in direction of tail
    if variables.you_body[0]['y'] == variables.height - 1 and variables.you_body[0]['y'] == variables.you_body[1]['y']+1:
        if variables.you_body[-1]['x'] < variables.you_body[0]['x']:
            return "left"
        if variables.you_body[-1]['x'] > variables.you_body[0]['x']:
            return "right"
    # if at right wall, turn in direction of tail
    if variables.you_body[0]['x'] == variables.width - 1 and variables.you_body[0]['x'] == variables.you_body[1]['x']+1:
        if variables.you_body[-1]['y'] < variables.you_body[0]['y']:
            return "up"
        if variables.you_body[-1]['x'] > variables.you_body[0]['x']:
            return "down"
    '''

    if len(variables.you_body) <= 4:
        move = chase_tail(variables, ['F', '.', 'T', '!'])
    else:
        move = chase_tail(variables, ['.', 'T', '!'])

    if len(move) == 0:
        move = chase_tail(variables, ['F', '.', 'T', 't', '!'])
        if len(move) == 0:
            move = move_to_space(variables)
            if len(move) == 0:
                move = get_food(variables)
                if len(move) == 0:
                    move = get_food(variables, ['F', '.', 'T', 't', '!'])
                    if len(move) == 0:
                        move = avoid_self_and_borders_randomly(variables)
                        if len(move) == 0:
                            move = chase_tail(
                                variables, ['F', '.', 'T', 't', '!', '*'])
                            if len(move) == 0:
                                move = move_to_space(
                                    variables, ['F', '.', 'T', 't', '!', '*'])
                                if len(move) == 0:
                                    move = get_food(
                                        variables, ['F', '.', 'T', 't', '!', '*'])
                                    if len(move) == 0:
                                        move = avoid_self_and_borders_randomly(
                                            variables, ['F', '.', 'T', 't', '!', '*'])
    return move


def heavily_favor_get_food(variables):
    print("heavily_favor_get_food")
    move = get_food(variables)
    if len(move) == 0:
        move = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
        if len(move) == 0:
            move = chase_tail(variables)
            if len(move) == 0:
                move = move_to_space(variables)
                if len(move) == 0:
                    move = chase_tail(
                        variables, ['F', '.', 'T', 't', '!', '*'])
                    if len(move) == 0:
                        move = avoid_self_and_borders_randomly(variables)
                        if len(move) == 0:
                            move = move_to_space(
                                variables, ['F', '.', 'T', 't', '!', '*'])
                            if len(move) == 0:
                                move = avoid_self_and_borders_randomly(
                                    variables, ['F', '.', 'T', 't', '!', '*'])
    return move


def favor_get_food(variables):
    print("favor_get_food")
    move = get_food(variables)
    if len(move) == 0:
        move = chase_tail(variables)
        if len(move) == 0:
            move = move_to_space(variables)
            if len(move) == 0:
                move = avoid_self_and_borders_randomly(variables)
                if len(move) == 0:
                    move = get_food(variables, ['F', '.', 'T', 't', '!', '*'])
                    if len(move) == 0:
                        move = chase_tail(
                            variables, ['F', '.', 'T', 't', '!', '*'])
                        if len(move) == 0:
                            move = move_to_space(
                                variables, ['F', '.', 'T', 't', '!', '*'])
                            if len(move) == 0:
                                move = avoid_self_and_borders_randomly(
                                    variables, ['F', '.', 'T', 't', '!', '*'])
    return move


def decide_move(variables):
    board = variables.board
    height = variables.height
    width = variables.width
    you_x = variables.you_x
    you_y = variables.you_y
    you_health = variables.you_health
    you_body = variables.you_body
    snakes = variables.snakes
    you_id = variables.you_id
    you_size = len(you_body)

    can_chase_tail = True
    """ for snake in snakes:
        if len(snake["body"]) >= you_size:
            if snake["id"] != you_id:
                can_chase_tail = False
                break """

    if (you_health >= 75) and can_chase_tail:
        move = favor_chase_tail(variables)
        if move in ['up', 'down', 'left', 'right']:
            return move
    elif you_health <= 25:
        move = heavily_favor_get_food(variables)
        if move in ['up', 'down', 'left', 'right']:
            return move
    else:
        move = favor_get_food(variables)
        if move in ['up', 'down', 'left', 'right']:
            return move

    return random.choice(['up', 'down', 'left', 'right'])

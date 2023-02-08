import collections

from point import *


def a_star(variables, target, safe):
    board = variables.board
    you_x = variables.you_x
    you_y = variables.you_y
    height = variables.height
    width = variables.width
    _open = collections.deque([Point(variables, you_x, you_y, safe)])
    closed = set()

    while True:
        try:
            top = _open.popleft()
        except:
            return []
        if top.get_symbol() == target:
            break
        closed.add(top)
        neighbors = top.get_neighbors()
        for neighbor in neighbors:
            in_open, in_closed = False, False
            for value in tuple(_open):
                if value == neighbor:
                    if value.rank > neighbor.rank:
                        _open.remove(value)
                    else:
                        in_open = True
            for value in tuple(closed):
                if value == neighbor:
                    if value.rank > neighbor.rank:
                        closed.remove(value)
                    else:
                        in_closed = True
            if (not in_open) and (not in_closed):
                _open.append(neighbor)
    return top.get_move()


def get_food(variables, safe=['F', '.']):
    return a_star(variables, 'F', safe)


def chase_tail(variables, safe=['F', '.', 'T', '!']):
    return a_star(variables, 'T', safe)

import numpy as np
from enum import Enum

class status(Enum):
    empty = 0
    obstacle = 1
    apple = 2
    snake = 3
    snake_head = 4

def statusToChar(e):
    if e == status.empty:
        return '.'
    elif e == status.obstacle:
        return 'X'
    elif e == status.apple:
        return 'o'
    elif e == status.snake:
        return 's'
    elif e == status.snake_head:
        return 'S'
    else:
        print("ERROR in statusToChar")

class direction(Enum):
    left = 0
    right = 1
    up = 2
    down = 3

def directionToArray(d):
    if d == direction.left:
        return np.array([0,-1])
    elif d == direction.right:
        return np.array([0,1])
    elif d == direction.up:
        return np.array([-1,0])
    elif d == direction.down:
        return np.array([1,0])
    else:
        print("ERROR in directionToArray")

def directionToString(d):
    if d == direction.left:
        return 'left '
    elif d == direction.right:
        return 'right'
    elif d == direction.up:
        return 'up   '
    elif d == direction.down:
        return 'down '
    else:
        print("ERROR in directionToString")

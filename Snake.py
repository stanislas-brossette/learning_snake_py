import numpy as np
from enums import *

class Node:
    def __init__(self, pos, next=None):
        self.pos_ = pos
        self.next_ = next

class Snake:
    def __init__(self, x, y, d=direction.right):
        self.head_ = Node(np.array([x,y]))
        self.direction_ = d
        self.length_ = 1
        self.alive_ = True
        self.view_distance_ = 2

    def isAlive(self):
        return self.alive_

    def move_forward(self, world):
        if not self.alive_:
            return -100
        score_move = 0
        prevPos = self.head_.pos_
        nextPos = prevPos + directionToArray(self.direction_)
        nextPosContent = world.content_[nextPos[0], nextPos[1]]
        if(nextPosContent == status.empty):
            score_move = -0.1
            self.head_.pos_ = prevPos + directionToArray(self.direction_)
            n = self.head_
            while(n.next_):
                savePos = n.next_.pos_
                n.next_.pos_ = prevPos
                prevPos = savePos
                n = n.next_
        elif(nextPosContent == status.apple):
            score_move = 100
            previousHead = Node(self.head_.pos_, self.head_.next_)
            self.head_.next_ = previousHead
            self.head_.pos_ = nextPos
            self.length_ = self.length_ + 1
            world.changeAppleLocation(nextPos)
        elif(nextPosContent == status.obstacle
                or nextPosContent == status.snake
                or nextPosContent == status.snake_head):
            score_move = -100
            #print('die')
            self.alive_ = False
            self.length_ = 0
        return score_move

    def turn(self, d):
        if isinstance(d,direction):
            if d == oppositeDirection(self.direction_):
                self.alive_ = False
                self.length_ = 0
            self.direction_ = d

    def display(self):
        print("Snake")
        n = self.head_
        print(n.pos_)
        while(n.next_):
            n = n.next_
            print(n.pos_)

    def get_view(self, world):
        vd = self.view_distance_
        view_size = 2*vd + 1
        view = np.full((view_size, view_size), status.empty)
        for i in range(view_size):
            for j in range(view_size):
                x = self.head_.pos_[0] - vd + i
                y = self.head_.pos_[1] - vd + j
                if(x < 0 or y < 0
                        or x >= world.height_
                        or y >= world.width_):
                    view[i,j] = status.obstacle
                else:
                    view[i,j] = world.content_[x,y]
        return view



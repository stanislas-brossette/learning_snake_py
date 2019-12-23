import numpy as np
from enums import direction, status, directionToArray

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

    def isAlive(self):
        return self.alive_

    def move_forward(self, world):
        prevPos = self.head_.pos_
        nextPos = prevPos + directionToArray(self.direction_)
        nextPosContent = world.content_[nextPos[0], nextPos[1]]
        if(nextPosContent == status.empty):
            self.head_.pos_ = prevPos + directionToArray(self.direction_)
            n = self.head_
            while(n.next_):
                savePos = n.next_.pos_
                n.next_.pos_ = prevPos
                prevPos = savePos
                n = n.next_
        elif(nextPosContent == status.apple):
            previousHead = Node(self.head_.pos_, self.head_.next_)
            self.head_.next_ = previousHead
            self.head_.pos_ = nextPos
            self.length_ = self.length_ + 1
            world.changeAppleLocation(nextPos)
        elif(nextPosContent == status.obstacle
                or nextPosContent == status.snake
                or nextPosContent == status.snake_head):
            self.alive_ = False

    def turn(self, d):
        if isinstance(d,direction):
            self.direction_ = d

    def display(self):
        print("Snake")
        n = self.head_
        print(n.pos_)
        while(n.next_):
            n = n.next_
            print(n.pos_)

        
        

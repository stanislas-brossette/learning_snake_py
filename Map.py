import numpy as np
import time
from enums import *
from Snake import Snake
from matplotlib import pyplot as plt


class Map:
    """ Map in which the snake evolves"""
    def __init__(self, height, width, n_apples, render=False):
        self.height_ = height 
        self.width_ = width
        self.n_apples_ = n_apples
        self.apples_ = np.zeros((self.n_apples_,2))
        self.render_ = render
        self.resetContent()
        self.randomizeApples()
        self.resetContent()
        if self.render_:
            contentFloat = np.array([[statusToFloat(si) for si in ri] for ri in self.content_])
            plt.ion()
            self.fig_ = plt.figure()
            self.ax_ = self.fig_.add_subplot(111)
            self.im_ = self.ax_.imshow(contentFloat)
            self.fig_.canvas.draw()
            plt.pause(0.001)

    def render(self):
        if self.render_:
            contentFloat = np.array([[statusToFloat(si) for si in ri] for ri in self.content_])
            self.im_.set_data(contentFloat)
            self.fig_.canvas.draw()
            plt.pause(0.001)


    def randomizeApples(self):
        self.apples_ = np.zeros((self.n_apples_,2))
        for i in range(self.n_apples_):
            foundLocation = False
            while(not foundLocation):
                x = np.random.randint(0,self.height_)
                y = np.random.randint(0,self.width_)
                if(self.content_[x,y] == status.empty):
                    foundLocation = True
            self.apples_[i,0] = x
            self.apples_[i,1] = y
    
    def changeAppleLocation(self, applePos):
        for a in self.apples_:
            if (a == applePos).all():
                foundLocation = False
                while(not foundLocation):
                    x = np.random.randint(0,self.height_)
                    y = np.random.randint(0,self.width_)
                    if(self.content_[x,y] == status.empty):
                        foundLocation = True
                a[0] = x
                a[1] = y


    def resetContent(self):
        self.content_ = np.full((self.height_, self.width_), status.empty)
        self.content_[:, 0] = status.obstacle
        self.content_[:,-1] = status.obstacle
        self.content_[0, :] = status.obstacle
        self.content_[-1,:] = status.obstacle
        for apple in self.apples_:
            self.content_[apple[0].astype(int), apple[1].astype(int)] = status.apple

    #def render(self):
    #    sToPrint = ''
    #    for row in self.content_:
    #        for e in row:
    #            sToPrint = sToPrint + statusToChar(e)
    #        sToPrint = sToPrint + '\n'
    #    print(sToPrint)


    def update(self, snake):
        self.resetContent()
        n = snake.head_
        self.content_[n.pos_[0], n.pos_[1]] = status.snake_head
        while(n.next_):
            n = n.next_
            self.content_[n.pos_[0], n.pos_[1]] = status.snake



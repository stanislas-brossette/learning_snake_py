import numpy as np
from curtsies import Input
from Map import Map
from Snake import Snake
from enums import *
from State import State, Transition

class Game:
    def __init__(self, width, length, n_apples, snake_x0, snake_y0, d=direction.right, render=False):
        self.width_ = width
        self.length_ = length
        self.n_apples_ = n_apples
        self.snake_x0_ = snake_x0
        self.snake_y0_ = snake_y0
        self.snake_ = None
        self.direction_ = d
        self.score_ = 0
        self.render_ = render
        self.reset()

        if self.render_:
            self.render()

    def reset(self):
        self.world_ = Map(self.width_, self.length_, self.n_apples_, self.render_)
        self.snake_x0_ = 1 + np.random.randint(self.length_-2)
        self.snake_y0_ = 1 + np.random.randint(self.width_-2)
        self.direction_ = direction(np.random.randint(4))
        self.snake_ = Snake(self.snake_x0_, self.snake_y0_, self.direction_)
        self.world_.update(self.snake_)
        self.score_ = 0
        s = State(self.snake_, self.world_)
        s_array = np.concatenate((s.to_array(), [self.snake_.length_], directionToArray(self.snake_.direction_)))
        return s_array

    def render(self):
        self.world_.render()

    def step(self, d):
        t = Transition()
        t.state_ = State(self.snake_, self.world_)
        t.direction_ = d
        self.snake_.turn(d)
        score_move = self.snake_.move_forward(self.world_)
        self.world_.update(self.snake_)
        t.next_state_ = State(self.snake_, self.world_)
        #t.score_ = self.snake_.length_ - 1
        self.reward_ = self.snake_.length_ + score_move - 1
        #self.reward_ = score_move
        self.score_ = self.score_ + self.reward_

        state_array = np.concatenate((t.next_state_.to_array(), [self.snake_.length_], directionToArray(self.snake_.direction_)))
        if self.render_:
            #print('\n\nnew step')
            #print("self.snake_.length_:{}".format(self.snake_.length_))
            #print("directionToArray(self.snake_.direction_):{}".format(directionToArray(self.snake_.direction_)))
            #t.next_state_.render()
            self.render()
        return (state_array, self.reward_, not self.snake_.isAlive(), t.direction_)

    def get_direction_input(self):
        with Input(keynames='curses') as input_generator:
            for e in input_generator:
                if e == 'KEY_UP':
                    return direction.up
                elif e == 'KEY_DOWN':
                    return direction.down
                elif e == 'KEY_LEFT':
                    return direction.left
                elif e == 'KEY_RIGHT':
                    return direction.right
                else:
                    print(e)
        

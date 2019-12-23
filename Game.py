from curtsies import Input
from Map import Map
from Snake import Snake
from enums import direction
from State import State, Transition

class Game:
    def __init__(self, width, length, n_apples, snake_x0, snake_y0, d=direction.right, render=False):
        self.width_ = width
        self.length_ = length
        self.n_apples_ = n_apples
        self.snake_x0_ = snake_x0
        self.snake_y0_ = snake_y0
        self.direction_ = d
        self.render_ = render
        self.reset()

        if self.render_:
            self.render()

    def reset(self):
        self.world_ = Map(self.width_, self.length_, self.n_apples_, self.render_)
        self.snake_ = Snake(self.snake_x0_, self.snake_y0_, self.direction_)
        self.world_.update(self.snake_)
        s = State(self.snake_, self.world_)
        s_array = s.to_array()
        return s_array

    def render(self):
        self.world_.render()

    def step(self, d):
        t = Transition()
        t.state_ = State(self.snake_, self.world_)
        t.direction_ = d
        self.snake_.turn(d)
        self.snake_.move_forward(self.world_)
        self.world_.update(self.snake_)
        t.next_state_ = State(self.snake_, self.world_)
        t.score_ = self.snake_.length_ - 1
        if self.render_:
            self.render()
        #print("not self.snake_.isAlive():{}".format(not self.snake_.isAlive()))
        return (t.next_state_.to_array(), t.score_, not self.snake_.isAlive(), t.direction_)

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
        

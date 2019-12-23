from curtsies import Input
from Map import Map
from Snake import Snake
from enums import direction

class Game:
    def __init__(self, width, length, n_apples, snake_x, snake_y, d=direction.right):
        self.world_ = Map(width, length, n_apples)
        self.snake_ = Snake(snake_x, snake_y, d)
        self.world_.update(self.snake_)
        self.display()

    def display(self):
        self.world_.display()

    def step(self, d):
        self.snake_.direction_ = d
        self.snake_.move_forward(self.world_)
        self.world_.update(self.snake_)

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
        

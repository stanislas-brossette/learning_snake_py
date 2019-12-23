from Map import Map
from Snake import Snake
from enums import direction
from curtsies import Input

from Game import Game

game = Game(30,30,4,15,15)
while(game.snake_.isAlive()):
    d = game.get_direction_input()
    game.step(d)
    game.display()


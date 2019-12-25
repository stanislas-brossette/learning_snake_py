from Map import Map
from Snake import Snake
from enums import direction
from curtsies import Input

from Game import Game

print("direction(0):{}".format(direction(0)))

game = Game(30,30,4,15,15,render=True)
while(game.snake_.isAlive()):
    print("game.snake_.direction_:{}".format(game.snake_.direction_))
    d = game.get_direction_input()
    game.step(d)
    game.render()


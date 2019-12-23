from Map import Map
from Snake import Snake
from enums import status, statusToChar, directionToString

class State:
    def __init__(self, snake, world):
        self.length_ = snake.length_
        self.view_ = snake.get_view(world)

    def to_string(self):
        sToPrint = ''
        for row in self.view_:
            for e in row:
                sToPrint = sToPrint + statusToChar(e)
            sToPrint = sToPrint + '\n'
        return sToPrint
        
    def display(self):
        print(self.to_string())

class Transition:
    def __init__(self):
        self.state_ = None
        self.direction_ = None
        self.next_state_ = None
        self.score_ = None

    def to_string(self):
        s_state = self.state_.to_string()
        s_next_state = self.next_state_.to_string()
        split_state = s_state.split('\n')
        split_next_state = s_next_state.split('\n')
        res = ''
        emptyLargePad = '           '
        emptySmallPad = '   '
        for i, s in enumerate(split_state):
            res = res + split_state[i]
            if i == 0:
                res = res + emptySmallPad + directionToString(self.direction_) + emptySmallPad
            elif i == 1:
                scoreStr = str(self.score_)
                scoreStr = scoreStr.ljust(5, ' ')
                res = res + emptySmallPad + scoreStr + emptySmallPad
            else:
                res = res + emptyLargePad
            res = res + split_next_state[i] + '\n'
        return res

    def display(self):
        s = self.to_string()
        print(s)
        #self.state_.display()
        #print("self.direction_:{}".format(self.direction_))
        #self.next_state_.display()
        #print("self.score_:{}".format(self.score_))

        

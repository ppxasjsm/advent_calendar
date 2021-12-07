import numpy as np


class Navigation:

    def __init__(self, starting_position):
        self.initial_position = starting_position #dictionary
        self._current_position = starting_position
        print(self.initial_position)

    def move_up(self, distance):
        position = self.current_position
        position['depth'] = position['depth'] - distance
        self.current_position = position

    def move_down(self, distance):
        position = self.current_position
        position['depth'] = position['depth'] + distance
        self.current_position = position

    def move_forward(self, distance):
        position = self.current_position
        position['forward'] = position['forward'] + distance
        self.current_position = position

    @property
    def current_position(self):
        """Current position of boat"""
        return self._current_position

    @current_position.setter
    def current_position(self, value):
        self._current_position = value

if __name__ == '__main__':
    initial_position = {'depth': 0, 'forward': 0}
    boat = Navigation(initial_position)
    f = open('data.txt')
    lines = f.readlines()
    f.close()

    for l in lines:
        info = l.strip().split(' ')
        if info[0] == 'forward':
            print('moving forward')
            boat.move_forward(int(info[1]))
        if info[0] == 'up':
            print('moving up')
            boat.move_up(int(info[1]))
        if info[0] == 'down':
            boat.move_down(int(info[1]))
    print(f'position is: {boat.current_position}')
    curr_pos = boat.current_position
    multiplied = curr_pos['depth']*curr_pos['forward']
    print(f'multiplied position: {multiplied}')

from configuration import (MIN_BOARD_LENGTH, MIN_BOARD_WIDTH,
                           DEFAULTS_BOARD_LENGTH, DEFAULTS_BOARD_WIDTH,
                           MAX_BOARD_LENGTH, MAX_BOARD_WIDTH)


class Board():
    def __init__(self, length=DEFAULTS_BOARD_LENGTH, width=DEFAULTS_BOARD_WIDTH):
        self._validate(length, width)
        self._length = int(length)
        self._width = int(width)
        pass

    def _validate(self, length, width):
        try:
            if int(length) != float(length):
                raise ValueError('Length cannot be a floating point number')
            if int(length) % 2 == 0:
                raise ValueError('Length cannot be an even number')
            if int(length) < MIN_BOARD_LENGTH or int(length) > MAX_BOARD_LENGTH:
                raise ValueError('Length out of range')
            if int(width) != float(width):
                raise ValueError('Width cannot be a floating point number')
            if int(width) % 2 == 0:
                raise ValueError('Width cannot be an even number')
            if int(width) < MIN_BOARD_WIDTH or int(width) > MAX_BOARD_WIDTH:
                raise ValueError('Width out of range')
        except ValueError:
            raise ValueError('Invalid input')

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

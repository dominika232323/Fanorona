from configuration import (MIN_BOARD_LENGTH, MIN_BOARD_WIDTH,
                           DEFAULTS_BOARD_LENGTH, DEFAULTS_BOARD_WIDTH,
                           MAX_BOARD_LENGTH, MAX_BOARD_WIDTH)


class BoardSizeError(ValueError):
    pass


class Board():
    def __init__(self, length=DEFAULTS_BOARD_LENGTH, width=DEFAULTS_BOARD_WIDTH):
        self._validate(length, width)
        self._length = int(length)
        self._width = int(width)
        pass

    def _validate(self, length, width):
        try:
            if int(length) != float(length):
                raise BoardSizeError('Length cannot be a floating point number')
            if int(length) % 2 == 0:
                raise BoardSizeError('Length cannot be an even number')
            if int(length) < MIN_BOARD_LENGTH or int(length) > MAX_BOARD_LENGTH:
                raise BoardSizeError('Length out of range')
            if int(width) != float(width):
                raise BoardSizeError('Width cannot be a floating point number')
            if int(width) % 2 == 0:
                raise BoardSizeError('Width cannot be an even number')
            if int(width) < MIN_BOARD_WIDTH or int(width) > MAX_BOARD_WIDTH:
                raise BoardSizeError('Width out of range')
        except ValueError:
            raise BoardSizeError('Invalid input')

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width
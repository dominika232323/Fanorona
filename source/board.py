from source.constants import (
    MIN_BOARD_LENGTH,
    MIN_BOARD_WIDTH,
    DEFAULTS_BOARD_LENGTH,
    DEFAULTS_BOARD_WIDTH,
    MAX_BOARD_LENGTH,
    MAX_BOARD_WIDTH
)


class Board:
    """
    Class Board. Contains attributes:
    :param length: board's length, defaults to DEFAULTS_BOARD_LENGTH from constants
    :type length: int

    :param width: board's width, defaults to DEFAULTS_BOARD_LENGTH from constants
    :type width: int
    """
    def __init__(self, length=DEFAULTS_BOARD_LENGTH, width=DEFAULTS_BOARD_WIDTH):
        """
        Creates an instance of Board.
        """
        self._validate(length, width)
        self._length = int(length)
        self._width = int(width)

    @staticmethod
    def _validate(length, width):
        """
        :param length: board's length
        :param width: board's width
        :raise: BoardSizeError if length is an even number, less than MIN_BOARD_LENGTH from constants, greater
        than MAX_BOARD_LENGTH from constants or has an invalid type
        :raise: BoardSizeError if width is an even number, or less than MIN_BOARD_WIDTH from constants or greater
        than MAX_BOARD_WIDTH from constants or has an invalid type.
        """
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
        """
        :return: board's length
        """
        return self._length

    @property
    def width(self):
        """
        :return: board's width
        """
        return self._width


class BoardSizeError(ValueError):
    pass

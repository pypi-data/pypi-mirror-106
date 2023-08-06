from typing import List, Tuple, TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from honu.display import Display

# Used for postions
X = 0
Y = 1


class WinCondition(Enum):
    GET_ALL_FLAGS = 'get_all_flags'
    CALC_OUTPUT = 'calculate_output'
    MODIFY_BOARD = 'modify_board'


class Tile(Enum):
    EMPTY = 'empty'

    WHITE = 'white'
    BLACK = 'black'
    GREY = 'grey'
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    PURPLE = 'purple'
    BROWN = 'brown'


class Player():
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos


class Flag():
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos


class Game():
    def __init__(self, level: List[List[Tile]], player: Player, flags: List[Flag]):
        self.level = level
        self.width = len(level[0]) if len(level) > 0 else 0
        self.height = len(level)
        self.player = player
        self.flags = flags
        # Clear flags if present
        self.__remove_flags_if_below()
        self._observers: List['Display'] = []
        # Used by the user to output values
        self.output = None

    def debug_print(self):
        for row in self.level:
            tile_string = []
            for tile in row:
                tile_string.append(tile.value)
            print(tile_string)
        print(f'player: {self.player.pos[X]},{self.player.pos[Y]}')
        print(
            f'flags: {", ".join([",".join([str(flag.pos[X]), str(flag.pos[Y])]) for flag in self.flags])}')

    def __remove_flags_if_below(self) -> None:
        for flag in self.flags:
            if flag.pos[X] == self.player.pos[X] and flag.pos[Y] == self.player.pos[Y]:
                self.flags.remove(flag)

    def _add_observer(self, observer: 'Display') -> None:
        self._observers.append(observer)

    def update_display(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def write_below(self, tile: Tile) -> None:
        self.level[self.player.pos[Y]][self.player.pos[X]] = tile
        self.update_display()

    def read_below(self) -> Tile:
        return self.level[self.player.pos[Y]][self.player.pos[X]]

    def get_pos(self) -> Tuple[int, int]:
        return self.player.pos

    def move(self, translation: Tuple[int, int]) -> bool:
        new_pos: Tuple[int, int] = (
            self.player.pos[X]+translation[X], self.player.pos[Y]+translation[Y])

        is_out_of_x = not 0 <= new_pos[X] <= self.width - 1
        is_out_of_y = not 0 <= new_pos[Y] <= self.height - 1
        if is_out_of_x or is_out_of_y:
            return False
        
        is_on_empty_tile = self.level[new_pos[Y]][new_pos[X]] == Tile.EMPTY
        if is_on_empty_tile:
            return False
        else:
            self.player.pos = new_pos
            self.__remove_flags_if_below()
            self.update_display()
            return True

    def up(self) -> bool:
        return self.move((0, -1))

    def down(self) -> bool:
        return self.move((0, 1))

    def left(self) -> bool:
        return self.move((-1, 0))

    def right(self) -> bool:
        return self.move((1, 0))

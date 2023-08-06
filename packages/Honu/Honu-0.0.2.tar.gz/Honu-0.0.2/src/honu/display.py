from honu.game import Tile
from honu.graphics import GraphWin, Rectangle, Point, Text, Image  # type: ignore
from honu.static.sprites import SPRITE_SIZE_PX
from math import floor
from typing import List, Tuple, TYPE_CHECKING
from time import sleep
from pkg_resources import resource_string

if TYPE_CHECKING:
    from honu.game import Game

TURTLE_MOVEMENT_FRAMES = 20
TURTLE_MOVEMENT_SLEEP = 0.01


class TileGraphic():
    def __init__(self, win, start_x, start_y, end_x, end_y, fill):
        self.fill = fill
        self.win = win
        self.rect = Rectangle(Point(start_x, start_y), Point(end_x, end_y))
        if fill == Tile.EMPTY.value:
            # Don't draw tile
            self.rect.setOutline('')
        else:
            self.rect.setFill(fill)
        self.rect.draw(self.win)

    def set_fill(self, fill):
        self.fill = fill
        self.rect.setFill(fill)


class TurtleGraphic():
    sprite = resource_string('honu.static.sprites','turtle.png')

    def __init__(self, win, center_x, center_y, i, j, tile_size_px):
        self.win = win
        self.i = i
        self.j = j
        self.tile_size_px = tile_size_px

        self.image = Image(Point(center_x,center_y),SPRITE_SIZE_PX,SPRITE_SIZE_PX,TurtleGraphic.sprite,tile_size_px//SPRITE_SIZE_PX)

        self.image.draw(self.win)

    def move_to_tile(self, pos: Tuple[int, int]):
        x = (pos[0]-self.i)*self.tile_size_px
        y = (pos[1]-self.j)*self.tile_size_px
        # NOTE: May introduce rounding errors
        dx = x/TURTLE_MOVEMENT_FRAMES
        dy = y/TURTLE_MOVEMENT_FRAMES
        self._move_on_line(dx, dy)
        self.i = pos[0]
        self.j = pos[1]

    def _move_on_line(self, dx, dy):
        for i in range(TURTLE_MOVEMENT_FRAMES):
            self.image.move(dx, dy)
            sleep(TURTLE_MOVEMENT_SLEEP)


class FlagGraphic():
    sprite = resource_string('honu.static.sprites','flag.png')

    def __init__(self, win, center_x, center_y, i, j, tile_size_px) -> None:
        self.win = win
        self.i = i
        self.j = j
        self.tile_size_px = tile_size_px

        self.image = Image(Point(center_x,center_y),SPRITE_SIZE_PX,SPRITE_SIZE_PX,FlagGraphic.sprite,tile_size_px//SPRITE_SIZE_PX)
        self.image.draw(self.win)

    def undraw(self) -> None:
        self.image.undraw()


class Display():
    def __init__(self, game: 'Game', width, height, sleep_time) -> None:
        game._add_observer(self)
        self.width = width
        self.height = height
        self.sleep_time = sleep_time

        self.level_height = len(game.level)
        if self.level_height == 0:
            raise Exception('The level cannot be empty!')
        self.level_width = len(game.level[0])

        self.tile_scale = self.calc_tile_scale()
        self.tile_size_px = self.tile_scale * SPRITE_SIZE_PX

        self.level_offset_x, self.level_offset_y = self.calc_level_offset()

        self.win = GraphWin('Kame Code', width, height)

        self.tile_graphics: List[List[TileGraphic]] = self.map_tiles_to_graphics(game)
        self.flag_graphics: List[FlagGraphic] = self.map_flags_to_graphics(game)
        self.turtle_graphics: TurtleGraphic = self.map_turtle_to_graphics(game)

    def calc_level_offset(self) -> Tuple[int, int]:
        y_offset = (self.height-self.level_height*self.tile_size_px)/2
        x_offset = (self.width-self.level_width*self.tile_size_px)/2
        return x_offset, y_offset

    def map_tiles_to_graphics(self, game: "Game") -> List[List[TileGraphic]]:
        mapped_graphics: List[List[TileGraphic]] = []
        for i, row in enumerate(game.level):
            mapped_row: List[TileGraphic] = []
            for j, tile in enumerate(row):
                start_x = j*self.tile_size_px+self.level_offset_x
                start_y = i*self.tile_size_px+self.level_offset_y
                end_x = start_x + self.tile_size_px
                end_y = start_y + self.tile_size_px
                print(tile)
                fill = tile.value
                tile_graphic = TileGraphic(
                    self.win, start_x, start_y, end_x, end_y, fill)
                mapped_row.append(tile_graphic)
            mapped_graphics.append(mapped_row)
        return mapped_graphics

    def map_flags_to_graphics(self, game: "Game") -> List[FlagGraphic]:
        flag_graphics: List[FlagGraphic] = []
        for flag in game.flags:
            i, j = flag.pos
            flag_x = (i+0.5) * \
                self.tile_size_px+self.level_offset_x
            flag_y = (j+0.5) * \
                self.tile_size_px+self.level_offset_y
            flag_graphics.append(FlagGraphic(
                self.win, flag_x, flag_y, i, j, self.tile_size_px))
        return flag_graphics

    def map_turtle_to_graphics(self, game: "Game") -> TurtleGraphic:
        i, j = game.player.pos
        turtle_x = (i+0.5) * \
            self.tile_size_px+self.level_offset_x
        turtle_y = (j+0.5) * \
            self.tile_size_px+self.level_offset_y
        return TurtleGraphic(self.win, turtle_x, turtle_y, i, j, self.tile_size_px)

    def calc_tile_scale(self) -> int:
        """
        Calculates the scaling factor of the sprites
        """
        return max(1,
                   floor(min(self.width/self.level_width, self.height /
                         self.level_height)/SPRITE_SIZE_PX)
                   )

    def update(self, observable_game: 'Game') -> None:

        for i in range(len(self.tile_graphics)):
            for j in range(len(self.tile_graphics[i])):
                tile: TileGraphic = self.tile_graphics[i][j]
                if tile.fill != observable_game.level[i][j].value:
                    tile.set_fill(observable_game.level[i][j].value)

        flag_coords = {
            f'{flag.pos}' for flag in observable_game.flags}

        remove_list: List[FlagGraphic] = []
        for flag_graphic in self.flag_graphics:
            if f'{(flag_graphic.i, flag_graphic.j)}' not in flag_coords:
                flag_graphic.undraw()
                remove_list.append(flag_graphic)

        for flag_graphic in remove_list:
            self.flag_graphics.remove(flag_graphic)

        self.turtle_graphics.move_to_tile(
            observable_game.player.pos)

        self.pause()

    def pause(self):
        """
        Pause for a given amount of time.
        """
        sleep(self.sleep_time)

    def prompt_close(self):
        message = Text(Point(self.win.getWidth()/2, 20), 'Click anywhere to quit.')
        message.draw(self.win)
        self.win.getMouse()
        self.win.close()

    def close(self):
        self.win.close()

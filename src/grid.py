import graphics

from index import *
from defs import *
from chunk import Chunk
from sfml.graphics import RectangleShape, Color


class Grid(object):
    def __init__(self, width, height, graphics, resources):
        super(Grid, self).__init__()
        self.offest_x = 0
        self.offest_y = 0
        self.width = width
        self.height = height
        self.graphics = graphics
        self.resources = resources

        self.grid = []
        for i in range(0, width):
            self.grid.append(
                [EMPTY for j in range(0, height)]
            )

    def __getitem__(self, pos):
        x, y = pos
        return self.grid[x][y]

    def __setitem__(self, pos, v):
        x, y = pos
        self.grid[x][y] = v

    def load_chunk_data(self, chunk):
        for i in range(0, CHUNK_WIDTH):
            for j in range(0, CHUNK_HEIGHT):
                self[i, j] = chunk[i, j]

    def get_chunk_data(self):
        chunk = Chunk()
        for i in range(0, CHUNK_WIDTH):
            for j in range(0, CHUNK_HEIGHT):
                chunk[i, j] = self[i, j]

        return chunk

    def offest(self, delta_x, delta_y):
        self.offest_x += delta_x
        self.offest_y += delta_y

    def left(self):
        return self.offest_x

    def right(self):
        return self.offest_x + self.width * BLOCK_SIZE

    def top(self):
        return self.offest_y

    def bottom(self):
        return self.offest_y + self.height * BLOCK_SIZE

    def locate(self, x, y):
        x -= self.offest_x
        y -= self.offest_y

        return (
            int(x / BLOCK_SIZE),
            int(self.height -  y / BLOCK_SIZE)
        )

    def draw(self, x, y, index):
        self.graphics.draw_texture(
            self.resources.get_resource_by_index(index),
            self.offest_x + BLOCK_SIZE * x,
            self.offest_y + BLOCK_SIZE * (self.height - y - 1),
            BLOCK_SIZE, BLOCK_SIZE
        )

    def render(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self[(i, j)] == EMPTY:
                    continue

                self.draw(i, j, self[(i, j)])

        if DEBUG_MODE:
            bound = RectangleShape()
            bound.outline_thickness = 4
            bound.outline_color = Color(255, 0, 0, 100)
            bound.fill_color = Color.TRANSPARENT
            bound.position = (self.left() + 4, self.top() + 4)
            bound.size = (
                self.right() - self.left() - 8,
                self.bottom() - self.top() - 8
            )
            self.graphics.window.draw(bound)

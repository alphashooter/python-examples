from typing import Optional, List

from time import sleep
from random import random

from common import graphics


class Field(object):
    def __init__(self, width: int, height: int):
        self.cells = []
        for y in range(height):
            self.cells.append([])
            for x in range(width):
                cell = Cell(self, x, y, random() < 0.25)
                self.cells[y].append(cell)
        self.width = width
        self.height = height

    def draw(self) -> None:
        graphics.clear()
        for row in self.cells:
            for cell in row:
                cell.draw()
        graphics.show()

    def update(self) -> None:
        for row in self.cells:
            for cell in row:
                cell.update()
        for row in self.cells:
            for cell in row:
                new = cell.next()
                if new:
                    self.cells[new.y][new.x] = new

    def get_cell(self, x: int, y: int) -> 'Cell':
        return self.cells[y % self.height][x % self.width]

    def get_neighbours(self, cell: 'Cell') -> List['Cell']:
        x, y = cell.x, cell.y

        result = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                neighbour = self.get_cell(i, j)
                if neighbour is cell:
                    continue
                result.append(neighbour)

        return result


class BasicCell(object):
    def __init__(self, field: Field, x: int, y: int, alive: bool):
        self.field = field
        self.x = x
        self.y = y
        self.alive = alive
        self.__next = None

    def draw(self) -> None:
        raise NotImplementedError()

    def update(self) -> None:
        raise NotImplementedError()

    def kill(self, next: Optional['BasicCell'] = None) -> None:
        if next is None:
            next = Cell(self.field, self.x, self.y, False)
        self.__next = next

    def next(self) -> Optional['BasicCell']:
        return self.__next


class Cell(BasicCell):
    def __init__(self, field: Field, x: int, y: int, alive: bool):
        BasicCell.__init__(self, field, x, y, alive)
        self.age = 0

    def draw(self) -> None:
        if not self.alive:
            return

        red = 0
        green = max(0xFF - self.age, 0x80)
        blue = 0
        color = '#%02x%02x%02x' % (red, green, blue)

        graphics.draw_circle(10 * self.x + 5, 10 * self.y + 5, 5, color)

    def update(self) -> None:
        self.age += 1

        neighbours = self.field.get_neighbours(self)
        alive = 0
        for neighbour in neighbours:
            if neighbour.alive:
                alive += 1

        if self.alive:
            if alive < 2 or alive > 3:
                self.kill()
        else:
            if alive == 3:
                next = Cell(self.field, self.x, self.y, True)
                self.kill(next)


graphics.window('Game of Life', 400, 300)

field = Field(40, 30)
while True:
    field.draw()
    field.update()
    sleep(0.100)

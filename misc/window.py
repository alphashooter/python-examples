from typing import Tuple
from tkinter import *


__all__ = 'Window',


class Window(object):
    def __init__(self, x: int, y: int, width: int, height: int, name=None):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        if name:
            self.__root.title(name)
        self.__closed = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.geometry(f'{width}x{height}{x:+d}{y:+d}')
        self.__root.resizable(False, False)
        self.__canvas = Canvas(self.__root, bd=0, bg='white', width=width, height=height)
        self.__canvas.pack()

    def draw_ellipse(self, pos: Tuple[float, float], size: Tuple[float, float], color: str = 'black'):
        x, y = pos
        w, h = size
        self.__canvas.create_oval(*map(round, (x, y, x+w, y+h)), fill=color, width=0)

    def draw_rectangle(self, pos: Tuple[float, float], size: Tuple[float, float], color: str = 'black'):
        x, y = pos
        w, h = size
        self.__canvas.create_rectangle(*map(round, (x, y, x + w, y + h)), fill=color, width=0)

    def draw_polygon(self, *points: Tuple[float, float], color: str = 'black'):
        self.__canvas.create_polygon(*map(round, [coord for point in points for coord in point]), fill=color, width=0)

    def clear(self):
        self.__canvas.destroy()
        self.__canvas = Canvas(self.__root, bd=0, bg='white', width=self.__width, height=self.__height)
        self.__canvas.pack()

    def update(self):
        self.__root.update()

    def close(self):
        self.__closed = True
        self.__root.quit()

    @property
    def closed(self):
        return self.__closed

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

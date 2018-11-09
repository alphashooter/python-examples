from typing import Union, Iterable
import tkinter as tk


_window = None
_root = None
_canvas = None  # type: tk.Canvas


class Point(object):
    __slots__ = 'x', 'y'

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __pos__(self):
        return Point(self.x, self.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, other: 'Point') -> 'Point':
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: 'Point') -> 'Point':
        if not isinstance(other, Point):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: 'Point') -> 'Point':
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other: 'Point') -> 'Point':
        if not isinstance(other, Point):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other: Union[int, float, 'Point']) -> Union[float, 'Point']:
        if not isinstance(other, (float, int, Point)):
            return NotImplemented
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        return Point(other * self.x, other * self.y)

    def __rmul__(self, other: Union[int, float, 'Point']) -> Union[float, 'Point']:
        if not isinstance(other, (float, int, Point)):
            return NotImplemented
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        return Point(other * self.x, other * self.y)

    def __imul__(self, other: Union[int, float]) -> 'Point':
        if not isinstance(other, (float, int)):
            return NotImplemented
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other: Union[int, float]) -> 'Point':
        if not isinstance(other, (float, int)):
            return NotImplemented
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other: Union[int, float]) -> 'Point':
        if not isinstance(other, (float, int)):
            return NotImplemented
        self.x /= other
        self.y /= other
        return self

    def normalize(self, length: float = 1) -> 'Point':
        divisor = self.length
        if divisor == 0:
            return Point(self.x, self.y)
        multiplier = length / divisor
        return multiplier * self

    @property
    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


def _init(title: str = '', width: int = 400, height: int = 300) -> bool:
    global _window, _root, _canvas

    if _window is not None:
        return False

    _window = tk.Tk()
    _window.title(title)
    _window.geometry('%dx%d' % (width, height))

    _root = tk.Frame(_window, bg='white')
    _root.place(x=0, y=0, width=width, height=height)

    _canvas = tk.Canvas(_root)
    _canvas.place(x=0, y=0, width=width, height=height)


def clear() -> None:
    """
    Clear screen.

    :return:
    """
    _init()
    _canvas.delete('all')


def configure(title: str, width: int, height: int) -> None:
    """
    Configure Tk window.

    :param title: Window title
    :param width: Window width
    :param height: Window height
    :return:
    """
    if _init(title, width, height):
        return
    _window.title(title)
    _window.geometry('%dx%d' % (width, height))
    _root.place(x=0, y=0, width=width, height=height)
    _canvas.place(x=0, y=0, width=width, height=height)


def draw_line(start: Point, end: Point, width: float = 1, color: str = 'black') -> None:
    """
    Draw line.

    :param start: Position of line's start
    :param end: Position of line's end
    :param width: Line width
    :param color: Fill color
    :return:
    """
    _init()
    _canvas.create_line(start.x, start.y, end.x, end.y, width=width, fill=color)


def draw_rect(top_left: Point, bottom_right: Point, color: str = 'black', outline: str = 'black') -> None:
    """
    Draw rectangle.

    :param top_left: Position of rectangle's top-left corner
    :param bottom_right: Position of rectangle's bottom-right corner
    :param color: Fill color
    :param outline: Outline color
    :return:
    """
    _init()
    _canvas.create_rectangle(top_left.x, top_left.y, bottom_right.x, bottom_right.y, fill=color, outline=outline)


def draw_ellipse(top_left: Point, bottom_right: Point, color: str = 'black', outline: str = 'black') -> None:
    """
    Draw ellipse.

    :param top_left: Position of ellipse's top-left bound.
    :param bottom_right: Position of ellipse's bottom-right bound.
    :param color: Fill color
    :param outline: Outline color
    :return:
    """
    _init()
    _canvas.create_oval(top_left.x, top_left.y, bottom_right.x, bottom_right.y, fill=color, outline=outline)


def draw_polygon(points: Iterable[Point], color: str = 'black', outline: str = 'black') -> None:
    """
    Draw polygon.

    :param points: Collection of polygon's points.
    :param color: Fill color
    :param outline: Outline color
    :return:
    """
    _init()
    args = []
    for point in points:
        args.append(point.x)
        args.append(point.y)
    _canvas.create_polygon(*args, fill=color, outline=outline)


def show():
    """
    Update screen.
    :return:
    """
    _init()
    _window.update_idletasks()
    _window.update()

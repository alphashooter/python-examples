import tkinter as _tk


_window = None
_root = None
_canvas = None  # type: _tk.Canvas


def _init():
    global _window, _root, _canvas

    if _window is not None:
        return

    _window = _tk.Tk()
    _window.title('')
    _window.geometry('400x300')

    _root = _tk.Frame(_window, bg='white')
    _root.place(x=0, y=0, width=400, height=300)

    _canvas = _tk.Canvas(_root)
    _canvas.place(x=0, y=0, width=400, height=300)


def clear():
    global _canvas
    _init()
    _canvas.delete('all')


def window(title, width, height):
    _init()
    _window.title(title)
    _window.geometry('%dx%d' % (width, height))
    _root.place(x=0, y=0, width=width, height=height)
    _canvas.place(x=0, y=0, width=width, height=height)


def draw_line(x1, y1, x2, y2, width=1, color='black'):
    _init()
    _canvas.create_line(x1, y1, x2, y2, width=width, fill=color)


def draw_rect(x1, y1, x2, y2, color='black', outline='black'):
    _init()
    _canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline)


def draw_circle(x, y, radius, color='black', outline='black'):
    _init()
    _canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline=outline)


def show():
    _init()
    _window.update_idletasks()
    _window.update()

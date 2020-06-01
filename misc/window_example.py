from time import time, sleep
from math import sin, cos, pi
from misc.window import Window

window = Window(100, 100, 800, 600)  # create window 800x600 at (100, 100)
fps = 60  # frames per second/updates per second
radius = 50
center = (400, 300)
frame = 0

while not window.closed:
    # frame start
    start = time()
    window.clear()  # clear window before redraw
    frame += 1

    # redraw frame
    angle = ((0.01 * frame) % 2) * pi  # radians
    offset = 100 * (1 + cos(2 * angle))
    point1 = (center[0] + offset * cos(angle) - radius, center[1] + offset * sin(2 * angle) - radius)  # (x, y)
    point2 = (center[0] - offset * cos(angle) - radius, center[1] - offset * sin(2 * angle) - radius)  # (x, y)
    size = (2 * radius, 2 * radius)  # (width, height)
    if angle < pi:
        window.draw_ellipse(point1, size, color='green')
        window.draw_rectangle(point2, size, color='#0000ff')  # https://ru.wikipedia.org/wiki/RGB
    else:  # reversed order
        window.draw_rectangle(point2, size, color='#0000ff')  # https://ru.wikipedia.org/wiki/RGB
        window.draw_ellipse(point1, size, color='green')
    window.update()  # flush draw commands

    # normalize fps
    pause = 1 / fps - (time() - start)
    if pause > 0:
        sleep(pause)

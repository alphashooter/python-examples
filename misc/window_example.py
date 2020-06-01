from time import time, sleep
from math import sin, cos, pi
from misc.window import Window

window = Window(100, 100, 800, 600)
fps = 60  # frames per second/updates per second
radius = 50
center = (400, 300)
frame = 0

while not window.closed:
    # frame start
    start = time()
    frame += 1

    angle = ((0.01 * frame) % 2) * pi
    offset = 100 * (1 + cos(2 * angle))
    point1 = (center[0] + offset * cos(angle), center[1] + offset * sin(2 * angle))
    point2 = (center[0] - offset * cos(angle), center[1] - offset * sin(2 * angle))
    window.clear()
    if angle < pi:
        window.draw_ellipse((point1[0] - radius, point1[1] - radius), (2 * radius, 2 * radius), color='green')
        window.draw_rectangle((point2[0] - radius, point2[1] - radius), (2 * radius, 2 * radius), color='blue')
    else:
        window.draw_rectangle((point2[0] - radius, point2[1] - radius), (2 * radius, 2 * radius), color='blue')
        window.draw_ellipse((point1[0] - radius, point1[1] - radius), (2 * radius, 2 * radius), color='green')
    window.update()

    # normalize fps
    pause = 1 / fps - (time() - start)
    if pause > 0:
        sleep(pause)

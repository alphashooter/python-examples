from time import sleep
from random import random
from shapes import *


def rectangle_input():
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    color = input('Enter color (red, green, blue, cyan, magenta, yellow, white, black, etc.): ')
    color = color.strip().lower()
    return Rectangle(width, height, color=color)


def square_input():
    size = int(input('Enter size: '))
    color = input('Enter color (red, green, blue, cyan, magenta, yellow, white, black, etc.): ')
    return Square(size, color=color)


figure_input = {
    'rectangle': rectangle_input,
    'square': square_input
}


while True:
    try:
        n = int(input('Enter N: '))
    except:
        print('Invalid input')
    else:
        break


figures = []
for i in range(1, n + 1):
    while True:
        name = input('Enter figure #%d type (rectangle, ellipse, triangle, square, circle): ' % i)
        name = name.strip().lower()  # remove leading and trailing whitespace and convert to lowercase
        try:
            input_func = figure_input[name]
            figure = input_func()
        except:
            print('Invalid input')
        else:
            figures.append(figure)
            break

vectors = []
for figure in figures:
    # set random position
    w, h = figure.width, figure.height
    figure.x = w / 2 + (800 - w) * random()
    figure.y = h / 2 + (600 - h) * random()

    # set random movement
    vector = Point(0.5 - random(), 0.5 - random())
    vector = vector.normalize(3 + 3 * random())
    vectors.append(vector)


graphics.configure('Figures', 800, 600)  # initialize window

while True:
    graphics.clear()  # clear window

    for i in range(n):
        figure, vector = figures[i], vectors[i]
        x, y, w, h = figure.x, figure.y, figure.width, figure.height

        # check x-axis collision
        if vector.x > 0 and x + vector.x > 800 - w / 2:
            vector.x = -vector.x
        if vector.x < 0 and x + vector.x < w / 2:
            vector.x = -vector.x

        # check y-axis collision
        if vector.y > 0 and y + vector.y > 600 - h / 2:
            vector.y = -vector.y
        if vector.y < 0 and y + vector.y < h / 2:
            vector.y = -vector.y

        # update figure position
        figure.x = x + vector.x
        figure.y = y + vector.y

        # draw figure
        figure.draw()

    # update window
    graphics.show()
    sleep(0.030)

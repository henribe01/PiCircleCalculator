import math
import random

import pyglet

WINDOW_SIZE = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
RADIUS = WINDOW_SIZE / 2
DOT_RADIUS = 2

# List to keep track of dots
dot_list = []

# Variables to get amount of dots in and out of the circle
n_in = n_total = 0

window = pyglet.window.Window(WINDOW_SIZE, WINDOW_SIZE)

# Real Circle
circle = pyglet.shapes.Circle(WINDOW_SIZE / 2, WINDOW_SIZE / 2, RADIUS, color=WHITE)

# Circle for border look
border_circle = pyglet.shapes.Circle(WINDOW_SIZE / 2, WINDOW_SIZE / 2, RADIUS - 2, color=BLACK)


@window.event
def on_draw():
    window.clear()
    circle.draw()
    border_circle.draw()
    for dot in dot_list:
        dot.draw()


def update(dt):
    global n_in
    global n_total
    x = random.randint(0, WINDOW_SIZE)
    y = random.randint(0, WINDOW_SIZE)
    dot = pyglet.shapes.Circle(x, y, 2)
    distance = math.sqrt((x - WINDOW_SIZE / 2) ** 2 + (y - WINDOW_SIZE / 2) ** 2)
    if distance <= RADIUS:
        dot.color = RED
        n_in += 1
    else:
        dot.color = BLUE
    n_total += 1
    dot_list.append(dot)
    print('Pi: {}'.format(4 * (n_in / n_total)))


if __name__ == '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()

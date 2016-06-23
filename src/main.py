#!/usr/bin/env python3

import graphics
import resources
import grid
import time

from defs import *
from utility import *
from index import *
from sfml.window import *
from graphics import TextStyle
from itembar import Itembar


# Load resources
res = resources.ResourceManager(INDEX_FILE)
counter = FPSCounter()
renderer = graphics.Graphics()
data = grid.Grid(GRID_WIDTH, GRID_HEIGHT, renderer, res)
itembar = Itembar(renderer, res)


def initialize():
    global data

    for i in range(0, GRID_WIDTH):
        data[(i, 0)] = GRASS

    for i in range(0, GRID_WIDTH, 2):
        data[(i, 1)] = LEAF
    data[(0, GRID_HEIGHT - 1)] = GRASS

    data.offest(GRID_OFFEST_X, GRID_OFFEST_Y)


def locate_mouse():
    mx, my = Mouse.get_position(renderer.window)
    x, y = data.locate(mx, my)

    return (x, y)


def do_events(graphics, event):
    global data

    if type(event) is KeyEvent:
        if event.code == Keyboard.ESCAPE:
            graphics.window.close()

    elif type(event) is MouseButtonEvent:
        if event.pressed:
            x, y = locate_mouse()
            if event.button == Mouse.LEFT:
                if data[(x, y)] == EMPTY:
                    data[(x, y)] = LEAF
            elif event.button == Mouse.RIGHT:
                data[(x, y)] = EMPTY


def update(graphics):
    global data
    global renderer
    VOLECITY = 10

    if (Keyboard.is_key_pressed(Keyboard.UP) or
        Keyboard.is_key_pressed(Keyboard.W)):
        if data.top() < -VOLECITY:
            data.offest(0, VOLECITY)
        else:
            data.offest(0, -data.top())
    if (Keyboard.is_key_pressed(Keyboard.DOWN) or
        Keyboard.is_key_pressed(Keyboard.S)):
        if data.bottom() > renderer.window.height + VOLECITY:
            data.offest(0, -VOLECITY)
        else:
            data.offest(0, renderer.window.height - data.bottom())
    if (Keyboard.is_key_pressed(Keyboard.LEFT) or
        Keyboard.is_key_pressed(Keyboard.A)):
        if data.left() < -VOLECITY:
            data.offest(VOLECITY, 0)
        else:
            data.offest(-data.left(), 0)
    if (Keyboard.is_key_pressed(Keyboard.RIGHT) or
        Keyboard.is_key_pressed(Keyboard.D)):
        if data.right() > renderer.window.width + VOLECITY:
            data.offest(-VOLECITY, 0)
        else:
            data.offest(renderer.window.width - data.right(), 0)


def render_debug_info(graphics):
    global counter

    graphics.draw_string(
        "Flatted %s\nFPS: %s" % (VERSION, counter.get_fps()),
        0, 0, res["ubuntu-italic"]
    )


def render(graphics):
    global data
    global itembar
    global counter

    graphics.clear()

    data.render()
    x, y = locate_mouse()
    data.draw(x, y, MOUSE_CURSOR)
    itembar.render()

    if DEBUG_MODE:
        render_debug_info(graphics)

    graphics.present()
    counter.tick()


# Start up
renderer.create_window(
    DEFAULT_WINDOW_WIDTH, 
    DEFAULT_WINDOW_HEIGHT,
    WINDOW_TITLE,
    res["icon"]
)

renderer.set_clear_color(175, 201, 232)
renderer.set_do_event_handler(do_events)
renderer.set_update_handler(update)
renderer.set_render_handler(render)

initialize()

renderer.main()

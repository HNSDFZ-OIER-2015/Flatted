#!/usr/bin/env python3

import graphics
import resources
import time

from defs import *
from utility import *
from sfml.window import VideoMode
from graphics import TextStyle


# Load resources
res = resources.ResourceManager("./resources/index.json")


def do_events(graphics, event):
    pass


def update(graphics):
    pass


counter = FPSCounter()


def render_debug_info(graphics):
    global counter

    graphics.draw_string(
        "Flatted %s\nFPS: %s" % (VERSION, counter.get_fps()),
        0, 0, res["ubuntu-italic"]
    )


def render(graphics):
    global counter

    graphics.clear()

    for i in range(0, HORIZONTAL_BLOCKS):
        graphics.draw_texture(
            res["grass"],
            BLOCK_SIZE * i, BLOCK_SIZE * (VERTICAL_BLOCKS - 1),
            BLOCK_SIZE, BLOCK_SIZE
        )
        r, g, b, a = res.get_attr("leaf", "color")

    for i in range(0, HORIZONTAL_BLOCKS, 2):
        graphics.draw_texture(
            res["leaf"],
            BLOCK_SIZE * i, BLOCK_SIZE * (VERTICAL_BLOCKS - 2),
            BLOCK_SIZE, BLOCK_SIZE, 
            r, g, b, a
        )

    render_debug_info(graphics)

    graphics.present()
    counter.tick()


# Start up
renderer = graphics.Graphics()
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
renderer.main()

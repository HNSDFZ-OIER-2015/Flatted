from sfml import *
from sfml.window import *
from sfml.system import *
from sfml.graphics import *


class TextStyle:
    REGULAR = Text.REGULAR
    BOLD = Text.BOLD
    ITALIC = Text.ITALIC
    UNDERLINED = Text.UNDERLINED


class Graphics(object):
    def __init__(self):
        super(Graphics, self).__init__()
        
    def create_window(self, width, height, title, icon = None):
            self.window = RenderWindow(
                VideoMode(width, height),
                title
            )

            # Centered the window
            desktop = VideoMode.get_desktop_mode()
            self.window.position = (
                (desktop.width - self.window.width) / 2,
                (desktop.height - self.window.height) / 2,
            )

            if not icon is None:
                # It seems that it doesn't work on Ubuntu
                self.window.icon = icon.pixels

            self.clear_color = Color(255, 255, 255)

    def set_do_event_handler(self, handler):
        """
        def do_events(graphics, event)
        """
        self.do_events = handler

    def set_render_handler(self, handler):
        """
        def render(graphics)
        """
        self.render = handler

    def set_update_handler(self, handler):
        """
        def update(graphics)
        """
        self.update = handler

    def set_clear_color(self, red, green, blue):
        self.clear_color = Color(red, green, blue)

    def draw_texture(
            self, texture, x, y,
            width = None, height = None,
            red = 255, green = 255, blue = 255, alpha = 255
        ):
        sp = Sprite(texture)
        sp.position = (x, y)
        sp.color = Color(red, green, blue, alpha)

        states = RenderStates()
        w = texture.size.x
        h = texture.size.y
        if width is None:
            width = texture.size.x
        if height is None:
            height = texture.size.y

        states.transform.scale((width / w, height / h), (x, y))
        self.window.draw(sp, states)

    def draw_string(
        self, string, x, y, font,
        size = 16,
        red = 0, green = 0, blue = 0, alpha = 255,
        style = TextStyle.REGULAR
    ):
        text = Text(string, font, size)
        text.position = (x, y)
        text.color = Color(red, green, blue, alpha)
        text.style = style
        self.window.draw(text)

    def clear(self):
        self.window.clear(self.clear_color)

    def present(self):
        self.window.display()

    def main(self):
        while self.window.is_open:
            # Processing events
            for event in self.window.events:
                if type(event) is CloseEvent:
                    self.window.close()

                self.do_events(self, event)

            # Updating the game
            self.update(self)

            # Rendering
            self.render(self)

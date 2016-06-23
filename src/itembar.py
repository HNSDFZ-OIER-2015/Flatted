from index import *


class Itembar(object):
    def __init__(self, graphics, resources):
        super(Itembar, self).__init__()
        self.width = resources.get_attr("itembar", "width")
        self.height = resources.get_attr("itembar", "height")
        self.margin_bottom = resources.get_attr("itembar", "margin-bottom")
        self.graphics = graphics
        self.resources = resources

    def render(self):
        self.graphics.draw_texture(
            self.resources.get_resource_by_index(ITEMBAR),
            (self.graphics.window.width - self.width) / 2,
            self.graphics.window.height - self.height - self.margin_bottom,
            self.width, self.height
        )

from sfml.window import Mouse
from index import *


class Itembar(object):
    def __init__(self, graphics, resources):
        super(Itembar, self).__init__()
        self.graphics = graphics
        self.resources = resources

        self.margin_bottom = resources.get_attr("itembar", "margin-bottom")
        self.width = resources.get_attr("itembar", "width")
        self.height = resources.get_attr("itembar", "height")
        self.x = (self.graphics.window.width - self.width) / 2
        self.y = self.graphics.window.height - self.height - self.margin_bottom

        setting = self.resources.get_attr_by_index(ITEMBAR, "setting")
        self.positions = {}
        self.columns = 0
        for key in setting.keys():
            if key == "columns":
                self.columns = setting[key]
                continue

            mx, my = setting[key]
            self.positions[int(key) - 1] = (mx, my)

        self.selectbox_width = resources.get_attr("item-selected", "width")
        self.selectbox_height = resources.get_attr("item-selected", "height")

        self.index = 0

    def wheel(self, delta):
        self.index += delta
        self.index %= self.columns

    def render(self):
        self.graphics.draw_texture(
            self.resources.get_resource_by_index(ITEMBAR),
            self.x, self.y, self.width, self.height
        )

        mx, my = self.positions[self.index]
        self.graphics.draw_texture(
            self.resources.get_resource_by_index(ITEM_SELECTED),
            self.x + mx, self.y + my,
            self.selectbox_width, self.selectbox_height
        )

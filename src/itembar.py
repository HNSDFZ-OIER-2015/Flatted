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
        self.columns = setting["columns"]
        self.item_width = setting["item_width"]
        self.item_height = setting["item_height"]
        self.item_offest_x =setting["item_offest_x"]
        self.item_offest_y =setting["item_offest_y"]
        self.positions = {}
        for holder, position in setting["placeholders"].items():
            mx, my = position
            self.positions[int(holder) - 1] = (mx, my)

        self.selectbox_width = resources.get_attr("item-selected", "width")
        self.selectbox_height = resources.get_attr("item-selected", "height")

        self.index = 0
        self.items = [0 for i in range(self.columns)]

    def wheel(self, delta):
        self.index += delta
        self.index %= self.columns

    def set_item(self, index, item):
        self.items[index] = item

    def current(self):
        return self.items[self.index]

    def render(self):
        self.graphics.draw_texture(
            self.resources.get_resource_by_index(ITEMBAR),
            self.x, self.y, self.width, self.height
        )

        for idx, item in enumerate(self.items):
            if item == 0:
                continue

            mx, my = self.positions[idx]
            self.graphics.draw_texture(
                self.resources.get_resource_by_index(item),
                self.x + mx + self.item_offest_x,
                self.y + my + self.item_offest_y,
                self.item_width, self.item_height
            )

        mx, my = self.positions[self.index]
        self.graphics.draw_texture(
            self.resources.get_resource_by_index(ITEM_SELECTED),
            self.x + mx, self.y + my,
            self.selectbox_width, self.selectbox_height
        )

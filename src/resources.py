import os
import json

from sfml.graphics import Texture, Image, Font


IMAGE_FILE = "image"
TEXTURE_FILE = "texture"
FONT_FILE = "font"


class ResourceManager(object):
    def __init__(self, index_file):
        super(ResourceManager, self).__init__()
        self.index_file = index_file
        self.prefix = os.path.abspath(os.path.dirname(index_file))

        with open(index_file) as reader:
            self.indices = json.load(reader)

        self.resources = {}

        for key, value in self.indices.items():
            path = self.get_path(key)
            restype = value["type"]

            if restype == IMAGE_FILE:
                self.resources[key] = Image.from_file(path)
            elif restype == TEXTURE_FILE:
                self.resources[key] = Texture.from_file(path)
            elif restype == FONT_FILE:
                self.resources[key] = Font.from_file(path)
            else:
                raise TypeError(
                    "Unknown resource type: %s" % (restype)
                )

    def get_path(self, name):
        return os.path.join(
            self.prefix,
            self.indices[name]["location"]
        )

    def get_attr(self, name, attr):
        return self.indices[name][attr]

    def __getitem__(self, name):
        return self.resources[name]

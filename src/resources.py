import os
import json

from sfml.graphics import Texture, Image, Font


IMAGE_FILE = "image"
TEXTURE_FILE = "texture"
FONT_FILE = "font"

TYPE_KEY = "type"
INDEX_KEY = "index"
LOCATION_KEY = "location"
SETTING_KEY = "setting"


class ResourceManager(object):
    def __init__(self, index_file):
        super(ResourceManager, self).__init__()
        self.index_file = index_file
        self.prefix = os.path.abspath(os.path.dirname(index_file))

        with open(index_file) as reader:
            self.data = json.load(reader)

        self.resources = {}
        self.indexes = {}
        self.index_data = {}

        for key, value in self.data.items():
            path = self.get_path(key)
            restype = value[TYPE_KEY]

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

            # Load personal settings
            if SETTING_KEY in value:
                path = os.path.join(
                    self.prefix,
                    value[SETTING_KEY]
                )

                with open(path) as reader:
                    self.data[key][SETTING_KEY] = json.load(reader)

            # Assign indexes
            if INDEX_KEY in value:
                self.indexes[value[INDEX_KEY]] = self.resources[key]
                self.index_data[value[INDEX_KEY]] = self.data[key]


    def get_path(self, name):
        return os.path.join(
            self.prefix,
            self.data[name][LOCATION_KEY]
        )

    def get_attr(self, name, attr):
        return self.data[name][attr]

    def get_resource_by_index(self, index):
        return self.indexes[index]

    def get_attr_by_index(self, index, attr):
        return self.index_data[index][attr]

    def __getitem__(self, name):
        return self.resources[name]

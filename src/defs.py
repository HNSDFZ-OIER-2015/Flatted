VERSION = "V0.0.5"
DEBUG_MODE = True

# Resources
INDEX_FILE = "./resources/index.json"

# Blocks
BLOCK_SIZE = 48
HORIZONTAL_BLOCKS = 16
VERTICAL_BLOCKS = 12

# Grid
GRID_WIDTH = 64
GRID_HEIGHT = 64
GRID_OFFEST_X = 0
GRID_OFFEST_Y = -(GRID_HEIGHT - VERTICAL_BLOCKS) * BLOCK_SIZE

# Chunk
CHUNK_WIDTH = 64
CHUNK_HEIGHT = 64

# Window settings
WINDOW_TITLE = "Flatted %s" % VERSION

# Width & height depend on blocks
DEFAULT_WINDOW_WIDTH = HORIZONTAL_BLOCKS * BLOCK_SIZE
DEFAULT_WINDOW_HEIGHT = VERTICAL_BLOCKS * BLOCK_SIZE

FRAMERATE_LIMIT = 60

import os

from defs import *


INTEGER_BYTES = 4
BYTES_ORDER = "big"


class Chunk(object):
	def __init__(self):
		super(Chunk, self).__init__()
		self.data = []

		for i in range(0, CHUNK_WIDTH):
			self.data.append(
				[0 for j in range(0, CHUNK_HEIGHT)]
			)

	def __getitem__(self, pos):
		x, y = pos
		return self.data[x][y]

	def __setitem__(self, pos, value):
		x, y = pos
		self.data[x][y] = value

	def __repr__(self):
		S = [
			str([self.data[i][j] for i in range(0, CHUNK_WIDTH)])
			for j in range(CHUNK_HEIGHT - 1, -1, -1)
		]
		return "\n".join(S)

	def __str__(self):
		return repr(self)

	def load(self, filepath):
		i, j = 0, 0
		with open(filepath, "rb") as reader:
			while j < CHUNK_HEIGHT:
				buf = reader.read(INTEGER_BYTES)
				# This doesn't work. So strange...
				# v = 0
				# v.from_bytes(buf, BYTES_ORDER)
				v = 	(buf[0] << 24) + (buf[1] << 16) + (buf[2] << 8) + buf[3]
				self[i, j] = v

				i += 1
				if i == CHUNK_WIDTH:
					i, j = 0, j + 1

	def save(self, filepath):
		with open(filepath, "wb") as writer:
			for j in range(0, CHUNK_HEIGHT):
				for i in range(0, CHUNK_WIDTH):
					buf = self[i, j].to_bytes(INTEGER_BYTES, BYTES_ORDER)
					writer.write(buf)

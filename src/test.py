from chunk import Chunk

c = Chunk()
c.load("test.dat")
print(c)
c[0, 0] = 1
print(c)
c.save("test.dat")
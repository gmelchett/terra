
import random

class Fractal:
    def __wrap(self, d):
        if d >= self.size:
            return d - self.size + 1
        if d < 0:
            return d - 1
        return d

    def __add_rand(self, avg, rand):
        return max(0, min(255, avg + random.randint(-rand, rand)))

    def __square_avg(self, x, y, d, rand):

        xa = self.__wrap(x - d)
        xb = self.__wrap(x + d)
        ya = self.__wrap(y - d)
        yb = self.__wrap(y + d)

        a = 0
        p = 0

        if self.terrain[xa][self.__wrap(y)] is not None:
            a = a + self.terrain[xa][self.__wrap(y)]
            p = p + 1
        if self.terrain[xb][self.__wrap(y)] is not None:
            a = a + self.terrain[xb][self.__wrap(y)]
            p = p + 1
        if self.terrain[self.__wrap(x)][ya] is not None:
            a = a + self.terrain[self.__wrap(x)][ya]
            p = p + 1
        if self.terrain[self.__wrap(x)][yb] is not None:
            a = a + self.terrain[self.__wrap(x)][yb]
            p = p +1

        return self.__add_rand(a / p, rand)

    def __generate(self, x, y, d, rand):

        # diamond
        a = 0
        p = 0
        if self.terrain[x][y] is not None:
            a = a + self.terrain[x][y]
            p = p + 1
        if self.terrain[x + d][y] is not None:
            a = a + self.terrain[x + d][y]
            p = p +1
        if self.terrain[x][y + d] is not None:
            a = a + self.terrain[x][y + d]
            p = p + 1
        if self.terrain[x + d][y + d] is not None:
            a = a + self.terrain[x + d][y + d]
            p = p + 1

        self.terrain[x + d / 2][y + d / 2] = self.__add_rand(a / p, rand)
        # square
        self.terrain[x][y + d / 2] =  self.__square_avg(x, y + d/2, d / 2, rand)
        self.terrain[x + d][y + d / 2] =  self.__square_avg(x + d, y + d/2, d / 2, rand)
        self.terrain[x + d / 2][y] =  self.__square_avg(x + d / 2, y, d / 2, rand)
        self.terrain[x + d / 2][y + d] =  self.__square_avg(x + d / 2, y + d, d /2, rand)

    def __init__(self, size = 9):
        self.size = size
        self.terrain = []

        for y in range(0, size):
            l = []
            for x in range(0, size):
                l.append(None)
            self.terrain.append(l)

        self.terrain[0][0] = random.randint(0, 255)
        self.terrain[0][size - 1] = random.randint(0, 255)
        self.terrain[size - 1][0] = random.randint(0, 255)
        self.terrain[size - 1][size - 1] = random.randint(0, 255)

        d = size - 1
        l = 1
        rand = 128

        while True:
            for m in range(0, l):
                for n in range(0, l):
                    self.__generate(m*d, n*d, d, rand)
            if d == 1:
                break
            l = l * 2
            d = d / 2
            rand = rand / 2
    def get_terrain(self):
        return self.terrain
    def get_size(self):
        return self.size


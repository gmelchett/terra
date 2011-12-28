
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

    def __get(self, x, y, s, p):

        if y < 0 or y >= self.size:
            return s, p

        if self.terrain[self.__wrap(x)][y] is not None:
            return s + self.terrain[self.__wrap(x)][y], p + 1
        else:
            return s, p

    def __square_avg(self, x, y, d, rand):
        s = 0
        p = 0

        s, p = self.__get(x - d, y, s, p)
        s, p = self.__get(x + d, y, s, p)
        s, p = self.__get(x, y + d, s, p)
        s, p = self.__get(x, y - d, s, p)

        return self.__add_rand(s / p, rand)

    def __generate(self, x, y, d, rand):

        # diamond
        s = 0
        p = 0
        s, p = self.__get(x, y, s, p)
        s, p = self.__get(x + d, y, s, p)
        s, p = self.__get(x, y + d, s, p)
        s, p = self.__get(x + d, y + d, s, p)

        self.terrain[x + d / 2][y + d / 2] = self.__add_rand(s / p, rand)

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
        # Wrap east-west
        self.terrain[size - 1][0] = self.terrain[0][0]
        self.terrain[size - 1][size - 1] = self.terrain[0][size - 1]

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


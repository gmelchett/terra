
import random

class Fractal:
    def __dump(self):
        if self.debug:
            for x in range(0, self.size):
                print self.terrain[x]

    def __xwrap(self, d):
        if d >= self.size:
            return d - self.size + 1
        if d < 0:
            return d - 1
        return d

    def __add_rand(self, avg, rand):
        return max(0, min(255, avg + random.randint(-rand, rand)))

    def __get(self, x, y, s, p):

        if y < 0 or y >= self.size:
            return s, p + 1

        if self.debug:
            print x, "wrapped:", self.__xwrap(x), y, "is", self.terrain[self.__xwrap(x)][y]

        if self.terrain[self.__xwrap(x)][y] is not None:
            return s + self.terrain[self.__xwrap(x)][y], p + 1
        else:
            return s, p

    def __set(self, x, y, val):
        self.histogram[val] += 1
        self.terrain[self.__xwrap(x)][y] = val

    def __square_avg(self, x, y, d, rand):
        s = 0
        p = 0

        s, p = self.__get(x - d, y, s, p)
        s, p = self.__get(x + d, y, s, p)
        s, p = self.__get(x, y + d, s, p)
        s, p = self.__get(x, y - d, s, p)

        if x == 0 or x == self.size or y == 0 or y == self.size:
            return 0
        else:
            return self.__add_rand(s / p, rand)

    def __generate(self, x, y, d, rand):

        # diamond
        s = 0
        p = 0
        s, p = self.__get(x, y, s, p)
        s, p = self.__get(x + d, y, s, p)
        s, p = self.__get(x, y + d, s, p)
        s, p = self.__get(x + d, y + d, s, p)

        self.__set(x + d / 2, y + d / 2, self.__add_rand(s / p, rand))

        # square
        self.__set(self.__xwrap(x), y + d / 2, self.__square_avg(x, y + d/2, d / 2, rand))
        self.__set(self.__xwrap(x + d), y + d / 2,  self.__square_avg(x + d, y + d/2, d / 2, rand))
        self.__set(self.__xwrap(x + d / 2), y, self.__square_avg(x + d / 2, y, d / 2, rand))
        self.__set(self.__xwrap(x + d / 2), y + d, self.__square_avg(x + d / 2, y + d, d /2, rand))

        self.__dump()

    def __init__(self, size = 9, debug=False, update_callback=None):
        self.size = size
        self.terrain = []
        self.histogram = 256 * [0]
        self.debug = debug

        for y in range(0, size):
            l = []
            for x in range(0, size):
                l.append(None)
            self.terrain.append(l)

        self.__set(0, 0, 0)
        self.__set(0, size - 1, 0)
        self.__set(size - 1, 0, 0)
        self.__set(size - 1, size - 1, 0)

        #self.__set(0, 0, random.randint(0, 255))
        #self.__set(0, size - 1, random.randint(0, 255))
        # TODO: Wrap east-west. This is not good enough
        #self.terrain[size - 1][0] = self.terrain[0][0]
        #self.terrain[size - 1][size - 1] = self.terrain[0][size - 1]

        d = size - 1
        l = 1
        rand = 128

        if update_callback:
            update_callback(0, 5)

        while True:
            for m in range(0, l):
                for n in range(0, l):
                    self.__generate(m*d, n*d, d, rand)
            if update_callback:
                update_callback(d, 5)

            if d == 2:
                break
            l = l * 2
            d = d / 2
            # TODO: Parameter
            rand = 65*rand/100
    def getTerrain(self):
        return self.terrain
    def getSize(self):
        return self.size
    def getHistogram(self):
        return self.histogram



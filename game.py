import os
import random
import time
import numpy as np


class ConwaysGameOfLife(object):
    def __init__(self, *args, **kwargs):
        self.size = 20
        self.tick = 0.5
        self.seed = random.randrange(0, 1000)
        self.cells = np.zeros((self.size, self.size), dtype=np.int8)
        self.random_seed_cells()

    def random_seed_cells(self):
        random.seed(self.seed)
        s = self.size - 1
        for n in range(self.size * 2):
            row = random.randint(0, s)
            col = random.randint(0, s)
            self.cells[row][col] = 1

    def run(self):
        running = True
        while running:
            self.update()
            self.display()
            time.sleep(self.tick)
            running = np.count_nonzero(self.cells) > 0

    def update(self):
        new_cells = np.copy(self.cells)
        for y, row in enumerate(self.cells):
            for x, col in enumerate(row):
                yh = y - 1
                yi = y + 1
                xh = x - 1
                xi = x + 1
                neighbors = 0
                for c in (
                    (yh, x), (yi, x),
                    (y, xh), (y, xi),
                    (yh, xh), (yi, xh),
                    (yh, xi), (yi, xi)
                ):
                    neighbors += self.get_cell(c)

                if neighbors < 2 or neighbors > 3:
                    new_cells[y, x] = 0
                elif neighbors == 3:
                    new_cells[y, x] = 1
        self.cells = new_cells

    def get_cell(self, c):
        y, x = c
        res = 0
        if x >= 0 and x < self.size and y >= 0 and y < self.size:
            res = self.cells[y, x]
        return res

    def display(self):
        os.system('clear')
        print "Seed: %s" % self.seed
        for row in self.cells:
            for col in row:
                 output = '*' if col == 1 else ' '
                 print output,
            print

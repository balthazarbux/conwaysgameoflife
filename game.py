import numpy as np
import random
import time
import os


class ConwaysGameOfLife(object):
    def __init__(self, *args, **kwargs):
        self.size = 20
        self.cells = np.zeros((self.size, self.size), dtype=np.int8)
        self.seed_cells()

    def seed_cells(self):
        s = self.size - 1
        for n in range(self.size * 2):
            row = random.randint(0, s)
            col = random.randint(0, s)
            self.cells[row][col] = 1

    def run(self):
        running = True

        while running:
            self.show_cells()
            self.update_cells()
            time.sleep(0.5)
            os.system('clear')

    def update_cells(self):
        for y, row in enumerate(self.cells):
            for x, col in enumerate(row):
                # check neighbors
                yh = y - 1
                yi = y + 1
                xh = x - 1
                xi = x + 1

                neighbors = 0
                if yh >= 0:
                    neighbors += self.cells[yh, x]
                if yi < self.size:
                    neighbors += self.cells[yi, x]
                if xh >= 0:
                    neighbors += self.cells[y, xh]
                if xi < self.size:
                    neighbors += self.cells[y, xi]
                if yh >= 0 and xh >= 0:
                    neighbors += self.cells[yh, xh]
                if yi < self.size and xh >= 0:
                    neighbors += self.cells[yi, xh]
                if yh >= 0 and xi < self.size:
                    neighbors += self.cells[yh, xi]
                if yi < self.size and xi < self.size:
                    neighbors += self.cells[yi, xi]

                if neighbors < 2 or neighbors > 3:
                    self.cells[y, x] = 0
                elif neighbors == 3:
                    self.cells[y, x] = 1

    def show_cells(self):
        for row in self.cells:
            for col in row:
                print col,
            print

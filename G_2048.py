from constants import *
from field import fields
import random

class g_2048():
    def __init__(self):
        self.field = []
        self.create_g()
        
    def create_g(self):
        for _ in range(FIELD_WIDTH ** 2):
            self.field.append(fields())
            
        for i in range(FIELD_WIDTH):
            for j in range(FIELD_WIDTH):
                index = i * FIELD_WIDTH + j
                if j > 0:
                    self.field[index].left = self.field[index - 1]
                if j < FIELD_WIDTH - 1:
                    self.field[index].right = self.field[index + 1]
                if i > 0:
                    self.field[index].top = self.field[index - FIELD_WIDTH]
                if i < FIELD_WIDTH - 1:
                    self.field[index].bottom = self.field[index + FIELD_WIDTH]

    def shift(self, side):
        """Moves values in the given direction without merging."""
        for _ in range(FIELD_WIDTH - 1):
            if side == "right":
                for i in range(FIELD_WIDTH ** 2 - 1, -1, -1):
                    if self.field[i].value is not None:
                        self.field[i].move(side)
            elif side == "left":
                for i in range(FIELD_WIDTH ** 2):
                    if self.field[i].value is not None:
                        self.field[i].move(side)
            elif side == "top":
                for col in range(FIELD_WIDTH):
                    for row in range(1, FIELD_WIDTH):
                        index = row * FIELD_WIDTH + col
                        if self.field[index].value is not None:
                            self.field[index].move(side)
            elif side == "bottom":
                for col in range(FIELD_WIDTH):
                    for row in range(FIELD_WIDTH - 2, -1, -1):
                        index = row * FIELD_WIDTH + col
                        if self.field[index].value is not None:
                            self.field[index].move(side)

    def merging(self, side):
        """Moves and merges tiles in the given direction."""
        self.shift(side)
        
        if side == "right":
            for row in range(FIELD_WIDTH):
                for col in range(FIELD_WIDTH - 1, 0, -1):
                    index = row * FIELD_WIDTH + col
                    if self.field[index].value is not None:
                        self.field[index].merge(side)

        elif side == "left":
            for row in range(FIELD_WIDTH):
                for col in range(1, FIELD_WIDTH):
                    index = row * FIELD_WIDTH + col
                    if self.field[index].value is not None:
                        self.field[index].merge(side)

        elif side == "top":
            for col in range(FIELD_WIDTH):
                for row in range(1, FIELD_WIDTH):
                    index = row * FIELD_WIDTH + col
                    if self.field[index].value is not None:
                        self.field[index].merge(side)

        elif side == "bottom":
            for col in range(FIELD_WIDTH):
                for row in range(FIELD_WIDTH - 2, -1, -1):
                    index = row * FIELD_WIDTH + col
                    if self.field[index].value is not None:
                        self.field[index].merge(side)

        self.shift(side)
    
    def emerge(self):
        empty_positions = [i for i, field in enumerate(self.field) if field.value is None]
        if empty_positions:
            random_position = random.choice(empty_positions)
            self.field[random_position].value = 2
        


    
    def merging_true(self, side):
        for _ in range(FIELD_WIDTH-1):
            self.merging(side)
        self.emerge()


    def print_2048(self):
        for i in range(0, FIELD_WIDTH ** 2, FIELD_WIDTH):
            print(" ".join(str(cell.value) if cell.value is not None else '.' for cell in self.field[i:i+FIELD_WIDTH]))



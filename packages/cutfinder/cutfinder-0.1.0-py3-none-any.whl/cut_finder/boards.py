#!/usr/bin/env python
"""
A new .py file

"""

class Board:
    def __init__(self, final_id: int, length: float):
        self.length = length
        self.id = final_id
        self.used = False
        self.addressed = False

    def __add__(self, other):
        if isinstance(other, Board):
            return self.length + other.length
        return self.length + other

    def __sub__(self, other):
        return self.length - other

    def __radd__(self, other):
        return self.length if other == 0 else self.__add__(other)

    def __gt__(self, other):
        if isinstance(other, Board):
            return self.length > other.length
        else:
            return self.length > other

    def __ge__(self, other):
        if isinstance(other, Board):
            return self.length >= other.length
        else:
            return self.length >= other

    def __le__(self, other):
        if isinstance(other, Board):
            return self.length <= other.length
        else:
            return self.length <= other

    def __lt__(self, other):
        if isinstance(other, Board):
            return self.length < other.length
        else:
            return self.length < other

    def __mul__(self, other):
        if isinstance(other, Board):
            return self.length * other.length
        else:
            return self.length * other


class FinalBoard(Board):
    def __init__(self, final_id: int, length: float):
        super().__init__(final_id, length)
        self.source = None

    def __repr__(self):
        if self.source:
            return f"{self.length} from board {self.source}"
        else:
            return str(self.length)


class StockBoard(Board):
    def __init__(self, stock_id: int, length: float):
        super().__init__(stock_id, length)
        self.cut_into = list()
        self.remainder = length

    def __repr__(self):
        return f"{self.length} remaining"



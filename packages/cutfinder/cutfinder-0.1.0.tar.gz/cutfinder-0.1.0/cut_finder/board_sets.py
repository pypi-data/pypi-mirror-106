#!/usr/bin/env python
"""
A new .py file

"""

__author__ = 'ccluff'

import boards


class BoardSet:
    boards = dict()

    def __iter__(self):
        yield from self.boards

    def __getitem__(self, item):
        return self.boards.get(item)

    def __eq__(self, other):
        return [board.length for board in self.boards.values()] == other

    def __len__(self):
        return len(self.boards)

    @property
    def used_boards(self):
        """boards that haven't been allocated"""
        return [board.length for board in self.boards.values() if board.used]

    @property
    def unused_boards(self):
        """boards that haven't been allocated"""
        return [board.length for board in self.boards.values() if not board.used]

    @property
    def unaddressed_boards(self):
        """boards that need to be considered still"""
        return [board for board in self.boards.values() if not board.addressed]


class FinalBoardSet(BoardSet):
    """Final Boards"""

    def __init__(self, dimensions_set):
        if str(dimensions_set).isnumeric():
            dimensions_set = [dimensions_set]
        self.boards = {id_ + 1: boards.FinalBoard(id_ + 1, dim) for id_, dim in enumerate(dimensions_set)}


class StockBoardSet(BoardSet):
    """Stock Boards"""

    def __init__(self, dimensions_set):
        if str(dimensions_set).isnumeric():
            dimensions_set = [dimensions_set]
        self.boards = {id_ + 1: boards.StockBoard(id_ + 1, dim) for id_, dim in enumerate(dimensions_set)}

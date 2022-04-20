import random
import numpy as np
import timeit
from Puzzle import *

def bfs_search(puzzle, input):
    startz = timeit.default_timer()
    visited = 0
    puzzle.open.append(input)
    while True:
        visited += 1
        current2 = puzzle.open[0]
        if current2.metnumb == 0:
            stop = timeit.default_timer()
            print("\nbfs visited", visited, "nodes and took ", stop - startz, " seconds to finish")
            return current2
            break
        for i in moves(current2):
            repeat = False
            for k in range(len(puzzle.closed)):
                if i.data == puzzle.closed[k].data:
                    repeat = True
            if repeat == False:
                puzzle.open.append(i)
        puzzle.closed.append(current2)
        puzzle.open.pop(0)


def dfs_search(puzzle, input):
    startz = timeit.default_timer()
    puzzle.open.append(input)
    visited = 0
    while True:
        visited += 1
        current1 = puzzle.open[0]
        if visited > 500 and visited % 500 == 0:
            del puzzle.open[0]
            puzzle.open.sort(key=lambda x: x.gen, reverse=False)
            current1 = puzzle.open[0]
        if current1.metnumb == 0:
            stop = timeit.default_timer()
            print("\ndfs visited", visited, "nodes and took ", stop - startz, " seconds to finish")
            return current1
            break
        for i in moves(current1):
            repeat = False
            for k in range(len(puzzle.closed)):
                if i.data == puzzle.closed[k].data:
                    repeat = True
            if repeat == False:
                puzzle.open.insert(1, i)
        puzzle.closed.append(current1)
        del puzzle.open[0]

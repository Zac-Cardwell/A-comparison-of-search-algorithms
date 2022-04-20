import random
import numpy as np
import timeit
from Puzzle import *

def USF(puzzle, input):
    startz = timeit.default_timer()
    puzzle.open.append(input)
    visited = 0
    while True:
        visited += 1
        current = puzzle.open[0]
        if current.metnumb == 0:
            stop = timeit.default_timer()
            print("\nufs visited", visited, "nodes and took ", stop - startz, "seconds to finish")
            return current
            break
        for i in moves(current):
            repeat = False
            for k in range(len(puzzle.closed)):
                if i.data == puzzle.closed[k].data:
                    repeat = True
            if repeat == False:
                puzzle.open.append(i)
        puzzle.closed.append(current)
        del puzzle.open[0]
        puzzle.open.sort(key=lambda x: x.gen, reverse=False)


def AStar(puzzle, input):
    startz = timeit.default_timer()
    puzzle.open.append(input)
    visited = 0
    while True:
        visited += 1
        current = puzzle.open[0]
        if current.metnumb == 0:
            stop = timeit.default_timer()
            print("\nA* visited", visited, "nodes and took ", stop - startz, "seconds to finish")
            return current
            break
        for i in moves(current):
            repeat = False
            for k in range(len(puzzle.closed)):
                if i.data == puzzle.closed[k].data:
                    repeat = True
            if repeat == False:
                puzzle.open.append(i)
        puzzle.closed.append(current)
        del puzzle.open[0]
        puzzle.open.sort(key=lambda x: x.metnumb, reverse=False)

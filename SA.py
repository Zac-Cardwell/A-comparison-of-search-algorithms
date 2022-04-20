import random
import numpy as np
import timeit
import math
from Puzzle import *

def annealing(puzzle, input):
  initial_temp = 90
  alpha = 0.01
  final_temp = .1
  current_temp = initial_temp
  current = input
  puzzle.open.append(current)
  startz = timeit.default_timer()
  visited = 0
  while True:
    visited += 1
    if current.metnumb == 0:
        stop = timeit.default_timer()
        print("\nAnnealing visited", visited, "nodes and took ",
              stop - startz, "seconds to finish")
        return current
        break
    temp = moves1(current)
    for i in temp:
        repeat = False
        for k in range(len(puzzle.closed)):
            if i.data == puzzle.closed[k].data:
                repeat = True
        for k in range(len(puzzle.open)):
            if i.data == puzzle.open[k].data:
                repeat = True
        if repeat is not True:
            puzzle.open.append(i)
        random.shuffle(puzzle.open)
        next = puzzle.open[0]
        if next.metnumb < current.metnumb:
          puzzle.closed.append(current)
          current = next
        elif random.uniform(0, 1) < math.exp((current.metnumb - next.metnumb) / current_temp):
            puzzle.closed.append(current)
            current = next
        if current_temp > final_temp:
          current_temp -= alpha


def prob_sa(current, next, temp):
    delta = current.metnumb - next.metnumb
    prob = delta/temp
    return prob
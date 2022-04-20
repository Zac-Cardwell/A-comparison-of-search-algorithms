import random
import numpy as np
import timeit

answer = [1, 2, 3, 4, 5, 6, 7, 8, 0]
""""possible moves for every location on the puzzle"""
neighbors = [[1, 3], [0, 2, 4], [1, 5], [4, 0, 6], [
    3, 5, 1, 7], [4, 2, 8], [7, 3], [6, 8, 4], [7, 5]]
problem = list(answer)


def shuffle():
    amount = input("Enter shuffle amount ")
    amount = int(amount)
    for i in range(amount):
        empty_tile = problem.index(0)
        move = neighbors[empty_tile]
        next = random.randrange(0, len(move), 1)
        swap_positions(problem, empty_tile, move[next])


class Node:
    def __init__(self, data, metnumb, gen):
        self.data = data
        self.metnumb = metnumb
        self.gen = gen
        self.parent = None

    def set_parent(self, data):
        self.parent = data


def swap_positions(list, pos1, pos2):
    get = list[pos1], list[pos2]
    list[pos2], list[pos1] = get
    return list


def metro(data):
    h_num = 0
    for x in range(0, len(data.data)):
        if answer[x] != data.data[x]:
            h_num = h_num + 1
    if h_num == 0:
        return 0
    else:
        return h_num + data.gen


def moves(data):
    empty_tile = data.data.index(0)
    children = []
    for x in range(len(neighbors[empty_tile])):
        temp = list(data.data)
        swap_positions(temp, neighbors[empty_tile][x], empty_tile)
        child = Node(temp, 0, data.gen + 1)
        child.metnumb = metro(child)
        child.set_parent(data)
        children.insert(x, child)
        children.sort(key=lambda x: x.gen, reverse=False)
    return children


class puzzle:
    def __init__(self):
        self.open = []
        self.closed = []


def results(final):
    print("\nIt took ", final.gen, "moves to solve the puzzle.")
    puzzle1 = np.reshape(final.data, (-1, 3))
    print("\n", puzzle1)
    print("________________________")
    currently = final.parent
    while currently is not None:
        puzzle1 = np.reshape(currently.data, (-1, 3))
        print(puzzle1)
        print("________________________")
        currently = currently.parent

def moves1(data):
    empty_tile = data.data.index(0)
    children = []
    for x in range(len(neighbors[empty_tile])):
        temp = list(data.data)
        swap_positions(temp, neighbors[empty_tile][x], empty_tile)
        child = Node(temp, 0, data.gen + 1)
        child.metnumb = metro(child)
        child.set_parent(data)
        children.insert(x, child)
        children.sort(key=lambda x: x.gen, reverse=False)
    return children
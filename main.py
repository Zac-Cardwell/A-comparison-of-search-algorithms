from Puzzle import *
from SA import *
from classic_search import *
from heuristic_search import *



shuffle()
start = Node(problem, 0, 0)
print(start.data)
puz, puz1, puz2, puz3, puz4 = puzzle(), puzzle(), puzzle(), puzzle(), puzzle()
start.metnumb = metro(start)


bfs = bfs_search(puz, start)
dfs = dfs_search(puz1, start)
usf = USF(puz2, start)
AS = AStar(puz3, start)
SA = annealing(puz4, start)

assert isinstance(AS, object)

print('\nBFS')
results(bfs)
print('\nUSF')
results(usf)
print('\nA*')
results(AS)
print('\nSimmulated Annealing')
results(SA)
print('\nDFS')
results(dfs)
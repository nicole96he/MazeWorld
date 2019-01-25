from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (0, 1, 4, 1, 3, 1, 2))

test_maze2 = Maze("maze2.maz")
test_mp2 = MazeworldProblem(test_maze2, (0, 3 ,1))
result2 = astar_search(test_mp2, test_mp2.manhattan_heuristic)
print (result2)


# # this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

#this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)


# test_1 = Maze("multi_maze1.maz")
# test_mp_design1 = MazeworldProblem(test_1, (0, 0, 4, 1, 4))
# result_1 = astar_search(test_mp_design1, test_mp_design1.manhattan_heuristic)
# print(result_1)
# test_mp_design1.animate_path(result_1.path)

# test_2 = Maze("multi_maze2.maz")
# test_mp_design2 = MazeworldProblem(test_2, (0, 4, 4))
# result_2 = astar_search(test_mp_design2, test_mp_design2.manhattan_heuristic)
# print(result_2)
# test_mp_design2.animate_path(result_2.path)
#
# test_3 = Maze("multi_maze3.maz")
# test_mp_design3 = MazeworldProblem(test_3, (0, 1, 1, 5, 2, 9, 5))
# result_3 = astar_search(test_mp_design3, test_mp_design3.manhattan_heuristic)
# print(result_3)
# test_mp_design3.animate_path(result_3.path)
#
# test_4 = Maze("multi_maze4.maz")
# test_mp_design4 = MazeworldProblem(test_4, (0, 3, 4))
# result_4 = astar_search(test_mp_design4, test_mp_design4.manhattan_heuristic)
# print(result_4)
# test_mp_design4.animate_path(result_4.path)

# test_5 = Maze("multi_maze5.maz")
# test_mp_design5 = MazeworldProblem(test_5, (0, 0, 16, 1, 16, 27, 9))
# result_5 = astar_search(test_mp_design5, test_mp_design5.manhattan_heuristic)
# print(result_5)
# test_mp_design5.animate_path(result_5.path)

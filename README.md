# MazeWorld
**How to run the code:**

1. test_sensorless.py
This file is used to test multi robots problem.

2. test_mazeworld.py
This file is used to test blind robot problem. Click run, it will test maze2 and maze3 and print bitmap solution path of maze3.
I also write test of five mazes, which is designed by myself, but i have comment these test. If you want to run these 5 tests, just uncomment these code.

3. astar_search.py
This file contains A* search.

4. MazeworldProblem.py
This file contains get_successors function, manhattan_heuristic function, safe function, goal_test function, cost function for multi robots problem.

5. SensorlessProblem.py
This file contains get_successors function, manhattan_heuristic function, safe function, foal_test function, cost function and move_path function for blind robot problem.

6. Maze.py
This file is used to check where is the wall, whether robot collipse or not, getting all information of maze.

7. maze1.maz, maze2.maz, maze3.maz, multi_maze1.maz, multi_maze2.maz, multi_maze3.maz, multi_maze4.maz, multi_maze5.maz
All of these files are different maze.

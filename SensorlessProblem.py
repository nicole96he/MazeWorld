from Maze import Maze
from time import sleep
from SearchSolution import SearchSolution

class SensorlessProblem:


    def __init__(self, maze, goal_locations):
        self.goal = goal_locations
        self.maze = maze
        start_state = []
        start_state.append((0,0,0))
        for x in range(0, maze.width): # use loop to generate start state
            for y in range(0, maze.height):
                if self.maze.is_floor(x,y):
                    start_state.append((x,y))
        self.start_state = tuple(start_state)

    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        for state in range(1, len(path)):
            sleep(1)
            print('\n', str(self))
            for i in range(self.maze.height):
                s = ""
                for j in range(self.maze.width):
                    if self.maze.is_floor(j,self.maze.height-i-1):
                        if (j,self.maze.height-i-1) in path[state]:
                            s += "$"
                        else:
                            s += "."
                    else:
                        s += "#"
                print(s)

        '''
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))
        '''


    '''
    Purpose: use manhattan distance as heuristic function, 
             choose smallest score as h_score of current state.
        Args:
            state
        Return:
            h_score
    '''
    def manhattan_heuristic(self,state):
        min_dis = abs(state[1][0]-self.goal[0]) + abs(state[1][1]-self.goal[1])
        for i in range(2, len(state)): # use loop to find smallest h_score
            cur_dis = abs(state[i][0]-self.goal[0]) + abs(state[i][1]-self.goal[1])
            if min_dis > cur_dis:
                min_dis = cur_dis
        return min_dis


    '''
    Purpose: get next state of current state.
        Args:
            current state
        Return:
            next state
    '''
    def get_successors(self,state):
        north_state = []   #create a list to put all possible location after moving north.
        north_state.append((0,1,0)) # put first node(0,1,0) to represent north.
        south_state = []
        south_state.append((0,-1,0))
        west_state = []
        west_state.append((-1,0,0))
        east_state = []
        east_state.append((1,0,0))
        next_state = []
        for i in range(1,len(state)):
            if self.safe_test(state[i][0],state[i][1]+1): # judge if new location after moving north is safe or not
                north_state.append((state[i][0], state[i][1]+1)) # put new location in north list.
            else:
                north_state.append((state[i][0], state[i][1]))
                # if move north meets wall, stay in original square.

            if self.safe_test(state[i][0], state[i][1]-1):
                south_state.append((state[i][0], state[i][1]-1))
            else:
                south_state.append((state[i][0],state[i][1]))

            if self.safe_test(state[i][0]-1, state[i][1]):
                west_state.append((state[i][0]-1, state[i][1]))
            else:
                west_state.append((state[i][0],state[i][1]))

            if self.safe_test(state[i][0]+1, state[i][1]):
                east_state.append((state[i][0]+1, state[i][1]))
            else:
                east_state.append((state[i][0],state[i][1]))
        north_state = sorted(set(north_state), key = north_state.index) # eliminate repeated nodes in north list
        south_state = sorted(set(south_state), key=south_state.index)
        west_state = sorted(set(west_state), key=west_state.index)
        east_state = sorted(set(east_state), key=east_state.index)
        if len(north_state)!=1: # if north list is not empty, put north list into next_state.
            next_state.append(tuple(north_state))

        if len(south_state)!=1:
            next_state.append(tuple(south_state))

        if len(west_state)!=1:
            next_state.append(tuple(west_state))

        if len(east_state)!=1:
            next_state.append(tuple(east_state))
        return next_state


    '''
    Purpose: check if current location is safe or not
        Args:
            x and y coordinate
        Return:
            true or false
    '''
    def safe_test(self,x,y):
        if self.maze.is_floor(x, y):
            return True
        return False


    '''
    Purpose: check if current state is goal state
        Args: 
            current state
        Return:
            true or false
    '''
    def goal_test(self,state):
        if len(state)==2:  # check if there are only a directional node and a location.
            if state[1] == self.goal: # check if the only location is goal location.
                return True
        return False


    '''
    Purpose: calculate g_score of current state
        Args:
            current state, parent
        Return:
            g_score
    '''
    def cost(self,child,parent):
        cur_cost = parent.transition_cost + 1
        # cost of current state is cost of its parent + 1, no matter the robot moves or not.
        return cur_cost


    '''
    Purpose: show the plan of this system by printing move direction.
        Args: 
            goal node
        Return:
            plan of this system
    '''
    def move_path(self,node):
        result = []
        current = node # this is goal node
        while current:
            if current.state[0]==(0,1,0):
                result.append(('north'))
            elif current.state[0]==(0,-1,0):
                result.append(('south'))
            elif current.state[0]==(-1,0,0):
                result.append(('west'))
            elif current.state[0]==(1,0,0):
                result.append(('east'))
            current = current.parent

        result.reverse()
        print (result)



## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3, (2,2))
    print(test_problem.get_successors(test_problem.start_state))

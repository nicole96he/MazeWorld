from Maze import Maze
from time import sleep
class MazeworldProblem:


    def __init__(self, maze, goal_locations):
        self.goal = goal_locations
        self.maze = maze
        self.robot_num = (len(goal_locations)-1)//2
        self.start_state = maze.start_state

    def __str__(self):
        string =  "Mazeworld problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


    '''
    Purpose: use manhattan distance as heuristic function, 
        Args:
            state
        Return:
            h_score
    '''
    def manhattan_heuristic(self,state):
        distt = 0
        for i in range(1,len(state)):
            distt += abs(state[i]-self.goal[i])

        return distt


    '''
    Purpose: get all possible next states of current state
        Args: current state
        Return: a list of states
    '''
    def get_successors(self,tuple_state):

        state = list(tuple_state) # transfer tuple into list
        cur_robot = state[0] # state[0] represents which robot is moving.
        next_robot = []
        list1 = []
        list3 = []
        if (cur_robot == self.robot_num-1): # judge which robot will move in next state
            next_robot.append(0)
        else:
            next_robot.append(cur_robot + 1)

        for element in range(1,2*cur_robot+1):
            list1.append(state[element])
        # put nodes of robots which order is former than current moving robot into list1
        for i in range(2*cur_robot+3,len(state)):
            list3.append(state[i])
        # put nodes of robots which order is latter than current moving robot into list3

        x = state[cur_robot*2 + 1]
        y = state[cur_robot*2 + 2]
        next_state = [(x,y+1),(x,y-1),(x-1,y),(x+1,y),(x,y)] #put all possible states of current robot in next_state list

        safe_state = []
        return_state = []
        for cur_state in next_state:  # check if states in next_state is saf or not
            if self.safe(cur_state):
                safe_state.append(cur_state)

        tup_left = list1+list3 # put all locations of other robots into tup_left list
        count = 0

        for safe in safe_state: # use loop to check if there is collision between robots or not.
            for loc in range(0, self.robot_num-1):
                if tup_left[2*loc] != safe[0] or tup_left[2*loc+1] != safe[1]:
                    count +=1

            if count == self.robot_num-1:
                list2 = [safe[0],safe[1]]
                final_state = tuple(next_robot + list1 + list2 + list3)
                return_state.append(final_state)

            count = 0

        return return_state

    '''
      Purpose: check if current location is safe or not
          Args:
              current state
          Return:
              true or false
      '''
    def safe(self,state):
        if self.maze.is_floor(state[0], state[1]):
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
        # do not need to check if first tuple in state is same as goal or not,
        # because first tuple represents which robot is moving.
        for i in range(1, len(state)):
            if state[i]!=self.goal[i]:
                return False
        #if state[0] == self.goal[0] and state[1] == self.goal[1]: single robot situation
        return True

    '''
        Purpose: calculate g_score of current state
            Args:
                current state, parent
            Return:
                g_score
        '''
    def cost(self,child, parent):
        cur_cost = parent.transition_cost
        for i in range(1,len(child)):
            if parent.state[i] != child[i]: # if a robot give up moving, the cost of this state is same as parent.
                cur_cost += 1
                break
        return cur_cost


    def move_path(self,node):
        return None


if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (0, 1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))

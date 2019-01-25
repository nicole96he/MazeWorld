from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic
        self.transition_cost = transition_cost


    def priority(self):
        value = self.heuristic + self.transition_cost # use f_Score value as priority
        return value

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:

    def __lt__(self, other):
        return self.priority() < other.priority() # select smallest priority value


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):

    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = [] # The set of currently discovered nodes that are not evaluated yet.
    heappush(pqueue, start_node) # Initially, only the start node is known.

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)
    visited_cost = {} # This is gScore, the cost of going from start node to current node.
    visited_cost[start_node.state] = 0 # The cost of going from start to start is zero.

    close_set = set() # The set of nodes already evaluated
    f_score = {}
    # For each node, the total cost of getting from the start node to the goal by passing by that node.
    f_score[start_node.state] = heuristic_fn(start_node.state) + 0
    # For first node, the f_score is completely heuristic.

    while pqueue:
        cur_node = heappop(pqueue)
        solution.nodes_visited +=1

        if search_problem.goal_test(cur_node.state): # Judge if current node is goal.
            solution.path = backchain(cur_node) # Call backchain function
            solution.cost = cur_node.transition_cost
            search_problem.move_path(cur_node)
            # For blind robot, call move_path function to print plan as a sequence of actions.
            return solution
        close_set.add(cur_node.state) # put node into close_set
        children = search_problem.get_successors(cur_node.state) # Call get_successors

        for child in children:
            if child in close_set:
                continue    # Ignore the neighbor which is already evaluated

            transition_cost = search_problem.cost(child, cur_node)
            # Call cost function to get g_score of current node
            new_node = AstarNode(child, heuristic_fn(child), cur_node, transition_cost)
            if child not in pqueue:  # discover a new node
                heappush(pqueue,new_node)
            elif transition_cost >= visited_cost[child]:
                continue

            visited_cost[child] = transition_cost
            f_score[child] = visited_cost[child] + heuristic_fn(child)

    return solution


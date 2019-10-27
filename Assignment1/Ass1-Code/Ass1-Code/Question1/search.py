# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

#

import math

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
       
        raise Exception("Function not defined")

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        raise Exception("Function not defined")

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        raise Exception("Function not defined")

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        raise Exception("Function not defined")
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        raise Exception("Function not defined")


def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    heauristic_factor = 0.5
    frontiers = dict()
    current = problem.getStartState()
    visited = {current: [None, 0, None]}
    while not problem.isGoalState(current):

        current_cost = visited[current][1]
        neighbors = problem.getSuccessors(current)

        for i in neighbors:

            next_state = i[0]
            if next_state in visited:
                continue
            parent = current
            total_cost = current_cost + i[3]
            move = i[1]
            heuristic_val = problem.getHeuristic(next_state)
            if next_state in frontiers and total_cost >= frontiers[next_state]['total cost']:
                continue
            frontiers[next_state] = {'parent': parent, 'total cost': total_cost, 'heuristic': heuristic_val, 'move': move}

        cost = math.inf
        next_best = None
        for frontier in frontiers:
            functional_cost = heauristic_factor * frontiers[frontier]['total cost'] \
                              + (1 - heauristic_factor) * frontiers[frontier]['heuristic']
            if functional_cost < cost:
                next_best = frontier
                cost = functional_cost


        visited[next_best] = [frontiers[next_best]['parent'], frontiers[next_best]['total cost'], frontiers[next_best]['move']]
        del frontiers[next_best]
        current = next_best


    parent = visited[current][0]
    path = [current, parent]

    while visited[parent][0] != None:
        parent = visited[parent][0]
        path.append(parent)

    path.reverse()

    return path











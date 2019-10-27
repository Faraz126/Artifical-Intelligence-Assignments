import search
import random

class JumpingFrogState:
    def __init__( self, numbers):
        """
          Constructs a new frog puzzle from a sequence of 1's and 2's with a zero in between.

        numbers: a list of 1,2,0 where 1 indicates green frog, 0 indicates empty rock and 2 indicates red frog


            [1,1,1,0,2,2,2]

          represents the frog puzzle:
            green frog, green frog, green frog, empty rock, red frog, red frog, red frog

        The configuration of the puzzle is stored in a 1-dimensional list 'rocks'.
        """

        self.rocks = numbers[:] # Make a copy so as not to cause side-effects.
        self.blankLocation = self.rocks.index(0)

    def isGoal(self):
        """
            checks to see if the current state is the goal state.

            ----------------
            red frog, red frog, red frog, empty rock, green frog, green frog, green frog
            ----------------

        :return: True or False indicating the state is True or False

        """
        return self == JumpingFrogState([2, 2, 2, 0, 1, 1, 1])

    def legalMoves(self):
        """
        returns a list of legal moves possible from the current state
        moves are encoded as,
        left = move the empty rock one step to the left
        ultra left = move the empty rock two steps to the left
        right = move the empty rock one step to the right
        ultra right = move the empty rock two steps to the right
        """
        moves = []
        if (self.blankLocation != 0):
            moves.append('left')
        if (self.blankLocation > 1):
            moves.append('ultra left')
        if (self.blankLocation != 6):
            moves.append('right')
        if (self.blankLocation < 5):
            moves.append('ultra right')
        return moves

    def result(self, move):
        """
        :param moves: a list of legal moves from the current state
        :return: returns new Jumping Frog State possible from the current
        """
        newState = self.rocks[:]

        if move == "left":
            newState[self.blankLocation], newState[self.blankLocation - 1] = newState[self.blankLocation -1 ], newState[self.blankLocation]
        elif move == "ultra left":
            newState[self.blankLocation], newState[self.blankLocation - 2] = newState[self.blankLocation - 2], newState[self.blankLocation]
        elif move == "right":
            newState[self.blankLocation], newState[self.blankLocation + 1] = newState[self.blankLocation + 1], newState[self.blankLocation]
        elif move == "ultra right":
            newState[self.blankLocation], newState[self.blankLocation + 2] = newState[self.blankLocation + 2], newState[self.blankLocation]
        return JumpingFrogState(newState)

    def __hash__(self):
        """
        since all configurations are a combination of 0,1,2 we can consider the sequence
        """

        trinary_number = 0
        for i in range(7):
            trinary_number += self.rocks[i] * (3 ** i)

        return hash(trinary_number)
        #return hash(''.join([str(i) for i in self.rocks]))
    def __eq__(self, other):
        """

        Overloads '==' such that two JumpingFrogState with the same configuration
          are equal.
        """

        if other == None:
            return False
        return other.blankLocation == self.blankLocation and other.rocks == self.rocks

    def __getAsciiString(self):
        """
            returns a string representation of the the given configuration, which is easier to view.
        """
        string = []
        for i in self.rocks:
            if i == 1:
                string.append('Green Frog')
            elif i == 2:
                string.append('Red Frog')
            else:
                string.append('Empty Rock')
        string = "  |  ".join(string)
        return string
    def __str__(self):
        return self.__getAsciiString()

class JumpingFroqSearchProblem(search.SearchProblem):
    """"
    implementation of the Jumping Froq problem as a search problem
    """
    def __init__(self,puzzle):
        "Creates a new JumpingFrogSearchProblem which stores search information."
        self.puzzle = puzzle

    def getStartState(self):
        return self.puzzle

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self, state):
        """
          Returns list of (successor, action, stepCost) pairs where
          each succesor is either left, ultra left, right, ultra right.
          move to left and right costs 1, while move to right and ultra right costs 2
        """
        succ = []
        for a in state.legalMoves():
            if a == 'left' or a == 'right':
                succ.append((state.result(a), a, state, 1))
            else:
                succ.append((state.result(a), a, state, 2))
        return succ

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        cost = 0
        for i in actions:
            if i == 'left' or i == 'right':
                cost += 1
            else:
                cost += 2
        return cost

    def getHeuristic(self, state):
        """
        :param state: the current state of the puzzle
        :return: the count of misplaced numbers


        """
        correct = [1,1,1,0,2,2,2]
        cost = 0
        for i in range(7):
            if correct[i] != state.rocks[i]:
                cost += 1
        return cost


FROG_PUZZLE_DATA = [[1, 1, 1, 0, 2, 2, 2],
                    [1, 2, 0, 1, 2, 1, 2],
                    [2, 1, 2, 2, 1, 1, 0],
                    [2, 2, 0, 1, 1, 1, 2],
                    [1, 2, 2, 2, 1, 1, 0],
                    [2, 2, 2, 1, 1, 1, 0]]

def loadFrogPuzzle(puzzleNumber):
    return JumpingFrogState(FROG_PUZZLE_DATA[puzzleNumber])

def createRandomEightPuzzle(moves=100):
    """
      moves: number of random moves to apply

      Creates a random eight puzzle by applying
      a series of 'moves'random moves to a solved
      puzzle.
    """
    puzzle = JumpingFrogState([0,1,1,1,2,2,2])
    for i in range(moves):
        # Execute a random legal move
        puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])
    return puzzle

for j in range(6):
    puzzle = loadFrogPuzzle(j)
    problem = JumpingFroqSearchProblem(puzzle)
    path = search.aStarSearch(problem)

    print(len(path))

import math
import random
import matplotlib.pyplot as plt
import numpy as np

@np.vectorize
def func1(x,y):
    return (x**2) + (y**2)

@np.vectorize
def func2(x,y):
    return 100 * ((y - (x ** 2)) ** 2) + (1 - x) ** 2
    #return (100 * ((x**2) - (y**2))) + ((1 - x)**2)

@np.vectorize
def func3(x,y):
    return ((x**2 + y**2)/4000) - (math.cos(x) * math.cos(y/math.sqrt(2))) + 1

def decay_func(x, factor = 50, decay_factor = 50):
    return factor * (math.e ** -( (x) / decay_factor))

def probability_function(change, temperature):
    return math.e ** (change/temperature)

class Point:
    def __init__(self, x, y):
        """
        :param x: x-co-ordinate of the point
        :param y: y-co-ordinate of the point
        """
        self.x = x
        self.y = y

    def function_apply(self, func):
        """
        :param func: the function to apply to the function
        :return: the value obtained after applying the function to the point
        """
        return func(self.x, self.y)

    def get_neighbors(self, step = 1):
        """
        :param step: the step size for the next step
        :return: returns the list of all the 8 neighbors from the current point at a distance of step.
        """
        neighbors = []

        x = [step, step, 0, -step, -step, -step, 0, step]
        y = [0, step, step, step, 0, -step, -step, -step]

        for i in range(8):
            neighbors.append(self + Point(x[i], y[i]))
        return neighbors

    def within_range(self, range):
        """
        :param range: a tuple of the form (min_x, max_x, min_y, max_y)
        :return: returns whether the point is within the given range. It performs an inclusive search.
        """
        return self.x >= range[0] and self.x <= range[1] and self.y >= range[2] and self.y <= range[3]

    def plot(self):
        #for plotting with matplotlib
        pass

    def df(self, func, other):
        """
        :param func: the function to input the point to
        :param other: the second point on which to calculate the function value
        :return: returns the change in value when moving from one point to another
        """
        cur = self.function_apply(func)
        next = other.function_apply(func)
        return next - cur

    def __lt__(self, other):
        return self.x**2  + self.y**2 < other.x**2 + other.y**2

    def __add__(self, other):
        """
        overloads the + operator and returns the pairwise sum of respective co-ordinates.
        """
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash(str(self))

    def __getAsciiString(self):
        my_str = 'x = ' + str(self.x) + ' y = ' + str(self.y)
        return my_str

    def __str__(self):
        return self.__getAsciiString()


def simulated_annealing(func, given_range = (-math.inf, math.inf, -math.inf, math.inf), precision = 0, find_max = True, step = 0.1 ):
    """
    :param func: the function to optimize. We are assuming the func is of the form, func(a, b) where a and b could be real numbers
    :param range: A tuple of the form (min_x, max_x, min_y, max_y) which denotes the boundaries of the given function
    :param precision: the number of decimal points to include in your calculation
    :return: returns path taken to find the optimized value
    """
    random_x = round((random.uniform(given_range[0], given_range[1])), precision)
    random_y = round((random.uniform(given_range[2], given_range[3])), precision)

    outputs = []
    inputs = []
    current_point = Point(random_x, random_y)

    iteration = 0
    search_end = False
    visited = set()
    path = []
    decay_factor = 200


    temperature = decay_func(iteration, decay_factor = decay_factor)
    temperature_threshold = 1

    while not search_end:
        outputs.append(current_point.function_apply(func))
        inputs.append(iteration)

        neighbors = [i for i in current_point.get_neighbors(step = step) if i.within_range(given_range) and i not in visited]

        if not find_max:
            change = -1
        else:
            change = 1

        #output = [change * current_point.df(func, i) for i in neighbors]
        max_dir = -1
        times = 0


        while max_dir == -1 and times < 10:
            times += 1
            index = random.randint(0,len(neighbors) -1)
            output = change * current_point.df(func, neighbors[index])
            if output > 0:
                max_dir = index
            else:
                prob = 100 * probability_function(output, temperature)
                random_num = random.uniform(0, 100)
                if random_num  < prob:
                    max_dir = index

        """
        for i in range(len(neighbors)):
            if find_max:
                if output[i] > 0 and max_dir == -1:
                    max_dir = i
                    probabilities[i] = 0
                elif output[i] > 0 and output[i] > output[max_dir]:
                    max_dir = i
                    probabilities[i] = 0
                elif output[i] < 0:
                    probabilities[i] = probability_function(output[i], temperature)
            else:
                if output[i] < 0 and max_dir == -1:
                    max_dir = i
                    probabilities[i] = 0
                elif max_dir != -1 and output[i] < output[max_dir]:
                    max_dir = i
                    probabilities[i] = 0
                elif output[i] > 0:
                    probabilities[i] = probability_function(-output[i], temperature)

        while max_dir == -1:
            probabilities, neighbors = (list(t) for t in zip(*sorted(zip(probabilities, neighbors), reverse = True)))

            for i in range(len(probabilities)):
                prob = probabilities[i] * 100
                random_num = random.uniform(0, 100)
                if random_num < prob:
                    max_dir = i
                    break
        """
        next_point = neighbors[max_dir]
        visited.add(next_point)
        path.append(next_point)
        iteration += 1
        temperature = decay_func(iteration, decay_factor = decay_factor)
        current_point = next_point

        if temperature < temperature_threshold:
            search_end = True



    return path





FUNCTION_NUMBER = 3 #to decide the function, 1 for sphere, 2 for rosenbrock 3 for griewank
FIND_MAX = True

if FUNCTION_NUMBER == 1:
    func = func1
    func_range = (-5, 5, -5, 5)
    step = 0.2

if FUNCTION_NUMBER == 2:
    func = func2
    func_range = (-2, 2, -1, 3)
    step = 0.1

if FUNCTION_NUMBER == 3:
    func = func3
    func_range = (-30, 30, -30, 30)
    step = 0.05





path = simulated_annealing(func, func_range, find_max = FIND_MAX, step = step)




x = [i.x for i in path]
y = [i.y for i in path]
z = [i.function_apply(func) for i in path]
X = [i for i in np.arange(func_range[0], func_range[1], 0.1)]
Y = [i for i in np.arange(func_range[2], func_range[3], 0.1)]
X, Y = np.meshgrid(X,Y)
Z = func(X,Y)


fig, (ax1, ax2) = plt.subplots(2,2)
ax1[1].plot(x, y, 'r.')
CS = ax1[1].contour(X, Y, Z)

ax1[1].clabel(CS, inline=2, fontsize=10)
ax1[1].set_title('Contour plot of the function')
ax1[1].set_xlabel('x')
ax1[1].set_ylabel('y')

ax2[0].plot(range(0, len(x)), x)
ax2[0].set_xlabel('iteration')
ax2[0].set_ylabel('x')
ax2[0].set_ylim(func_range[0], func_range[1])
ax2[1].plot(range(0, len(x)), y)

ax2[1].set_xlabel('iteration')
ax2[1].set_ylabel('y')
ax2[1].set_ylim(func_range[2], func_range[3])
ax1[0].plot(range(0, len(z)), z)
ax1[0].set_title('f(x,y) wrt iteration')
ax1[0].set_xlabel('iteration')
ax1[0].set_ylabel('f(x,y)')

mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show()





















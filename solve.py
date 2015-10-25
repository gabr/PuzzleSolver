import sys
import random

def drawTable(table, char="0"):
    print "+",
    print "-"*(len(table[0])*2-1),
    print "+"
    for row in range(len(table) -1, -1, -1):
        print "|",
        for column in table[row]:
            if column:
                print char,
            else:
                print " ",
        print "|"
    print "+",
    print "-"*(len(table[0])*2-1),
    print "+"

def drawSolution(x, y, solution):
    table = createTable(x, y)
    for px, py in solution:
        table[px][py] = True
    drawTable(table, char="X")

def makeMove(x, y, table):
    y_len = len(table)
    x_len = len(table[0])
    table[y][x] = not table[y][x]
    if x - 1 >= 0:
        table[y][x - 1] = not table[y][x - 1]
    if x + 1 < x_len:
        table[y][x + 1] = not table[y][x + 1]
    if y - 1 >= 0:
        table[y - 1][x] = not table[y - 1][x]
    if y + 1 < y_len:
        table[y + 1][x] = not table[y + 1][x]

def checkTable(table):
    for row in table:
        for column in row:
            if column == False:
                return False
    return True

def checkSolution(x, y, solution):
    table = createTable(x, y)
    for x, y in solution:
      makeMove(x, y, table)
    return checkTable(table)

def copyTable(table):
    return [[column for column in row] for row in table]

def createTable(x, y):
    return [[False for column in range(x)] for row in range(y)]

def makeNextStep(x_range, y_range, step):
    x, y = step
    if x + 1 < x_range:
      return (x + 1, y)
    else:
      if y + 1 < y_range:
        return (0, y + 1)
      else:
        return None

def canMakeNextStep(x_range, y_range, step):
    return makeNextStep(x_range, y_range, step) != (0, 0)

def solveDepthFirst(x_range, y_range):
    max_depth = x_range * y_range
    solution = [(0, 0)]
    while not checkSolution(x_range, y_range, solution):
      if len(solution) == max_depth:
        next_step = solution.pop()
      else:
        next_step = solution[-1]
      next_step = makeNextStep(x_range, y_range, next_step)
      while next_step == None:
        next_step = solution.pop()
        next_step = makeNextStep(x_range, y_range, next_step)
      while next_step in solution:
        next_step = makeNextStep(x_range, y_range, next_step)
        while next_step == None:
          next_step = solution.pop()
          next_step = makeNextStep(x_range, y_range, next_step)
      solution.append(next_step)
    return solution

def solveGenetic(x, y, max_number_of_steps):
    """
        Genetic algorithm.
        Solves problem trying random moves until whole
        table is True and number of step in solution
        is less then given max number of steps.
        Returns moves coordinates in order as list of tuples.
    """
    # create empty table
    table = createTable(x, y)

    # init steps counter
    steps_counter = 0

    # result list
    result = []
    while True:
        # increment steps counter
        steps_counter += 1

        # random next move that wasn't perform before
        while True:
            x_rand = random.randrange(0, x)
            y_rand = random.randrange(0, y)
            if not (x_rand, y_rand) in result:
                break

        # save this move
        result.append((x_rand, y_rand))

        # make this move on the table
        makeMove(x_rand, y_rand, table)

        # check table
        if checkTable(table):
            # done - return result
            return result

        # if it was the last step the reset
        if steps_counter + 1 == max_number_of_steps:
            steps_counter = 0
            table = createTable(x, y)
            result = []

def main():
    # check number of given arguments
    if len(sys.argv) != 4 or (sys.argv[1] != "g" and sys.argv[1] != "d"):
        print ""
        print "ussage:"
        print " %s <algorithm> <number of columns> <number of rows>" \
                % sys.argv[0]
        print ""
        print " <algorithm> need to be set as one of:"
        print "   g - genetic algorithm"
        print "   d - depth-first serach"
        print ""
        print " Coordinates expalantion (XxY):"
        print "    y"
        print "  ^     move: (1x1)       move: (2x1)      move: (2x0)"
        print "  | +-------+         +-------+        +-------+      "
        print "  | |   0   |         |     0 |        |       |      "
        print "  | | 0 0 0 |         |   0 0 |        |     0 |      "
        print "  | |   0   |         |     0 |        |   0 0 |      "
        print "  | +-------+   x     +-------+        +-------+      "
        print "  +------------>"
        quit()

    # extract algorithm type
    algorithm = sys.argv[1]

    # extract dimension from arguments
    x, y = [int(sys.argv[2 + i]) for i in range(2)]

    # print init message
    print "Solving %dx%d" % (x, y),

    # choose algorithm
    if algorithm == "g":
        print "using genetic algorithm"
        # infinite loop, end program with CTRL+C
        solution = None
        try:
            # maximum number of possible steps without steps repetitions
            number_of_steps = x * y
            while True:
                # find first solution with less steps then given
                solution = solveGenetic(x, y, number_of_steps)
                # update number of steps
                number_of_steps = len(solution)
                # print solution
                print "\nNumber of steps: %d" % number_of_steps
                print "Steps: %r" % solution
        except:
            # if we have result draw it step by step
            if solution:
                drawSolution(x, y, solution)

    if algorithm == "d":
        print "using depth-first serach algorithm"
        solution = solveDepthFirst(x, y)
        drawSolution(x, y, solution)

if __name__ == "__main__":
    main()

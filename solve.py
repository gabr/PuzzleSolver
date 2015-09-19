import sys
import random

def drawTable(table):
    print "+",
    print "-"*(len(table[0])*2),
    print "+"
    for row in range(len(table) -1, -1, -1):
        print "|",
        for column in table[row]:
            if column:
                print "0",
            else:
                print " ",
        print "|"
    print "+",
    print "-"*(len(table[0])*2),
    print "+"

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

def copyTable(table):
    return [[column for column in row] for row in table]

def createTable(x, y):
    return [[False for column in range(x)] for row in range(y)]

def solveBreadth(x, y):
    if x >= 5 or y >= 5:
        print "DONT!!!!"
        return []
    # create empty table
    tables = [createTable(x, y) for _ in range(x*y)]
    steps = [[] for _ in range(x*y)]
    while True:
        next_tables = []
        next_steps = []
        for table in range(len(tables)):
            for row in range(len(tables[table])):
                for column in range(len(tables[table][0])):
                    copy_table = copyTable(tables[table])
                    copy_steps = steps[table][:]
                    copy_steps.append((row, column))
                    makeMove(row, column, copy_table)
                    if checkTable(copy_table):
                        return copy_steps
                    next_tables.append(copy_table)
                    next_steps.append(copy_steps)
        tables = next_tables
        steps = next_steps

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

        # random next move
        x_rand = random.randrange(0, x)
        y_rand = random.randrange(0, y)

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
    # helper variable, store number of steps from previous solution
    number_of_steps = 100000

    # check number of given arguments
    if (len(sys.argv) != 4 and len(sys.argv) != 5) \
            or (sys.argv[1] != "b" and sys.argv[1] != "g"):
        print ""
        print "ussage:"
        print " %s b|g <number of columns> <number of rows>" % sys.argv[0],
        print "[<init number of steps>]"
        print ""
        print " b - use breadth-first search"
        print " g - use genetic algorithm"
        print "     Default value for initial number of steps is %d" \
                % number_of_steps
        print "     Used only in genetic algorithm!"
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

    # get algorithm type
    algorithm = sys.argv[1]

    # extract dimension from arguments
    x, y = [int(sys.argv[2 + i]) for i in range(2)]

    # check for number of steps
    if len(sys.argv) > 4:
        number_of_steps = int(sys.argv[4])

    # print init message
    print "Solving %dx%d" % (x, y),

    if algorithm == "g":
        print "using genetic algorithm with initial number of steps %d" \
               % number_of_steps
    elif algorithm == "b":
        print "using breadth-first search"

    # infinite loop, end program with CTRL+C
    solution = None
    try:
        if algorithm == "g":
            while True:
                # find first solution with less steps then given
                solution = solveGenetic(x, y, number_of_steps)
                # update number of steps
                number_of_steps = len(solution)
                # print solution
                print "\nNumber of steps: %d" % number_of_steps
                print "Steps: %r" % solution
        elif algorithm == "b":
            solution = solveBreadth(x, y)
            print "\nNumber of steps: %d" % len(solution)
            print "Steps: %r" % solution
    except:
        pass
    else:
        # if we have result draw it step by step
        if solution:
            table = createTable(x, y)
            drawTable(table)
            for step in solution:
                makeMove(step[0], step[1], table)
                print "move: %r" % (step,)
                drawTable(table)
                raw_input("Press for next...")
                print ""

if __name__ == "__main__":
    main()

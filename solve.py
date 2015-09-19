import sys

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

def createTable(x, y):
    return [[False for column in xrange(x)] for row in xrange(y)]

def solve(x, y, max_number_of_steps):
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
        steps_counter += 1

    # return result
    return result

def main():
    # helper variable, store number of steps from previous solution
    number_of_steps = 100000

    # check number of given arguments
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print ""
        print "ussage:"
        print " %s <number of columns> <number of rows>" % sys.argv[0],
        print "[<init number of steps>]"
        print ""
        print " Default value for initial number of steps is %d" \
                % number_of_steps
        print ""
        print ""
        print " Coordinates expalantion (XxY):"
        print ""
        print " y"
        print "  ^     move: (1x1)       move: (2x1)      move: (2x0)"
        print "  | +-------+         +-------+        +-------+      "
        print "  | |   0   |         |     0 |        |       |      "
        print "  | | 0 0 0 |         |   0 0 |        |     0 |      "
        print "  | |   0   |         |     0 |        |   0 0 |      "
        print "  | +-------+         +-------+        +-------+      "
        print "  +------------>"
        print "                x"
        quit()

    # extract dimension from arguments
    x, y = [int(sys.argv[1 + i]) for i in xrange(2)]

    # check for number of steps
    if len(sys.argv) > 3:
        number_of_steps = int(sys.argv[3])

    # print init message
    print "Solving %dx%d with initial number of steps %d" \
            % (x, y, number_of_steps)

    quit()

    # infinite loop, end program with CTRL+C
    while True:
        # find first solution with less steps then given
        solution = solve(x, y, number_of_steps)
        # update number of steps
        number_of_steps = len(solution)
        # print solution
        print "\nNumber of steps: %d" % number_of_steps
        print "Steps: %r" % solution

if __name__ == "__main__":
    main()

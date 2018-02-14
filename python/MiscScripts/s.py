def neigbors(point):
    x, y = point
    for i, j in itertools.product(range(-1, 2), repeat=2):
        if any((i, j)):
            yield (x + i, y + j)

def advance(board):
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    for point in recalc:
        count = sum((neigh in board)
                for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)

    return newstate

glider = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])
for i in range(1000):
    glider = advance(glider)
print glider
def readFile(rute):
    todo = []
    with open(rute, 'r') as file:
        for line in file:
            thing = line.strip().split(',')
            thing[-1] = int(thing[-1])
            todo.append(thing)
    return todo
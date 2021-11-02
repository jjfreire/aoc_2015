import sys, os, operator
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from constants import ROOT_DIR

switcher = {
    '^': (1, 0),
    '>': (0, 1),
    'v': (-1, 0),
    '<': (0, -1)
}

def get_tuple(direction):
    return switcher[direction]

def main():
    directions = None
    position = (0, 0)
    deliveries = {
        0: {
            0: 1
        }
    }

    with open(os.path.join(ROOT_DIR, '3\input\input.txt'), 'r') as instructions:
        directions = instructions.read()

    
    for dir in directions:
        position = tuple(map(operator.add, position, get_tuple(dir)))
        try:
            deliveries[position[0]][position[1]] += 1
        except KeyError:
            if position[0] not in deliveries:
                deliveries[position[0]] = {}
            deliveries[position[0]][position[1]] = 1
    
    print("Total houses with present:", sum(len(v) for v in deliveries.values()))


if __name__=="__main__":
    main()
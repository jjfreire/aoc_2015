import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from constants import ROOT_DIR

def main():
    floors = None
    actual_floor = 0
    char_found = 0

    with open(os.path.join(ROOT_DIR, '1\input\input.txt'), 'r') as instructions:
        floors = instructions.read()

    for i, floor in enumerate(floors):
        if floor == '(':
            actual_floor += 1
        elif floor ==')':
            actual_floor -= 1
        if actual_floor == -1 and not char_found:
            char_found = i
            with open(os.path.join(ROOT_DIR, '1\output\\p2\\answer.txt'), 'w') as output:
                output.write(str(i+1))

    with open(os.path.join(ROOT_DIR, '1\output\\p1\\answer.txt'), 'w') as output:
        output.write(str(actual_floor))

if __name__=="__main__":
    main()
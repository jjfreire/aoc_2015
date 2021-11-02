import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from constants import ROOT_DIR

def main():
    dimensions = None
    total_square_feet = 0
    total_ribbon = 0

    with open(os.path.join(ROOT_DIR, '2\input\input.txt'), 'r') as instructions:
        dimensions = instructions.readlines()

    for dimension in dimensions:
        l, w, h = [int(x) for x in dimension.split('x')]
        a1 = 2*l*w
        a2 = 2*w*h
        a3 = 2*h*l
        
        extra = int(min(a1/2, a2/2, a3/2))
        total_square_feet += a1 + a2 + a3 + extra

        #######
        sorted_sides = sorted([l, w, h])
        total_ribbon += sorted_sides[0]*2 + sorted_sides[1]*2 + l*w*h


    print('Total square feet of wrapping papper:', total_square_feet)
    
    print('Total feet of ribbon:', total_ribbon)

if __name__=="__main__":
    main()
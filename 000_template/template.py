#!/usr/bin/env python3

# User: yamadzaki

# Problem description:
# ...

# Problem description in Russian:
# ...

# Worktime on Amazon microinstance:...
# Complexity: O(?)


import sys
import threading
import time
#threading.stack_size(2**27)
#sys.setrecursionlimit(2**25)


def main():
    start = time.time()

    #G = list()
    numofvertices, numofedges = 0, 0

    with open(sys.argv[1]) as infile:
        i = 0
        for line in infile:
            if i == 0:
                numofvertices, numofedges = map(int, line.split())

            else:
                intline = list(map(int, line.split())) #[head, tail, weight]
                G[intline[0]][intline[1]][0] = intline[2]

            i+=1

    #print(G) 
    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


if __name__ == '__main__':
    #    main()
    thread = threading.Thread(target=main)
    thread.start()    
    

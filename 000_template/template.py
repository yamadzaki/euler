#!/usr/bin/env python3

# User: yamadzaki

# Problem description:
# ...

# Problem description in Russian:
# ...

# Worktime on my computer =): ...
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
    print('Number of vertices:', numofvertices, ', number of edges:', numofedges)
    print('Time to load file: {:.6f}, len(G): {} '.format(time.time()-start, len(G)*len(G[0])))

    return 0


if __name__ == '__main__':
    #    main()
    thread = threading.Thread(target=main)
    thread.start()    
    

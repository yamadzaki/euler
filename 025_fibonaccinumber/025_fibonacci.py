#!/usr/bin/env python3

# User: yamadzaki

# Problem description:
# ...

# Problem description in Russian:
# ...

# Worktime on Amazon microinstance:...
# Complexity: O(?)


import sys
import time

def fibgen():
    prev, now = 1, 1
    yield prev
    yield now
    while True:
        prev, now = now, now+prev
        yield now
    

def main():
    start = time.time()
    ans = 0

    digits = 1000
    lim = 10**(digits-1)
    idx = 0
    for fibnum in fibgen():
        idx+=1
    #    print(fibnum, fibnum//100)
        if (fibnum//lim) > 0:
            break
    
    ans = idx
    #print(G) 
    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


if __name__ == '__main__':
    main()
    


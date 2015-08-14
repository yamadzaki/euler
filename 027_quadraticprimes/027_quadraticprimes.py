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
import math

def isprime(num):
    '''Additional finction for primes generator'''
    if num <= 0:
        return False

    maxfactor = num**(1/2)
    maxfactor = math.floor(maxfactor)
    
    for i in range(2, maxfactor+1):
        quotient, reminder = divmod(num, i)
        if reminder == 0:
            return False

    return True

def test():
    assert isprime(1) == True
    assert isprime(2) == True
    assert isprime(3) == True
    assert isprime(4) == False
    assert isprime(5) == True
    assert isprime(6) == False
    assert isprime(17077) == True
    assert isprime(17078) == False

def main():
    start = time.time()
    ans = 0
    test()

#    amin = -1000
    amin = -999
    amax = 1000+1

#    bmin = -1000
    bmin = 0
    bmax = 1000+1

    maxprimenumbers = -1
    production = 0

#    for a in range(amin, amax):
    a = amin
    while a <= amax:
#        for b in range(bmin, bmax):
        b = bmin
        while b <= bmax:
            n = 0
            while True:
                if isprime(n**2+a*n+b):
                    n+=1
                else:
                    break
        
            if n > maxprimenumbers:
                maxprimenumbers = n
                production = a*b
            
            if b == 0:
                b+=1
            else:
                b+=2

        a+=2
        
    ans = production
    
    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


if __name__ == '__main__':
    main()
    


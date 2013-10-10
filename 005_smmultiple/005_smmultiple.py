#!/usr/bin/env python3

# User: yamadzaki

# Problem description: Problem 5
#Smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Problem description in Russian:
#Какое самое маленькое число делится без остатка на все числа от 1 до 20?
#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?

# Worktime on Amazon microinstance: 0,0001 s
# Complexity: O(N^2), constraint by prime numbers generator

#Using observation that we can decompose any number to prime dividers. And then compare with previous set of dividers.
#We should add missing dividers and pass others.


import sys
import threading
import time
#threading.stack_size(2**27)
#sys.setrecursionlimit(2**25)


def main():
    start = time.time()

#   dividers = [2, 3, 4, 5]
#   tempdiv = [6, 4, 4, 3]
#   adddiv(dividers, tempdiv)
#        # [2, 3, 4, 4, 5, 6]

#    limit = 10 #answer = 2520
    limit = 20

    dividers = list()
    primes = primegenerator(limit)
    
    for x in range(2, limit):
        tempdiv = makediv(x, primes)
        adddiv(dividers, tempdiv)
                  
    ans = 1
    for x in dividers:
        ans = ans*x

    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


def adddiv(dividers, tempdiv):
    '''To dividers add items from tempdiv if it not in dividers. 
    Dividers should be in order, tempdiv should be in reverse order!!!!!'''

    if len(tempdiv) == 0:
        return
    
    i = 0
    j = len(tempdiv)-1
    while j >= 0:
        if (i >= len(dividers)) or (dividers[i] > tempdiv[j]):
            dividers.insert(i, tempdiv[j])
            i += 1
            j -= 1
        elif dividers[i] == tempdiv[j]:
            i += 1
            j -= 1
        else:
            i += 1

    return


class PrimesError(Exception):
    """Base class for exceptions in this module."""
    pass


def makediv(x, primes):
    '''Function return list of prime dividers of x. Complexity: seems O(N*log(N)), but not shure.'''

    if x in primes:
        lst = list()
        lst.append(x)
        return lst

    for pr in primes:
        if (x % pr) == 0:
            x = x//pr
            lst = makediv(x, primes)
            lst.append(pr)
            return lst

    raise PrimesError('Please, generate more prime numbers in variable primes')
    return None #if i'm here, it is mistake


def primegenerator(limit):
    '''Function return list of prime numbers. Complexity: O(limit^2)'''

    primes = list()

    for num in range(2, limit+1):
        isprime = True

        for pr in primes:
            if (num % pr) == 0:
                isprime = False
                break

        if isprime:
            primes.append(num)

    return primes


if __name__ == '__main__':
    #    main()
    thread = threading.Thread(target=main)
    thread.start()    
    

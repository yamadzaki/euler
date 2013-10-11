#!/usr/bin/env python3

# User: yamadzaki

# Problem description: Problem 6
#Sum square difference
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Problem description in Russian:
#Какова разность между суммой квадратов и квадратом суммы?
#Сумма квадратов первых десяти натуральных чисел
#1^2 + 2^2 + ... + 10^2 = 385
#Квадрат суммы первых десяти натуральных чисел
#(1 + 2 + ... + 10)^2 = 552 = 3025
#Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
#Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.


# Worktime on Amazon microinstance: 0.00004 s
# Complexity: O(N).

# Make some simplisity. And note: if x[i]=x[i-1]+1: (x1+x2+..xn) = (x1+xn)*n/2


import sys
import threading
import time
#threading.stack_size(2**27)
#sys.setrecursionlimit(2**25)


def main():
    start = time.time()

    #n = 3 #ans =22
    #n = 10 #ans = 2640
    n = 100

    ans = 0
    for x in range(1, n):
        ans += x * (x+1 + n)*(n-(x+1)+1) # *2 and /2
        #print(ans, x, n)


    #print(G) 
    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


if __name__ == '__main__':
    #    main()
    thread = threading.Thread(target=main)
    thread.start()    
    

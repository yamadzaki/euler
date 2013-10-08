#!/usr/bin/env python3

# User: yamadzaki

# Problem description: Problem 2 
# Even Fibonacci numbers
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Problem description in Russian:
#Найдите сумму всех чётных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
#Каждые следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Найдите сумму всех чётных элементов ряда Фибоначчи, которые не превышают четыре миллиона.


# Worktime on microinstance: 0.000014 s
# Complexity: O(maxnum)


import sys
import threading
import time
#threading.stack_size(2**27)
#sys.setrecursionlimit(2**25)


def main():
    start = time.time()

    #test case:
    #maxnum = 9
    #answer : 2+8 = 10
    maxnum = 4000000

    i1, i2 = 1, 2
    sum = 2 #don't forget first numbers: 2 (and not 1)
    while True:
        #fibonacci generator
        fib = i1 + i2
        i1 = i2
        i2 = fib

        if fib >= maxnum:
            break
            
        #even number
        if (fib % 2) == 0: 
            sum += fib

    print('Time: {:.6f}'.format(time.time()-start))
    print('Answer:', sum)

    return 0


if __name__ == '__main__':
    #    main()
    thread = threading.Thread(target=main)
    thread.start()    
    

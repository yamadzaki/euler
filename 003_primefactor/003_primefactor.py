#!/usr/bin/env python3

# User: yamadzaki

# Problem description: Problem 3
#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

# Problem description in Russian:
#Найдите самый большой делитель сложного числа, являющийся простым числом.
#Простые делители числа 13195 - это 5, 7, 13 и 29.
#Какой самый большой делитель числа 600851475143, являющийся простым числом?

# Worktime on Amazon microinstance: 0.002 s
# Complexity: from O(log(N)) to O(sqrt(N)) to O(log(N)*sqrt(N))
# Make Trial division method http://en.wikipedia.org/wiki/Trial_division


import sys
import threading
import time
#threading.stack_size(2**27)
#sys.setrecursionlimit(2**25)


def main():
    start = time.time()

    num = 600851475143
#    num = 2 #Answer: 2
#    num = 3 #Answer: 3
#    num = 6 #Answer: 3
#    num = 10 #Answer: 5
#    num = 13195 #Answer: 29 Time = 0.06
#    num = 60013*2 
#    num =  13

    #number factorization
    sqrtnum = int(num**0.5)

    answer = num
    while num > 1:
        for i in range(2, sqrtnum+1, 1):
            if (num % i) == 0:
                answer = num
                num = num//i
                #print(i)
                break
    
    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(answer))

    return 0


if __name__ == '__main__':
    #    main()
    thread = threading.Thread(target=main)
    thread.start()    
    

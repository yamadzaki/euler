#!/usr/bin/env python3

# User: yamadzaki

# Problem description: Problem 4
# Largest palindrome product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

# Problem description in Russian:
#Число-палиндром с обеих сторон (справа и слева) читается одинаково. Самое большое число-палиндром, полученное произведением двух двухзначных чисел – 9009 = 91 × 99.
#Найдите самый большой палиндром, полученный произведением двух трёхзначных чисел


# Worktime on Amazon microinstance: 0.6 s
# Complexity: N=999-100, len(x)=const, max()=O(N*log(N): O(N^2 * len(x) + N*log(N)) = O(N^2)

import sys
import threading
import time
#threading.stack_size(2**27)
#sys.setrecursionlimit(2**25)


def main():
    start = time.time()

    startnum = 999
    stopnum = 100
#    startnum = 99
#    stopnum = 10

    palindromes = list()

    for i in range(startnum, stopnum-1, -1):
        for j in range(i, stopnum-1, -1):
            product = i*j
            if ispalindrome(product):
                palindromes.append(product)

    ans = max(palindromes)

    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


def ispalindrome(x):
    x = str(x)
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            return False

    return True


if __name__ == '__main__':
    #    main()
    thread = threading.Thread(target=main)
    thread.start()    
    

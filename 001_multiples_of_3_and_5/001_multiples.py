#!/usr/bin/env python3

# User: yamadzaki

# Problem description:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# Problem description in Russian:
#Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел - 23.
#Найдите сумму всех чисел меньше 1000 кратных 3 или 5

# Worktime on Amazon microinstance: 0.0004 s
# Complexity: O(maxnum*condition) = O(N)

import time

def main():
    start = time.time()

    maxnum = 1000
    condition = [3, 5]

    sum = 0
    state = False

    for k in range(maxnum):
        state = False
        for c in condition:
            if (k % c) == 0:
                state = True
                break

        if state:
            sum += k

    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer:', sum)

    return 0


if __name__ == '__main__':
    main()
    

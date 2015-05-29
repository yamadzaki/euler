#!/usr/bin/env python3

# User: yamadzaki

# Problem description:
# ...

# Problem description in Russian:
# ...

#Worktime: 19.789631
#Answer: 4179871

# Complexity: O(?)


import sys
import time

def dividers_ref(n):
# Референс, самая простая работающая функция
# Find all dividers of n
# Найти все делители числа n
    lst = []
    for i in range(1, n):
        if (n % i) == 0:
            lst.append(i)

    return lst

def dividers(n):
# Find all dividers of n
# Найти все делители числа n
    lst = []

    if n == 1:
        return lst

    lst.append(1)

    maxdivider = n
    mindivider = 2
    while mindivider < maxdivider:
        if (n % mindivider) == 0:
            maxdivider = n // mindivider
            lst.append(mindivider)
            if mindivider < maxdivider:
                lst.append(maxdivider)
            
        mindivider += 1

    return lst

def isabundant(n):
# Является ли число n избыточным?
    lst = dividers(n)
    #print('Nim:', n, 'Dividers:', lst, 'Sum(dividers):', sum(lst))
    if sum(lst) > n:
        return True

    return False

def test():
#    print('dividers of 10:', dividers(10))
#    print('dividers_ref of 10:', dividers_ref(10))
    for i in range(1, 100):
        ret = testdividers(i)
        if not ret: 
            return False

    testisabundant(11, False)
    testisabundant(12, True)



def testisabundant(n, ans):
    if isabundant(n) == ans:
        print('isabundant', n, 'OK')
        return True
        
    print('isabundant', n, 'Error')
    return False


def testdividers(n):
    lst1 = dividers(n)
    lst2 = dividers_ref(n)
    if len(lst1) != len(lst2):
        print('testdividers', n, 'Error 1')
        return False

    if len(lst1) != len(set(lst1)):
        print('testdividers', n, 'Error 2')
        return False

    for e in lst1:
        if not e in lst2:
            print('testdividers', n, 'Error 3')
            return False

    print('testdividers', n, 'OK')
    return True



def main():
    start = time.time()
    ans = 0
    print('Start working')
    
   # test()

    
#    for i in range(1, 28123):
#        ans = dividers(i)

#    for i in range(1, 28):
#        isabundant(i)

    abundant = []
    max = 28123
#    max = 24
    for i in range(1,max+1):
        if isabundant(i):
            abundant.append(i)

#    print('abundant', abundant)
    print('Phase 1 complete. len(abundant)=', len(abundant))
    print('Worktime: {:.6f}'.format(time.time()-start))
    sumabundant = set()
    index = 0
    for i in abundant:
        for next in abundant[index:]:
            if i+next <= max:
                sumabundant.add(i+next)
            else:
                break
        index+=1
                                
#    print('sumabundant', sumabundant)                                
    print('Phase 2 complete. len(sumabundant)=', len(sumabundant))
    print('Worktime: {:.6f}'.format(time.time()-start))
    abundant = []

    for i in range(1, max+1):
        if i not in sumabundant:
            ans+=i

    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


if __name__ == '__main__':
    main()
    


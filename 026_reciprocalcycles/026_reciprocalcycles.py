#!/usr/bin/env python3

# User: yamadzaki

# Problem description:
# ...

# Problem description in Russian:
# ...

# Реализуем деление в столбик с проверкой на повторяющиеся последовательности.
#

# Worktime on Amazon microinstance:...
# Complexity: O(?)


import sys
import time

def division(numerator, denominator):
    assert type(numerator) is list

    answer = []
    recurring = []

    flag = True
    i = 0
    ost = 0
    digitsincycle = 0
    while True:

        if i < len(numerator):
            xi = numerator[i]
        else:
            xi = 0
        

        xi = ost*10+xi
        t = xi//denominator
        ost = xi-denominator*t

        #print("xi=", xi)
        #print("t=", t)
        #print("ost=", ost)
        
        if xi in recurring:
            answer.append(")")
            id = recurring.index(xi) 
            id = answer.index(".") + id +1
            answer.insert(id, "(")
            digitsincycle = len(answer) - id - 2
            #print("answer=", answer, digitsincycle)

            return answer, digitsincycle 

        if t == 0 and i >= len(numerator)-1:
            answer.append(str(t))
        elif t != 0:
            answer.append(str(t))

        #print("i=", i)
        #print("answer=", answer)

        if ost == 0 and i>=len(numerator)-1:
            #print("++++++++++++++++")
            return answer, digitsincycle 

        if i == len(numerator)-1:
            answer.append(".")

        if i >=len(numerator):
            recurring.append(xi)

        i+=1

    return answer, digitsincycle 


def list2str(lst):
    return ''.join(lst)


def int2list(num):
    lst = []
    xi = num//10
    prevxi = num

    while xi != 0:
        t = prevxi - xi*10
        lst.append(t)
        prevxi = xi
        xi = xi//10

    lst.append(prevxi)    

    lst.reverse()
    #print("num, lst=", num, lst)
    return lst


def div(num, den):
    lst, dig = division(int2list(num), den)
    return list2str(lst), dig


def test():
    #print("division:", division([0], 1))
    assert division([0], 1) == (["0"], 0)
    assert division([1, 0], 1) == (["1", "0"], 0)
    assert division([1, 0], 5) == (["2"], 0)
#    assert list2str(division([0], 1)) == "0"
    assert int2list(1) == [1]
    assert int2list(10) == [1, 0]
    assert int2list(930) == [9, 3, 0]
    assert int2list(1420067) == [1, 4, 2, 0, 0, 6, 7]

    assert div(0, 10) == ("0", 0)
    assert div(110, 1) == ("110", 0)
    assert div(500, 2) == ("250", 0)
    assert div(1, 2) == ("0.5", 0)
    assert div(1, 4) == ("0.25", 0)
    assert div(1, 3) == ("0.(3)", 1)
    assert div(3, 9) == ("0.(3)", 1)
    assert div(10, 3) == ("3.(3)", 1)

    assert div(1, 2) == ("0.5", 0)
    assert div(1, 3) == ("0.(3)", 1)
    assert div(1, 4) == ("0.25", 0)
    assert div(1, 5) == ("0.2", 0)
    assert div(1, 6) == ("0.1(6)", 1)
    assert div(1, 7) == ("0.(142857)", 6)
    assert div(1, 8) == ("0.125", 0)
    assert div(1, 9) == ("0.(1)", 1)
    assert div(1, 10) == ("0.1", 0)


def main():
    start = time.time()
    ans = 0

    test()
    maxcycle = 0
    maxstr = ""
    maxdiv = 1
    maxx = 1000
    for i in range(1, maxx):
        str, cycle = div(1, i)
      #  print("1/", i, "=", str, "  length=", cycle)
        if cycle > maxcycle:
            maxcycle = cycle
            maxstr = str
            maxdiv = i

    print("1/", maxdiv , "=", maxstr)
    ans = maxdiv

    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


if __name__ == '__main__':
    main()
    


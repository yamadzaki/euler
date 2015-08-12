#!/usr/bin/env python3

# User: yamadzaki

# Problem description:
# ...

# Problem description in Russian:
# ...

# Число всех перестановок порядка n равно факториалу n.
# То есть для [0,1,2] число перестановок 6, для [0-9] это 10! = 3 628 800
# Есть ощущение, что для решения в лоб есть простой рекурсивный алгоритм.

# Worktime on Amazon microinstance:...                                  
# Complexity: O(?)


import time

def permutations(x):
#    print('x:', x)
    y = []
    if len(x) <= 1:
        y = [x]
    else:
        for xi in x:
            newx = x[:]
            newx.remove(xi)
#            print('xi, newx:', xi, newx)
            permlist = permutations(newx)
#            permlist2 = permlist[:]
            
            for perm in permlist:
#                print('perm:', perm)
                perm.insert(0, xi)
                y.append(perm)
#                print('perm+xi:', perm)
#                print('y in perm1:', y)

#            for perm in permlist2:
#                perm.insert(-1, xi)
#                y.append(perm)
    
#    print('y:', y)
    return y
            

def main():
    start = time.time()
    ans = 0

#    lex = [0, 1, 2]
    lex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx = 999999
#    lex = [0, 1, 2, 3, 4]

    p = permutations(lex)
#    print(p)
    print(p[idx])
    l = len(p[idx])
    for pos, i in enumerate(p[idx]):
        ans = ans + i*(10**(l-pos-1))
        


    print('Worktime: {:.6f}'.format(time.time()-start))
    print('Answer: {}'.format(ans))

    return 0


if __name__ == '__main__':
    main()
    


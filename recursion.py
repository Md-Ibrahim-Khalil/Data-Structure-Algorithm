#step 1
# import sys
# sys.setrecursionlimit(10000)
# def factorial(n):
#     print(n)
#     return n * factorial(n-1)
# factorial(3)

#step - 2
# import sys
# from math import factorial
#
#
# def factorail(n):
#     if n in [0,1]:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))

#step-3
def factorial(n):
    assert n >= 0 and int(n) == n, 'the number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): 
    return [ i for i in L if i % num != 0 ]

assert myFilter([1,2,3,4,5,7], 2) == [1,3,5,7]

## Problem 2
def myLists(L):
    return [ list(range(1, x+1)) for x in L ]
assert myLists([1,2,4]) == [[1], [1,2], [1,2,3,4]]



## Problem 3
def myFunctionComposition(f, g):
    return dict( (k, g[f[k]]) for k in f.keys() )
assert myFunctionComposition( {0:'a', 1:'b'}, {'a':'apple', 'b':'banana'} ) == {0:'apple', 1:'banana'}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = .001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    curr = 0
    for x in L:
        curr += x
    return curr



## Problem 7
def myProduct(L): 
    curr = 1
    for x in L:
        curr *= x
    return curr



## Problem 8
def myMin(L):
    import sys
    curr = sys.maxsize
    for x in L:
        if (x < curr):
            curr = x
    return curr



## Problem 9
def myConcat(L): 
    curr = ""
    for x in L:
        curr += x
    return curr



## Problem 10
def myUnion(L): 
    curr = set()
    for s in L:
        curr |= s
    return curr


# Please fill out this stencil and submit using the provided submission script.
import sys
sys.path.append('..')

from GF2 import one
import plotting


## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [-1, 7]
p1_v_minus_u = [-1,-1]
p1_three_v_minus_two_u = [-3, 1]



def add(u,v):
    return [u[i] + v[i] for i in range(len(u))]
def mul(c, v):
    return [ c*x for x in v ]
## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = add(p2_u, p2_v)
p2_v_minus_u = add(p2_v, mul(-1, p2_u))
p2_two_v_minus_u = add(mul(2, p2_v), mul(-1, p2_u))
p2_v_plus_two_u = add(p2_v, mul(2, p2_u))



## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [one, 0, 0]
p3_vector_sum_2 = [0, one, one]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

u_0010010 = {'e','c','d'}
u_0100010 = {'b','e','c','d'}



## Problem 5
# Use the same format as the previous problem

v_0010010 = {'d','c'}
v_0100010 = set()



## Problem 6
from math import sqrt
uv_a = 5
uv_b = 6
uv_c = 16
uv_d = -2 * (sqrt(2)/2)**2



## Problem 7
# use 'one' instead of '1'
x_gf2 = [one,0,0,0]



## Problem 8
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]

# Ungraded plotting problem
vec_add = lambda u,v: [ u[i]+v[i] for i in range(len(u)) ]
def vec_subtract(u,v):
    return [ u[i] - v[i] for i in range(len(u)) ] 

def scalar_mult(c, v):
    return [ c*x for x in v ]

def plotln(p1, p2, alpha0=1, alpha1=0, steps=100):
    points = []
    delta = float(alpha1 - alpha0) / steps
    alpha = alpha0
    for step in range(steps):
        alpha += delta
        beta = 1 - alpha
        points.append( vec_add( scalar_mult(alpha, p1), scalar_mult(beta, p2) ) )
    plotting.plot(points)

def ungraded():
    plotln( [-1.5, 2], [3,0], -20, 20, steps=1000)
    plotln( [2,1], [-2, 2] )

# Generalization
from operator import mul

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def pi_term(k):
    return 8 / mul(4*k-3 , 4*k-1)

def summation(n,term):
    total , k = 0 , 1
    while k<=n:
        total , k = total +term(k), k+1
    return total

def sum_naturals(n):
    return summation(n,identity)

def sum_cubes(n):
    return summation(n,cube)

def sum_pi(n):
    return summation(n,pi_term)
"""Currying:Transforming a multi-argument function into 
a sign-argument ,higher-order function."""

from operator import add

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

# 或者 curry2 = lambda f: lambda x: lambda y : f(x,y)

m = curry2(add)
add_three = m(3)
print(add_three(2))
print(m(3)(2))
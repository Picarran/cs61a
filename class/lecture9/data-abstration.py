# Rational arithmetic

def add_ration(x,y):
    """Add rational numbers x and y"""
    nx , dx = numer(x), denom(x)
    ny , dy = numer(y),denom(y)
    return rational(nx*dy + ny*dx , dx*dy)

def mul_rational(x,y):
    return rational(numer(x)*numer(y) , denom(x)*denom(y))

def rationals_are_equal(x,y):
    return numer(x)*denom(y) == numer(y)*denom(x)

def print_rational(x):
    print(numer(x),"/",denom(x))


"""Abstraction Barriers不能跨越"""
# Constructor and selectors

def rational0(n,d):
    """Construct a rational number x that represents n/d"""
    return [n,d]

def numer0(x):
    """Return the numerator of rational number x"""
    return x[0]

def denom0(x):
    """Return the denominator of rational number x"""
    return x[1]


"""Constructor and selectors可以有不同的实现方式,可以是上述的列表,
也可以是下面的higher-order function
需要Constructor and selectors对应"""
def rational(n,d):
    """Construct a rational number x that represents n/d"""
    def select(name):
        if name=='n':
            return n
        elif name=='d':
            return d
    return select

def numer(x):
    """Return the numerator of rational number x"""
    return x('n')

def denom(x):
    """Return the denominator of rational number x"""
    return x('d')
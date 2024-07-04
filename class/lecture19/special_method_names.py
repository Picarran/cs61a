# Special Method Names in Python
# __init__
# __repr__ : Method invoked to display an object as a Python expression
# __add__ : Method invoked to add one object to another
# __bool__ : Method invoked to convert an object to True or False
# __float__ : Method invoked to convert an object to a float (real number)

'''
>>> zero, one, two = 0, 1 ,2
>>> one + two
3
>>> bool(zero)
False

相当于
one.__add__(two)
3
zero.__bool__()
'''

# Special Method Names in Python
# __init__
# __repr__ : Method invoked to display an object as a Python expression
# __add__ : Method invoked to add one object to another
# __bool__ : Method invoked to convert an object to True or False
# __float__ : Method invoked to convert an object to a float (real number)

'''
>>> zero, one, two = 0, 1 ,2
>>> one + two
3
>>> bool(zero)
False

相当于
one.__add__(two)
3
zero.__bool__()
'''

class Ratio:
    '''
    '''

    def __init__(self,n,d):
        self.numer = n
        self.denom = d

    def __repr__(self) -> str:
        return 'Ratio({0},{1})'.format(self.numer,self.denom)
    
    def __str__(self) -> str:
        return '{0}/{1}'.format(self.numer,self.denom)
    
    def __add__(self,other):
        if isinstance(other,int):   # 类型检查
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other,Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other,float): 
            return float(self)+other   # 类型转换
        g = gcd(n,d)
        return Ratio(n//g, d//g)
    
    __radd__ = __add__

    def __float__(self):
        return self.numer/self.denom

def gcd(a,b):
    a,b = min(a,b),max(a,b)
    while a!=0:
        a,b=b%a,a
    return b
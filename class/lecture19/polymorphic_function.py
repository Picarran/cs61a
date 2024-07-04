# __str__ : print
# __repr__ : 交互模式 Method invoked to display an object as a Python expression

class Ratio:
    '''
    >>> half=Ratio(1,2) 
    >>> half
    Ratio(1,2)
    >>> print(half) 
    1/2


    如果没有def __repr__(self) & def __str__(self)
    >>> half=Ratio(1,2) 
    >>> half
    <__main__.Ratio object at 0x00000257B8249190>
    >>> print(half) 
    <__main__.Ratio object at 0x00000257B8249190>
    eg:hw6最后一题
    '''

    def __init__(self,n,d):
        self.numer = n
        self.donom = d

    def __repr__(self) -> str:
        return 'Ratio({0},{1})'.format(self.numer,self.donom)
    
    def __str__(self) -> str:
        return '{0}/{1}'.format(self.numer,self.donom)
"""函数默认参数:如果是一个可变的类型(mutable)(list or dict),
那么其实会一个调用相同的对象

a==b : value相同
a is b : 是同一个对象(指针指向同一个)
"""

def f(s=[]):
    """
    >>> f()
    1
    >>> f()
    2
    >>> f()
    3
    """
    s.append(5)
    return len(s)
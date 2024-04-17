def plus_minus(x):
    """Yield x and -x
    >>> t = plus_minus(3)
    >>> next(t)
    3
    >>> next(t)
    -3
    >>> list(plus_minus(5))
    [5, -5]
    """
    yield x
    yield -x


# 奇数偶数的处理
def evens(start, end):
    """A generator function that returns even numbers
    
    >>> list(evens(2, 10))
    [2, 4, 6, 8]
    >>> list(evens(1, 10))
    [2, 4, 6, 8]
    """

    # 找到>=start的最小偶数
    # odd = start + (start % 2) - 1
    even = start + (start % 2)
    while even <end:
        yield even
        eve +=2

def countdown(k):
    """Count down to zero
    >>> list(countdown(5))
    [5,4,3,2,1]
    """
    if k>0:
        yield k
        yield from countdown(k-1)
        """
        相当于
        for x in countdown(k-1):
            yield x
        """


# 字符串切片
def prefixes(s):
    """Yield all prefixes of s
    >>> list(prefixes('both))
    ['b','bo','bot','both']
    """

    if s:
        yield prefixes(s[:-1])   # 除了最后一个
        yield s


# 找到字符串所以的子串
def substrings(s):
    """Yield all substrings of s
    
    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """

    if s :
        yield from prefixes(s)
        yield from substrings(s[1:])

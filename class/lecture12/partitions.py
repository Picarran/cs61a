"""用yield来返回所有可能中的举例"""

def count_partitions(n,m):
    """Count partitions.

    >>> count_partitions(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n<0 or m==0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m
    
def count_partitions1(n, m):
    """Count partitions.

    >>> count_partitions(6, 4)
    9
    """
    if n <= 0:
        return 0
    elif m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions1(n-m, m) 
        without_m = count_partitions1(n, m-1)
        return exact_match + with_m + without_m
    
def list_partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n<=0 or m==0:
        return []
    else:
        exact_match = []
        if n==m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in list_partitions(n-m, m)]
        without_m = list_partitions(n, m-1)
        return exact_match + with_m + without_m
    
def yield_partitions(n, m):
    """List partitions.

    >>> for p in yield_partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1

    compute lazily:
    >>> t = yield_partitions(60, 50)
    >>> for _ in range(3):
            print(next(t))
    10 + 50 
    1 + 9 + 50
    2 + 8 + 50
    """
    if n>0 and m>0:
        if n==m:
            yield str(m)
        # 先输出含m的,再输出不含m的
        for p in yield_partitions(n-m, m):
            yield p + '+' + str(m)
        yield from yield_partitions(n, m-1)
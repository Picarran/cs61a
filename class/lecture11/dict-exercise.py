def dict_comp(nested_tup):
    """Return a dictionary that maps each tuple to the consecutive pair of digit
    within that tuple containing the maximum absolute pairwise difference.

    >>> dict_comp(((1, 2, 5, -6, 10), (-30, 4, 20, 1)))
    {(1, 2, 5, -6, 10): (-6, 10), (-30, 4, 20, 1): (-30, 4)}
    >>> dict_comp(((1, 2), (3, 4), (5, 6)))
    {(1, 2): (1, 2), (3, 4): (3, 4), (5, 6): (5, 6)}
    """

    """
    1. max()中key的使用
    2. 用range()+index来迭代同一迭代对象中的多个元素
    """
    return {tup: max([(tup[i], tup[i+1]) for i in range(len(tup)-1)] , key=lambda x: abs(x[0]-x[1])) for tup in nested_tup}

    dct = {}
    for tup in nested_tup:
        lst=[]
        for i in range(len(tup)-1):
            lst.append((tup[i], tup[i+1]))
        dct[tup] = max(lst, key=lambda x: abs(x[0]-x[1]))
    return dct

nested_tup = ((1, 2, 5, -6, 10), (-30, 4, 20, 1))
print(dict_comp(nested_tup))



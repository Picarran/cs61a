def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    return len(list((filter(lambda x: x==x[::-1],map(lambda x : x.lower(),L)))))
if __name__=='__main__':
    x = [[1,1],[4,5],[1,4]]
    print(sum(x,[1]))

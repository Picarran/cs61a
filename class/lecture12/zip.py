"""zip()的使用
判断回文串"""

def palindrome(s):
    """Return whether s is the same sequence backward and forward.

    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """
    # return s == reversed(s)  # This version doesn't work 
    # return list(s) == list(reversed(s))

    return all([a == b for a, b in zip(s, reversed(s))])



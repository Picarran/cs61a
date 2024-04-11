

def memo_diff(diff_function):
    """A memoization function."""
    cache = {}

    def memoized(typed, source, limit):
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        if (typed, source) in cache and limit <= cache[(typed, source)][1]:
            return cache[(typed, source)][0]
        else:
            res = diff_function(typed, source, limit)
            cache[(typed, source)]=(res, limit)
            return res
        # END PROBLEM EC
    return memoized

@memo_diff
def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """

    if limit<0 or (len(typed)==0 and len(source)==0):  # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0 
        # END
    if len(typed)==0 or len(source)==0:
        return abs(len(typed)- len(source))
    
    if typed[0]==source[0]:
        cnt = 0 
        return cnt + minimum_mewtations(typed[1:], source[1:], limit)
    else:
        cnt=1
        # if len(typed)==1:
        #     if typed[0] in source:
        #         return cnt + abs(len(typed)- len(source)) - 1
        #     return cnt + abs(len(typed)- len(source))
        # if len(source) ==1:
        #     if source[0] in typed:
        #         return cnt + abs(len(typed)- len(source)) - 1
        #     return cnt + abs(len(typed)- len(source)) 
        # # sub
        # if typed[1] == source[1]:
        sub =  cnt + minimum_mewtations(typed[1:], source[1:], limit-1)
        # 多了 or 少了
        
        add = cnt + minimum_mewtations(typed[1:], source, limit-1)
        cut = cnt + minimum_mewtations(typed, source[1:], limit-1)
        return min(sub, add, cut)

# print(minimum_mewtations('rut', 'rzumt',2))
# print(minimum_mewtations('donee', 'shush', 100))
# print(sum([True , True,True ,False]))




"""

>>> from cats import minimum_mewtations, feline_fixes, autocorrect, lines_from_file
>>> all_words = lines_from_file("data/words.txt")
>>> common_words = lines_from_file("data/common_words.txt")
>>> minimum_mewtations.call_count = 0
>>> autocorrect("woll", common_words, minimum_mewtations, 4)
'well'
>>> minimum_mewtations.call_count <= 72000 # minimum_mewtations should be memoized
True
>>> minimum_mewtations.call_count = 0
>>> autocorrect("woll", common_words, feline_fixes, 4)
'well'
>>> minimum_mewtations.call_count
0
>>> minimum_mewtations.call_count = 0
>>> autocorrect("woll", common_words, minimum_mewtations, 4)  # identical to the first call
'well'
>>> minimum_mewtations.call_count
0
>>> minimum_mewtations.call_count = 0
>>> autocorrect("woll", common_words, minimum_mewtations, 4)
'well'
>>> minimum_mewtations.call_count
0
>>> minimum_mewtations.call_count = 0
>>> autocorrect("woll", common_words, minimum_mewtations, 3)
'well'
>>> minimum_mewtations.call_count < 2500
True
>>> minimum_mewtations.call_count = 0
>>> autocorrect("woll", all_words, minimum_mewtations, 2)
'will'
>>> minimum_mewtations.call_count < 2700000
False

"""


# lst = [1]
# print(lst[1:])

dic = {}
dic[1] = {1,2}
print(dic)
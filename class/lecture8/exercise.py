"""递归计数"""
"""方法一,直接用递归次数相加,适用于递归一次cnt加1"""
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)

"""方法二:将cnt作为参数进行传递,根据条件对cnt进行操作,最后在基础情况return cnt"""
def waves(n):
    """from hw02
    Return whether n is balanced.

    >>> waves(1)
    True
    >>> waves(10001)
    False
    >>> waves(12233121)
    False
    >>> waves(1313)
    True
    >>> waves(12332023213)
    True
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'waves',
    ...       ['For', 'While'])
    True
    """
    def helper(n, count, prev):
        if n//10==0:
            return count
        curr, next, rest = n % 10, (n // 10) % 10, n // 10
        "*** YOUR CODE HERE ***"
        if next == curr:
            return helper(rest,count,prev)
        if prev < curr and next < curr :
            count+=1
        elif prev > curr and next > curr :
            count-=1
        return helper(rest,count,curr)
    return (helper(n // 10, 0, n % 10)==0)

"""
体会如何进行value的传递:返回的是算出来的结果,
那这一步要返回的结果就是在上一个返回结果基础上的处理：
例如: return merge(n1 // 10, n2) * 10 + n1 % 10
"""
def merge(n1, n2):
    """ Merges two numbers
    Write a procedure merge(n1, n2) which takes numbers with digits in decreasing order 
    and returns a single number with all of the digits of the two, in decreasing order. 
    Any number merged with 0 will be that number 
    (treat 0 as having no digits).(merge(11,0)->10;but merge(100,1)->1100) 
    Use recursion.

    Hint: If you can figure out which number has the smallest digit out of both, 
    then we know that the resulting number will have that smallest digit, 
    followed by the merge of the two numbers with the smallest digit removed.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    >>> merge(9854, 6421)  # I added one more test case
    98654421
    """
    if n1 == 0:  # cases when remaining n2 is larger than n1
        return n2
    elif n2 == 0:  # cases when remaining n1 is larger than n2
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    
if __name__ =='__main__':
    print(merge(100,21))


def count_stair_ways(n):
    """Imagine that you want to go up a flight of stairs that has n steps, 
    where n is a positive integer. You can either take 1 or 2 steps each time. 
    How many different ways can you go up this flight of stairs? In this question, 
    you'll write a function count_stair_ways that solves this problem.
    
    Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n==1 or n==2:
        return n
    return count_stair_ways(n-1)+count_stair_ways(n-2)


"""
基础情况的分析：
能找到递归方式,但是怎么确定基础情况?
代数模拟!!(count_k(3,3))
"""
def count_k(n, k):
    """
    Consider a special version of the count_stair_ways problem, 
    where instead of taking 1 or 2 steps, we are able to take up to and including k steps at a time. 
    Write a function count_k that figures out the number of paths for this scenario. 
    Assume n and k are positive.

    Hint: Your solution will follow a very similar logic to what you did for count_stair_ways.
    
    Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n==0:
        return 1
    if n<0:
        return 0
    i,total=1,0
    while i<=k:
        total += count_k(n-i,k)
        i+=1
    return total
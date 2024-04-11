"""函数调用次数记录;
用memorization大大减少递归的调用次数与时间
(decorator的应用)"""

def count(f):
    """一个decorator,记录函数被调用了多少次
    >>> fib = count(fib)
    >>> fib.call_count
    0
    >>> fib(5)
    5
    >>> fib.call_count
    15
    >>> fib(1)
    1
    >>> fib.call_count
    16
    """
    def counted(n):
        counted.call_count +=1
        return f(n)
    """可以这样定义关于这个counted函数的参数"""
    counted.call_count = 0
    return counted


"""相当于fib = count(fib)"""
# @count
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2)+ fib(n-1)

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n]= f(n)
        # 否则f(n)在cache里,不用再算了
        return cache[n]
    return memorized

"""记录最基础的fib()被调用了多少次"""
fib = count(fib)
counted_fib = fib

fib = memo_plus(fib)
"""记录最memo版本的fib()被调用了多少次"""
fib = count(fib)

"""
>>> fib(30) 
832040
>>> fib.call_count
59  (总步数,包括调用fib()的次数 + 查储存的次数)
>>> counted_fib.call_count
31  (因为每算出一个斐波那契数都会记录下来,要算fib(30),那么每一次分别算出fib(0-30))
"""


"""更通用的"""
def deep_convert_to_tuple(sequence):
    """Deeply converts tuples to lists.
    >>> deep_convert_to_tuple(5)
    5
    >>> deep_convert_to_tuple([2, 'hi'])
    (2, 'hi')
    >>> deep_convert_to_tuple([['These', 'are', 'all'], ['tuples.']])
    (('These', 'are', 'all'), ('tuples.',))
    """
    if isinstance(sequence, list) or isinstance(sequence, tuple):
        return tuple(deep_convert_to_tuple(item) for item in sequence)
    else:
        return sequence


def memo_plus(f):
    cache = {}
    def memo_plus1(*args):
        immutable_args = deep_convert_to_tuple(args)    # 参数处理的时候不用加*
        if immutable_args not in cache:
            cache[immutable_args] = f(*args)   # 在函数传参时候要加*
        return cache[immutable_args]
    return memo_plus1
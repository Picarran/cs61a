# Tree

def tree(label , branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be tree'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

if __name__=='__main__':
    """
    >>> tree(1,[5])
    AssertError : branches must be tree
    1的分支应该是:没有分支的且label为5的树([[5]]):外面的括号代表[5]为1的分支,里面的括号代表没有分支label为5的树
    所以应该是tree(1,[[5]]), 但不要这样写!!!
    >>> tree(1,[tree(5)])
    [1, [5]]
    >>> tree(1,[tree(5,[tree(7)]),tree(6)])
    [1, [5 , [7]] , [6]]
    """
    # tree(1,[5])
    tree(1,[tree(5)])
    tree(1,[tree(5,[tree(7)]),tree(6)])


### +++ === ABSTRACTION BARRIER === +++ ###

def exponential_tree(n):
    """用递归描述(/生成)整棵树
    >>> exponential_tree(2)
    [2, [1, [0], [0]], [1, [0], [0]]]
    >>> exponential_tree(3)
    [3, [2, [1, [0], [0]], [1, [0], [0]]], [2, [1, [0], [0]], [1, [0], [0]]]]
    """
    if n==0:
        return tree(0)
    left , right = exponential_tree(n-1), exponential_tree(n-1)
    return tree(n,[left,right])

def fib_tree(n):
    """example : fib"""
    if n<=1:
        return tree(n)
    left , right = fib_tree(n-2), fib_tree(n-1)
    return tree(label(left)+label(right) , [left,right])
    
def count_leaves(t):
    """The number of leaves in tree
    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(t):
        return 1
    else:
        """sum():所加的类型和start值相同(默认:0(int))"""
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    """Return a list containing the leaf labels of tree
    
    >>> leaves(fib_tree(5))
    [1,0,1,0,1,1,0,1]
    """
    if is_leaf(tree):
        return [label(tree)]
    return sum([leaves(b) for b in branches(tree)] , [])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label
    is indented by two spaces times its depth from the root
    
    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """

    """处理输出缩进的方法!!!"""
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)



def increment_leaves(t):
    """
    基于一棵树创建一颗新树
    Return a tree like t but with leaf labels incremented
    
    >>> print_tree(increment_leaves(fib_tree(4)))
    3
      1
        1
        2
      2
        2
        1
          1
          2
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t) , bs)

def increment(t):
    """Return a tree t but with all labels incremented"""
    """基础情况时branches(t)为空,不会再进入递归,开始返回"""
    return tree(label(t)+1 , [increment(b) for b in branches(t)])

"""递归的两种方式"""
"""
1.对每次的返回值进行操作
"""
def fact1(n):
    if n==0:
        return 1
    else:
        return n * fact1(n-1)
    
"""
2.每次更新result,最后得到result一路返回
"""
def fact2(n):
    def fact_times(n,ans):
        if n==0:
            return ans
        ans *= n
        return fact_times(n-1,ans)
    return fact_times(n,1)


haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])
"""
>>> print_tree(haste):
h
  a
    s
    t
  e
"""
def print_sum(t,path_sum):
    """Print the sum of labels along the path from root to each leaf.
    
    >>> print_sums(tree(3, [tree(4), tree(5, [tree(6)])]), 0)
    7
    14
    >>> print_sums(haste, '')
    has
    hat
    he
    """
    path_sum += label(t)
    if is_leaf(t):
        print(path_sum)
    else:
        for branch in branches(t):
            print_sum(branch, path_sum)


def count_paths(t, total):
    """Return the number of paths from the root to any node in t 
    for which the labels along the path sum to total.

    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> print_tree(t) 
    3
      -1
      1
        2
          1
        3
      1
        -1
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    
    # if is_leaf(t):
    #     return found
    # for b in branches(t):
    #     found += count_paths(b, total-label(t))
    # return found
    """这里与上面等价,sum()很好地处理了最后到leaf的返回问题,
    同时处理了两种情况:
    1. 到leaf时候:sum([]),返回found(1/0:取决于leaf满不满足条件) + 0
    2. 每次到一个节点(树),返回该节点的found(1/0:取决于该节点满不满足条件) 
        + sum[branch1, branch2, ...](每个分支的found数,组成列表然后求和)
    """
    return found + sum([count_paths(b, total-label(t)) for b in branches(t)])

### ====================================================== ###
# exercise
def find_path(t, x):
    """
    Write a function that takes in a tree and a value x 
    and returns a list containing the nodes along the path 
    required to get from the root of the tree to a node containing x.
    
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    # if ___:
    #     return _____________________________
    # _____________________________:
    #     path = ______________________
    #     if _____________________________:
    #         return _____________________________
            
    if label(t)==x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path
        
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    """"
    当你对数组操作了,那就触及到tree的实现了,跨越了ABSTRACTION BARRIER,  BURN IT !!!!!
    t0 = t[:]
    if is_leaf(t):
        t.append(leaves)
        return
    for b in branches(t):
        sprout_leaves(b, leaves)
    return t
    """

    if is_leaf(t):
        return tree(label(t), [tree(leaf) for leaf in leaves])
    return tree(label(t), [sprout_leaves(b, leaves) for b in branches(t)])




if __name__=='__main__':
    # t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    # find_path(t,5)

    t1 = tree(1, [tree(2), tree(3)])
    new1 = sprout_leaves(t1, [4, 5])


def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"

    # if is_leaf(t):
    #     return label(t)
    return label(t) + sum([sum_tree(b) for b in branches(t)])

def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"

    """
    # if is_leaf(t):
    #     return True
    
    lst = []
    for b in branches(t):
        lst.append(sum_tree(b))
    lst = list(set(lst))        # *** set():去重
    if (len(lst) in [0,1]):
        for b in branches(t):
            if balanced(b)==False:
                return False
        return True
    return False
    """
    
    # for b in branches(t):
    #     """
    #     1. 找到更特殊的情况(False 还是 True)直接返回,否则完成迭代返回另一种情况
    #     2. ***判断每次迭代是否相同,开头元素的处理
    #     """
    #     if sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b):
    #         return False
    # return True

    """all():
    Return True if bool(x) is True for all values x in the iterable.
    If the iterable is empty, return True."""
    return all([sum_tree(branches(t)[0])==sum_tree(b) and balanced(b) for b in branches(t)])

def add_trees(t1, t2):
    """
    Define the function add_trees, which takes in two trees and returns a new tree 
    where each corresponding node from the first tree is added with 
    the node from the second tree. 
    If a node at any particular position is present in one tree but not the other, 
    it should be present in the new tree as well. 
    At each level of the tree, nodes correspond to each other starting 
    from the leftmost node.

    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """

    "*** YOUR CODE HERE ***"
    if is_leaf(t1):
        return tree(label(t1)+label(t2), branches(t2))
    if is_leaf(t2):
        return tree(label(t1)+label(t2), branches(t1))
    bs = []
    len_bs = max(len(branches(t1)), len(branches(t2)))
    for i in range(len_bs):
        if i >=len(branches(t1)):
            b = branches(t2)[i]
        elif i >= len(branches(t2)):
            b = branches(t1)[i]
        else:
            b = add_trees(branches(t1)[i], branches(t2)[i])
        bs.append(b)
    return tree(label(t1)+label(t2), bs)
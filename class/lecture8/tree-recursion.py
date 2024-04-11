"""
树递归:用于探索不同选择或者不同的可能性(但不能用于像斐波那契数列的递归)
原理见md文件
Example:Counting Partitions
The number of partitions of a positive integer n, 
using parts up to size m, is the number of ways in which n can be expressed 
as the sum of positive integer parts up to m in increasing order.
>>> count_partitions(6,4)
9
ps:
2+4=6
1+1+4=6
3+3=6
1+2+3=6
1+1+1+3=6
2+2+2=6
1+1+2+2=6
1+1+1+1+2=6
1+1+1+1+1+1=6
"""
def count_partitions(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        with_m = count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m + without_m
    
def count_partitions2(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==1:
        """m==1,那只能有一种分类方式:全部1加起来"""
        return 1
    else:
        with_m = count_partitions2(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m + without_m
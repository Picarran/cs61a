# coding: utf-8
# 计算幂次
# 两种模拟方法：数位调转？ -> 乘/除 合适的参数
# round(num,n) 四舍五入到n位小数，不传入n时默认到整数

def remove(n,digit):
    """Return all digits of non-negative N
    that are not DIGIT, for some 
    non-negative DIGIT less than 10
    >>> remove(231,3)
    21
    >>> remove(243132,2)
    4313
    """

    kept ,digits = 0,0
    while n>0:
        n,last = n//10,n%10
        if last!=digit:
            kept = kept + last*10**digits   # 计算幂次
            digits+=1
    return kept

def remove1(n,digit):
    kept,digits =0,0
    while n>0:
        n,last=n//10,n%10
        if last!=digit:
            kept=kept/10 +last
            digits+=1
    return round(kept*10**(digits-1))   #四舍五入到n位小数，不传入n时默认到整数

if __name__ =='__main__':
    print(remove1(231,3))
    print(remove1(243132,2))
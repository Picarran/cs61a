# 쳲���������
def fib(n):
    pred , curr = 0, 1
    # pred , curr = 1, 0    #��0��ʼ
    k=1
    while k<n:
        pred,curr = curr,pred+curr
        k+=1
    return curr
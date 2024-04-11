# 得到一个函数的反函数（只能考虑整数）

def search(f):
    """
    实现:从0开始一个个找x,看是否满足f(x),若满足,返回x
    """
    x=0
    while True:
        if f(x):
            return x
        x+=1

def square(x):
    return x*x

def inverse(f):
    """Return the g(y) such that g(f(x))=x"""
    return lambda y : search(lambda x :f(x)==y)

if __name__ =='__main__':
    sqrt = inverse(square)
    print(sqrt(25))
# a function that prints an inverse cascade
"""
>>> inverse_cascade(1234)
1
12
123
1234
123
12
1
"""
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n :f_then_g(grow , print , n//10)
shrink = lambda n :f_then_g(print,shrink,n//10)

if __name__=='__main__':
    inverse_cascade(1234)
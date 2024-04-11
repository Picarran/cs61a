square = lambda x: x*x
print(square(10),square(100))
"""
Unlike def statements, lambda expressions can 
be used as an operator or an operand to a call expression. 
This is because they are simply one-line expressions that evaluate to functions. 
In the example below, (lambda y: y + 5) is the operator and 4 is the operand.
>>> (lambda y : y+5)(4)
9
>>> (lambda f,x : f(x))(lambda y :y+1 ,10)
11
(lambda y :y+1 ,10)是传入的值,
lambda y :y+1对应f,10对应x
"""
print((lambda y : y+5)(4))
print((lambda f,x : f(x))(lambda y :y+1 ,10))
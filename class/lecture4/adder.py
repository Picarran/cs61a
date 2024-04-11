# functions as return value
def make_adder(n): # parent = G(global)
    def adder(k): # parent = make_adder
        return n+k
    return adder

add_three = make_adder(3)
print(add_three(4))
print(make_adder(3)(4))

# function composition
def square(x):
    return x*x

def triple(x):
    return 3*x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

tripare = compose1(triple,square)
print(tripare(5))

print(compose1(square,make_adder(2))(2))
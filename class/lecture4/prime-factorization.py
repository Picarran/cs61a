def prime_factor(n):
    """Print the prime factor of n in non_decreasing oder
    
    >>> prime_factor(8)
    2
    2
    2
    >>> prime_factor(11)
    11
    >>> prime_factor(858)
    2
    3
    11
    13
    """
    while n > 1:
        k=smallest_prime_factor(n)
        print(k)
        n//=k

def smallest_prime_factor(n):
    i=2
    while n % i != 0:
        i+=1
    return i
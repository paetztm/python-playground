
def add(increment):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return increment + func(*args, **kwargs)
        return wrapper
    return decorator

@add(3)
def f(n):
    return n+2

print f(4)

def multiply(multiplicative):
    def decorator(func):
        def wrapper(*args, **kwargs):
            multiplicative * func(*args, **kwargs)
        return wrapper
    return decorator

@multiply(7)
def g(n):
    return n + 5

print g(7)

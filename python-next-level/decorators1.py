
def printlog(func):
    def wrapper(*args, **kwargs):
        print 'CALLING: {}'.format(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@printlog
def f(n):
    return n+2

items = ["apples", "oranges", "bananas"]
@printlog
def find_max():
    return max(items, key=lambda x: len(x))
print f(3)

def check_id(func):
    def wrapper(arg):
        print "ID of func: {}".format(id(func))
        return func(arg)
    print "ID of wrapper: {}".format(id(wrapper))
    return wrapper

@check_id
def g(x):
    return x * 3

print g(3)

print id(g)


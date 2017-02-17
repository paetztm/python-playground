
class PrintLog(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print "Calling: {}".format(self.func.__name__)
        return self.func(*args, **kwargs)


@PrintLog
def f(n):
    print n + 1


f(3)

print type(PrintLog)


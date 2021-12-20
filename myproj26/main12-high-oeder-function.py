# 장식자(Decorators)
def base_10(fn):
    def wrap(x, y):
        return fn(x, y) + 10

    return wrap


# @base_10
# @base_10
def mysum(x, y):
    return x + y


mysum = base_10(base_10(mysum))

print(mysum(1, 2))

def mysum2(x, y):
    return x + y + 10


def mysum3(x, y, z):
    return x + y + z + 10


# 가변인자
def mysum(x, y, *args):  # x,y 를 넣는 이유는 최소 2개는 받고 싶다는 말임 x,y에 먼저 저장되고 남은게 저장되기 때문
    # args is tuple
    print("args:", x, y, args)
    return x + y + sum(args) + 10


# print(mysum())
# print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 2, 3))

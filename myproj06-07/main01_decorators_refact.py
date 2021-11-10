import time

# 인자에 대한 리턴값을 저장
# -key: 인자 값에 대한 튜플
# -value: 그 인자로 함수를 수행했을 때의 리턴 값
# cached = {}  # 전역변수 (가급적 지양)


# def mysum2(x, y):
#     key = (x, y)
#     if key not in cached:  # 새로운 값이라면 1초를 대기하고, 이미 값이 있으면 바로 출력
#         time.sleep(1)  # 1초간 대기
#         cached[key] = x + y + 10
#     return cached[key]

# def mymiltply2(x, y):
#     time.sleep(2)  # 위 코드와 다른 점은 같은 값이 있어도 대기
#     return x * y + 10
# 만약 여기에도 위와 같은 cached를 사용한다면 해당 코드 (1,2)를 이용하면 13의 값이 나온다
# 즉 값을 따로따로 저장해야한다 cached2={}을 만들어야함

"""데코레이터 이용"""


def memoize(fn):
    cached = {}

    def wrap(x, y):
        key = (x, y)
        if key not in cached:
            cached[key] = fn(x, y)
        return cached[key]

    return wrap


# 데코레이터를 사용하면 각각 함수에 대한 인자 결과를 구현하는 것을 만든다-cached2를 만들지 않아도 됨
@memoize  # 41번을 대체 @를 쓰는 문법이 데코레이터
def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


# mysum2 = memoize(mysum2)  # memoize에 계산되는 것을 mysum2을 통해 만들고 mysum2에 저장
# other_fn(1,2)


@memoize  # 49을 대체
def mymiltply2(x, y):
    time.sleep(1)
    return x * y + 10


# mymiltply2 = memoize(mymiltply2)

print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 4))
print(mysum2(1, 2))
print(mysum2(1, 2))

print(mymiltply2(1, 2))
print(mymiltply2(1, 3))
print(mymiltply2(1, 4))

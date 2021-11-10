# name="Tom"
# mysum=lambda x,y:x+y

# other_name=name
# other_fn=mysum

# def fn(x):
#     y="hello"
#     return y
# fn(name)

# def base(base_number):
#     # fn = lambda x, y: x + y + 10 #아래 2줄 코드와 같음
#     # def fn(x, y):
#     #     return x + y + 10
#     def fn(x, y):
#         return x + y + base_number

#     return fn


# other_fn1 = base(10)  # base_10를 이용할 것이야
# other_fn2 = base(20)
# print(other_fn1(1, 2))
# print(other_fn2(1, 2))

import time

# 인자에 대한 리턴값을 저장
# -key: 인자 값에 대한 튜플
# -value: 그 인자로 함수를 수행했을 때의 리턴 값
cached = {}  # 전역변수 (가급적 지양)


def mysum2(x, y):
    key = (x, y)
    if key not in cached:  # 새로운 값이라면 1초를 대기하고, 이미 값이 있으면 바로 출력
        time.sleep(1)  # 1초간 대기
        cached[key] = x + y + 10
    return cached[key]


def mymiltply2(x, y):
    time.sleep(2)  # 위 코드와 다른 점은 같은 값이 있어도 대기
    return x * y + 10


# 만약 여기에도 위와 같은 cached를 사용한다면 해당 코드 (1,2)를 이용하면 13의 값이 나온다
# 즉 값을 따로따로 저장해야한다 cached2={}을 만들어야함


print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 4))
print(mysum2(1, 2))
print(mysum2(1, 2))

print(mymiltply2(1, 2))
print(mymiltply2(1, 3))
print(mymiltply2(1, 4))

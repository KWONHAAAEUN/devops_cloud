# def base_10(fn):  # 장식자
#     def wrap(x, y):
#         return fn(x, y) + 10

#     return wrap

# def base_20(fn):  # 장식자
#     def wrap(x, y):
#         return fn(x, y) + 20

#     return wrap

"""10,20.. 모든 경우의 수를 def 하기 싫어서 만든 코드"""


def base(base_number):
    def wrap(fn):  # 장식자
        def inner(x, y):
            return fn(x, y) + base_number

        return inner

    return wrap


# base_10 = base(10)
# base_20 = base(20)
# base_100 = base(100)
# 이 코드들을 사용하려면 base_10, base_20 을 이용해야하고
# base(10)과 같이 실행하면 바로 값이 들어가기에 필요 없다


@base(10)  # 순서대로 진행
# @base_20
# @base_100
def mysum2(x, y):  # @를 쓰지 않았으면 3이 나왔을 것
    return x + y


# def mymultiply2(x,y):
#     return x*y

print(mysum2(1, 2))

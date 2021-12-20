def get_default_value():
    print("get_default_value()를 호출")
    return 10


# 함수 정의 시점에 호출이 된다
def hello(name, age=get_default_value()):
    print(f"인녕 나는 {name}이야 {age}살이지")


# 파이썬에서 default 값이 필요할 때마다, 그 함수가 호출되게 하려면?
# 인자 두 개를 맞춰주어야 함, js에만 undefined가 있음
def hello(name, age=None):
    if age is None:
        age = get_default_value()
    print(f"안녕 아는 {name}이야 {age}살이지")


hello("Tom")
hello("Steve")
hello("John")

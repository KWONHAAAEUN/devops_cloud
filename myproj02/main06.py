def gugudan(number):
    # number = 2
    print(f"#### {number}단 ####")
    for i in range(1, 10):
        print(f"{number}*{i}={number*i}")


for j in range(1, 10):
    gugudan(j)


# gugudan()
# gugudan()
# gugudan() #3번 출력
# def로 정의한 것은 아래에서 호출함수를 사용하지 않으면 출력되지 않음
# 여러개의 인자(구구단의 단)중 특정 부분만 호출해야할때 유용할것이라 생각이 들음


# gugudan()을 정의할때 함수를 넣는다면 아래 호출의 경우 숫자를 넣으면 바로 출력가능

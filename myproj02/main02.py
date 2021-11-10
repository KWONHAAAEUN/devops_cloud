answer = input("12+23=")
# answer를 가지고 계산을 할 목적이라면, answer 값 변환은 최대한 빠르게 하는 것이 좋다.
answer = int(answer or 0)
# if문을 하나 더 작성하여 answer의 길이가 0일 때와
# 0이 아닐 때로 나누어 else 값일 때는 int 값으로 변환하는 부분을 사용해도 된다.

if answer == 35:
    print("정답")
else:
    print("땡")

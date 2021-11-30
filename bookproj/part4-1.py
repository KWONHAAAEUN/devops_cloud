# 1~10 사이 랜덤 수를 두 변수에 저장하고 값 비교하기
import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)

print("첫번 째 수:", guess, "두번 째 수:", secret)

if guess < secret:
    print("too low")
elif guess == secret:
    print("just right")
else:
    print("too higt")

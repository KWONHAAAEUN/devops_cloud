# 숫자 퀴즈
# 랜덤 숫자를 맞춰보세요

# 힌트:random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다

# 유저에게 10회의 기회를 준다 for/range 사용
# 숫자를 맞췄다면, 몇 번 만에 맞췄는 지 출력
# 입력한 숫자가 랜덤수보다 작다면, '더 큰 수를 입력해주세요'라고 출력
# 작다면, '더 작은 수를 입력해주세요'라고 출력
# 횟수를 초과했다면, '다음 기회에..'를 출력

import random

randomnum = random.randint(1, 100)

count = 1
for i in range(10):
    mynum = input("1~100 숫자를 입력하세요: ")
    mynum = int(mynum)
    if randomnum == mynum:
        print(f"{count}번만에 맞췄습니다")
        break
    elif 100 >= mynum > randomnum:
        count += 1
        if count == 11:
            break
        else:
            print("랜덤수보다 작은 수를 입력해주세요")

    elif 1 <= mynum < randomnum:
        count += 1
        if count == 11:
            break
        else:
            print("랜덤수보다 큰 수를 입력해주세요")

    elif mynum < 1 or mynum > 100:
        count += 1
        if count == 11:
            break
        else:
            print("범위에 맞지 않는 수를 입력하였습니다")

if count == 11:
    print("다음 기회에..")

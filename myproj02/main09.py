import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]
input("준비되셨으면 엔터키를 눌러주세요")

random.shuffle(animal_names)

begin_time = time.time()

ok_counter = 0

# for count in range(5):
#     random_name = random.choice(animal_names)
# 중복 제거 방법1: 이미 사용된 random_name을 받았다면 다시 가져오는것
# 셔플 후에 범위를 뽑는다

for random_name in animal_names[0:5]:
    print(random_name)
    line = input(">>>")
    if random_name == line:
        ok_counter += 1
        print("정확합니다")
    else:
        print("오타가 있습니다")

end_time = time.time()

print(f"{ok_counter}번 성공하셨습니다")
print(f"{end_time-begin_time}초가 걸리셨습니다")

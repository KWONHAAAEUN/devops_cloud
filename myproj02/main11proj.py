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
len_sum = 0
for random_name in animal_names[0:5]:
    len_sum += len(random_name)  # random으로 받은 글자들의 수를 누적 저장
    print(random_name)
    line = input(">>>")
    if random_name == line:
        ok_counter += 1
        print("정확합니다")
    else:
        print("오타가 있습니다")

end_time = time.time()

speed = (len_sum * 60) // (end_time - begin_time)  # 분당 타이핑 속도를 구하는 공식

print(f"{ok_counter}번 성공하셨습니다")
print(f"{end_time-begin_time}초가 걸리셨습니다")
print(f"분당 타이핑 속도는{speed}입니다")

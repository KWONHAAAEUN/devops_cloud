# while을 이용해 변수 크기 비교

guess_me = 7
number = 3

for x in range(10):
    while True:
        if number < guess_me:
            print(x, "too low")
        elif number == guess_me:
            print(x, "found it!")
            break
        else:
            print("oops")
            break
        number += 1

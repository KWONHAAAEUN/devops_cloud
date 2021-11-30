guess_me = 5
number = input("숫자 하나를 입력하세요")

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break

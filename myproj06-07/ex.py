mylist = [1, 2, 3, 4, 5]

for number in mylist:
    print(number)

mylist2 = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for number in mylist2:
    print(number)

x, y = 1, 2
x, y = [1, 2]

for x, y in mylist2:
    print(x, y)

s = "안녕하세여"

for idx, ch in enumerate(s):
    print(idx, ch)


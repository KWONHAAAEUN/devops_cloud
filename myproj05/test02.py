# def check_even_number(number):
#     return number % 2 == 0

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numbers in filter(check_even_number, numbers):
#     print(numbers)

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

print("=========================")
print("방탄소년단 곡명만 출력하기")
print("=========================")


def filter_fn1(song_dict):
    return song_dict["artist"] == "방탄소년단"


for song_dict in filter(filter_fn1, song_list):
    print(song_dict["title"])

print("=========================")
print('곡명에 "사랑"이 포함된 곡명만 출력')
print("=========================")


def filter_fn2(song_dict):
    return "사랑" in song_dict["title"]


for song_dict in filter(filter_fn2, song_list):
    print(song_dict["title"])

print("=========================")
print('"좋아요"수가 200000이상인 곡만 출력')
print("=========================")


def filter_fn3(song_dict):
    return song_dict["like"] > 200_000


for song_dict in filter(filter_fn3, song_list):
    print(song_dict["title"])


print("=========================")
print("제목 정렬해서 출력하기")
print("=========================")


def filter_fn4(song_dict):
    return song_dict["like"] > 200_000


def sort_fn4(song_dict):
    return song_dict["title"]


new_song_list = filter(filter_fn4, song_list)
new_song_list = sorted(new_song_list, key=sort_fn4)

for song_dict in new_song_list:
    print(song_dict["like"], song_dict["title"])

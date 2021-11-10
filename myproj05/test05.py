import pandas as pd
from collections import Counter

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 07. 멜론 top100리스트에서 2곡 이상 랭크된 가수는 몇 팀인가요?

top100_artist = []
result = []

def rank_list(song_dict):
    artist = song_dict["artist"]
    return artist


top100_artist = list(map(rank_list, song_list))  # 가수 이름 총 목록

result = Counter(top100_artist)
sum = 0
print("2곡 이상 랭크된 가수는")
for a, value in result.items():
    if value >= 2:
        print(a)
        sum += 1
print("총 ", sum)

# if len(top100_artist) >= 2:
#     team_count = len(top100_artist)
#     print(f"2곡 이상 랭크된 가수는{top100_artist}로 총{team_count}입니다")

# top100_artist1 = []


# def filter_fn10(song_dict):
#     return len(song_dict["artist"]) >= 2


# print(list(filter(filter_fn10, song_list)))

# top100_artist1 = list(set(map(rank_list1, song_list)))

# print(f"top100에 2곡 이상 랭크된 가수 목록은 : {top100_artist1}", "총", len(top100_artist1), "팀입니다")


# print(len(result))

# for artist in counter:
#     print(artist)
# print("랭크가 된 가수들은 :", top100_artist, "총 ", result.count(), "팀 입니다")

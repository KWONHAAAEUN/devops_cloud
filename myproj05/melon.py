import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# for song_dict in song_list:
#     if song_dict["artist"]=="방탄소년단":
#         print(song_dict["title"])

# 가수 별 곡 수
artist_list = []
artist_dict = {}

for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_list.append(artist)

    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1

print(artist_dict)

# 가수 별 곡 수 사전을 이용하는 방법
# print(artist_list)
# {
#     artist_list
# }

# list comprehension
from collections import counter

artist_list = [song_dict["artist"] for song_dict in song_list]

print(counter(artist_list))

counter = Counter(artist_list)

for artist in counter:
    print(artist)

for song_count in counter.vlaues():
    print(song_count)

for artist in counter:
    print(artist, counter[artist])

for artist, song_count in counter.items():
    print(artist, song_count)

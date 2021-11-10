import pandas as pd
from typing import List
from pprint import pprint

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def pick_like_value(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, key=pick_like_value, reverse=True)

for song_dict in sorted_song_list[0:10]:
    # 210 줄을 지우고 in 뒤에 아래 코드를 넣는 것으로 대체 가능
    # sorted(song_list, key=pick_like_value,reverse=True)[:10]:
    print("{like} {title}".format(**song_dict))


# def get_title_and_length_for_song(song_dict):
#     title: str = song_dict["title"]
#     return [title, len(title)]


# def check_bts_song(song_dict):
#     return song_dict["artist"] == "방탄소년단"


# for idx, title, length in enumerate(
#     map(get_title_and_length_for_song, filter(check_bts_song, song_list))
# ):
#     print(
#         "{title} {length} {like} {artist}".format(
#             title=title, length=length, **song_list[idx]
#         )
#     )

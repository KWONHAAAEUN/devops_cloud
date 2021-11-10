import pandas as pd
from typing import List
from pprint import pprint
from collections import defaultdict
from collections import Counter

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

like_sum_for_bts = sum(
    [song_dict["like"] for song_dict in song_list if song_dict["artist"] == "방탄소년단"]
)
print(like_sum_for_bts)
# def get_title_and_length_for_song(song_dict):
#     title: str = song_dict["title"]
#     return [title, len(title)]


# def check_bts_song(song_dict):
#     return song_dict["artist"] == "방탄소년단"


# for idx, (title, length) in enumerate(
#     map(get_title_and_length_for_song, filter(check_bts_song, song_list))
# ):
#     print(
#         "{title} {length} {like} {artist}".format(
#             title=title, length=length, **song_list[idx]
#         )
#     )

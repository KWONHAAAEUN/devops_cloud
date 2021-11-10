import pandas as pd
from typing import List
from pprint import pprint

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# def check_bts_song(song_dict):
#     return len(song_dict["artist"]) >= 3


# def get_title_and_length_for_song(song_dict):
#     title: str = song_dict["title"]
#     like: int = song_dict["like"]
#     return like * len(title)


# for idx, like_length in enumerate(
#     map(get_title_and_length_for_song, filter(check_bts_song, song_list))
# ):
#     print(
#         "{title} {artist} {like_length}".format(
#             like_length=like_length, **song_list[idx]
#         )
#     )


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    return [title, len(title)]


def check_bts_song(song_dict):
    return song_dict["artist"] == "방탄소년단"


for idx, title, length in enumerate(
    map(get_title_and_length_for_song, filter(check_bts_song, song_list))
):
    print(
        "{title} {length} {artist}".format(
            title=title, length=length, **song_list[idx]
        )
    )

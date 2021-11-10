import pandas as pd
from pprint import pprint  # pprint를 이용해서 출력하면 print가 정렬된다
from typing import List  # 타입 힌팅을 사용한다

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    return [title, len(title)]


def check_bts_song(song_dict):
    return song_dict["artist"] == "방탄소년단"


# 목록을 반환
# 필터로는 방탄소년단이라는 아티스트를 뽑고 맵으로는 타이틀의 단어 수와 타이틀 곡을 고른다
for title, length in map(
    get_title_and_length_for_song, filter(check_bts_song, song_list)
):
    print(title, length)

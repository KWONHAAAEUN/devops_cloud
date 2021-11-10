import pandas as pd
from pprint import pprint  # pprint를 이용해서 출력하면 print가 정렬된다
from typing import List  # 타입 힌팅을 사용한다

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

""" 방탄소년단의 곡명 문자열로 구성된 리스트를 만들어 출력하기 """
# title_list: List[str] = []  # title_list은 문자열로만 구성을 할 것이다, 코드 가독성 측면에서 좋음
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단":
#         # title_list.append(song_dict["title"]) 아래 2줄 코드와 같음
#         title: str = song_dict["title"]
#         title_list.append(title)
# 단순하게 title_list에 =를 사용해서 넣으면 리스트가 아니게 된다
# 파이썬에서는 리스트끼리 합칠 때 뒤에 값을 넣어주는 append를 필수적으로 사용해야함
new_song_list: List[dict] = []
for song_dict in song_list:
    artist: str = song_dict["artist"]  # 현재와 아래줄은 필터가 되는 부분이 된다
    if artist == "방탄소년단":
        new_song_list.append(song_dict)  # 전체 곡 정보를 다 넣는것

pprint(new_song_list)

""" 필터를 이용한 방법 """


def check_bts_song(song_dict):  # bts 노래라면 True 아니라면 False를 리턴
    """bts 노래라면 True를 반환합니다"""
    artist: str = song_dict["artist"]
    return artist == "방탄소년단"


# 필터의 개념은 이용하지만 직접적으로 필터는 쓰지 않은 방법
# new_song_list: List[dict]=[]
# for song_dict in song_list:
#     if check_bts_song(song_dict):
#         new_song_list.append(song_dict)
# pprint(new_song_list)

# 아래 코드는 33~36를 필터로 줄인것
new_song_list = list(filter(check_bts_song, song_list))
pprint(new_song_list)
# 단순히 print만 한다고 하면
for song_dict in filter(check_bts_song, song_list):
    print("{title}{artist}{like}".format(**song_dict))

"""곡명에 사랑이 포함된 곡명만 출력하기"""

title_list: List[str] = []
for song_dict in song_list:
    title: str = song_dict["title"]
    if "사랑" in title:
        title_list.append(title)

print(title_list)

""" 필터를 이용한 방법 """


def check_contains_love(song_dict):
    title: str = song_dict["title"]
    return "사랑" in title


for song_dict in filter(check_contains_love, song_list):
    # print(song_dict)
    print("{rank}{title}".format(**song_dict))

"""좋아요 수가 200,000이상인 곡들의 곡명 리스트를 만들어 출력하기"""
title_list: List[str] = []
for song_dict in song_list:
    title: str = song_dict["title"]
    like: int = song_dict["like"]
    if like >= 200_000:
        title_list.append(title)

print(title_list)

"""필터를 이용한 방법"""


def check_above_200000(song_dict):
    like: int = song_dict["like"]
    return like >= 200_000


for song_dict in filter(check_above_200000, song_list):
    print("{title}-{like}".format(**song_dict))

"""멜론 top100리스트에서 곡명 단어수 출력->곡명,단어수 리스트를 만들어보기"""
for song_dict in song_list:
    title: str = song_dict["title"]
    title_length = len(title)
    print(title, title_length)

"""맵 사용한 버전"""


def get_title_for_song(song_dict):
    return song_dict["title"]


# 변환을 담당하는 함수
# for song_dict in song_list:
#     print(get_title_for_song(song_dict))

# 101,102와 같은 부분
# title_list=list(map(get_title_for_song,song_list))
# print(title_list)

for title in map(get_title_for_song, song_list):
    print(f"{title}-{len(title)}")

"""다른 방법"""


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    return [title, len(title)]


# return 값에 값을 2개 지정해줬기 때문에 for문에서도 2개를 받아야한다
for title, length in map(get_title_and_length_for_song, song_list):
    print(title, length)

"""응용"""
# 방탄소년단의 노래에 대해서만, 곡명과 글자수를 출력
bts_list = []
for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        title: str = song_dict["title"]
        bts_list.append([title, len(title)])

for title, length in bts_list:
    print(title, length)

"""필터/맵 버전"""


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

"""문제"""
# artist 글자수가 3글자 이상인 곡에 대해서 좋아요 수와 제목 글자수의 곱을 출력
# 아트스트 3글자 이상 좋아요*제목글자수 곱 출력
"""for/if 구현"""
new_song_list: List[dict] = []
value = []
for song_dict in song_list:
    if len(song_dict["artist"]) >= 3:
        value: int = song_dict["like"] * len(song_dict["title"])
        new_song_list.append(
            dict(song_dict, value=value)
        )  # 사전에 복제본을 만드는 것 b라는 키를 추가하면서
        # 위 코드는 아래 사전과 같은 코드이다
        # new_song_list.append({
        #     "title":song_dict["title"],
        #     "artist":song_dict["artist"],
        #     "like":song_dict["like"],
        #     "value":value,
        # })

for song_dict in new_song_list:
    print("{title}-{artist}-{value}".format(**song_dict))

"""필터/맵 구현"""


def check_bts_song(song_dict):
    return len(song_dict["artist"]) >= 3


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    like: int = song_dict["like"]
    return like * len(title)


for idx, like_length in enumerate(  # enumerate로 인덱스값을 포함
    map(get_title_and_length_for_song, filter(check_bts_song, song_list))
):
    # filter 이용해 아티스트 3글자 이상을 가져오고 map 으로 좋아요*타이틀곡 글자수를 계산
    print(
        "{title} {artist} {like_length}".format(
            like_length=like_length, **song_list[idx]
        )
    )

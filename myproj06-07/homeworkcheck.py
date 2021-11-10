from collections import defaultdict
from collections import Counter
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

"""멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 리스트 만들어 출력
-단어수가 많으면 우선순위""" """아래 좋아요 수로 top10"""


def pick_like_value(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, key=pick_like_value, reverse=True)
# 214줄 범위를 아래 코드로 지정하고 in 뒤에 top10_song_list를 넣을 수 있다
# top10_song_list=sorted_song_list[:10]

for song_dict in sorted_song_list[0:10]:
    # 210 줄을 지우고 in 뒤에 아래 코드를 넣는 것으로 대체 가능
    # sorted(song_list, key=pick_like_value,reverse=True)[:10]:
    print("{like} {title}".format(**song_dict))

"""곡명 단어 수로 top10"""


def pick_word_count_for_title(song_dict):
    title: str = song_dict["title"]
    word_list = title.split()
    return len(word_list)


sorted_song_list = sorted(song_list, key=pick_word_count_for_title, reverse=True)
top10_song_list = sorted_song_list[:10]

for song_dict in top10_song_list:

    print("{like} {title}".format(**song_dict))

"""max, min 함수"""
"""좋아요 수가 가장 많고 적은 곡은?"""


def peek_like_for_song(song_dict):
    return song_dict["like"]


# 에러처리 1번 (song_list가 비었을 때)
song_dict = max(
    song_list, key=peek_like_for_song, default=None
)  # song_dict이 비었으면 default 값을 내보냄
if song_dict == None:
    print("노래 제목이 비었습니다")
else:
    print(song_dict)
# 에러처리 2번
try:  # 에러가 발생하게 두고 그 에러를 잡는다-파이썬에서 주로 사용하는 방법
    song_dict = max(song_list, key=peek_like_for_song)
except ValueError:
    print("노래 제목이 비었습니다")
else:
    print(song_dict)
# 에러처리 3번
if song_list:  # 에러를 미리 검사-보통 파이썬에서 사용하기보다는 c에서 주로 사용하는 방법
    song_dict = max(song_list, key=peek_like_for_song)
    print(song_dict)
else:
    print("노래목록이 비었습니다")

"""리스트에 랭크된 가수는 총 몇 팀인가요?(중복 제가한 가수명 리스트의 크기)"""
# 방법 1
artist_list = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist not in artist_list:
        artist_list.append(artist)
print(len(artist_list))

# 방법 2
artist_set = set()
for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_set.add(artist)  # 집합에 추가하는 것은 add 순서가 없기 때문
print(len(artist_set))

# 방법 3
# for song_dict in song_list:
#     song_dict["artist"]
# 위와 아래 2줄 코드는 같음
# [song_dict["artist"]
# for song_dict in song_list]

artist_set = set([song_dict["artist"] for song_dict in song_list])  # set이 중복을 제거해줌
print(len(artist_set))

# 방법 4
artist_set = {song_dict["artist"] for song_dict in song_list}
print(len(artist_set))

"""2곡이상 랭크된 가수는 몇 팀인가요?"""

artist_list = [song_dict["artist"] for song_dict in song_list]

# 방법 1
song_count_dict = {}  # key: artist, value: song count
for artist in artist_list:
    if artist not in song_count_dict:
        song_count_dict[artist] = 0
    else:
        song_count_dict[artist] += 1

pprint(song_count_dict)

# 방법 2
# keyerror가 발생할 때, key error를 숨기고, 지정된 디폴트 값으로 key/value을 저장합니다
song_count_dict = defaultdict(int)
for artist in artist_list:
    song_count_dict[artist] += 1

pprint(song_count_dict)

# 카운터 이용 방법 1
song_count_dict = Counter(artist_list)

artist_count_above_2 = 0
for song_count in song_count_dict.values():
    if song_count >= 2:
        artist_count_above_2 += 1
print(artist_count_above_2)

# 방법 2
song_count_dict = Counter(artist_list)


def check_above_1(song_count):
    return song_count > 1


print(len(list(filter(check_above_1, song_count_dict.values()))))

"""방탄소년단의 좋아요 총 합은?"""
# List Comprehension with if statement
like_sum_for_bts = sum(
    [song_dict["like"] for song_dict in song_list if song_dict["artist"] == "방탄소년단"]
)
print(like_sum_for_bts)

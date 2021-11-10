"""코드를 작성하면서 느낀점은 제가 print에 주로 집중하는 것을 알 수 있었습니다
그렇게 작성하다보니 코드 자체가 깔끔한 느낌이 아닌 결과로만 나올 수 있게 만들었는데 
연습을 통해 개선해 나가도록 노력하겠습니다"""

import pandas as pd
from collections import Counter

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 01. 멜론 top100 리스트에서 '곡명'단어 수 출력
def map_fn1(song_dict):
    print(song_dict["title"], "의 단어수는", len(song_dict["title"].split(" ")))
    return ""


for song_dict in map(map_fn1, song_list):
    print(song_dict)

# 02. 멜론 top100 리스트에서 '곡명'단어 수 top10출력
"""곡명을 출력하기 위해서 정렬을 진행한 title을 뽑고 싶어 새로운 def로 또 다시 정렬을 하고..등등 만들어 봤었습니다
그 과정에서 잘 이뤄지지 않아 일단은 단어 수만 출력하도록 만들었습니다"""
new_song_list = []

def map_fn2(song_dict):
    return len(song_dict["title"].split(" "))


new_song_list = list(map(map_fn2, song_list))
new_song_list = sorted(new_song_list, reverse=True)

print("곡명 단어수 top10")

for song_dict in new_song_list[:10]:
    print("띠리링 노래 단어 수:",song_dict)

# 03. 멜론 top100리스트에서 "좋아요"수가 가장 많은 곡과 작은 곡

a = []
b = []
c = []


def max_fn1(song_dict):
    return song_dict["like"]


a = list(map(max_fn1, song_list))


def max_fn2(song_dict):
    if song_dict["like"] == max(a):
        b.append(song_dict["title"])
    return b


def max_fn3(song_dict):
    if song_dict["like"] == min(a):
        c.append(song_dict["title"])
    return c


b = list(map(max_fn2, song_list))
c = list(map(max_fn3, song_list))

print("좋아요 수가 가장 많은 곡은", b[0], max(a))
print("좋아요 수가 가장 많은 곡은", c[0], min(a))

# 04. 멜론 top100리스트에서 "곡명"단어수가 가장 많은 곡과 작은 곡

def max_fn4(song_dict):
    title = len(song_dict["title"].split(" "))
    return title


max_title = max(song_list, key=max_fn4)
min_title = min(song_list, key=max_fn4)
max_word = len(max_title["title"].split(" "))
min_word = len(min_title["title"].split(" "))

print("곡명 단어수가 가장 많은 곡 : {title}".format(**max_title), max_word)
print("곡명 단어수가 가장 적은 곡 : {title}".format(**min_title), min_word)

# 05. 멜론 top100리스트에서 "곡명"글자수가 가장 많은 곡과 작은 곡

def max_fn5(song_dict):
    title = len(song_dict["title"])
    return title


max_title1 = max(song_list, key=max_fn5)
min_title1 = min(song_list, key=max_fn5)
max_word1 = len(max_title1["title"])
min_word1 = len(min_title1["title"])

print("곡명 글자수가 가장 많은 곡 : {title}".format(**max_title1), max_word1)
print("곡명 글자수가 가장 적은 곡 : {title}".format(**min_title1), min_word1)

# 06. 멜론 top100리스트에서 랭크된 가수는 총 몇팀인가요?

top100_artist = []

def rank_list(song_dict):
    artist = song_dict["artist"]
    return artist

top100_artist = list(set(map(rank_list, song_list)))

print(f"top100에 랭크된 가수 목록은 : {top100_artist}", "총", len(top100_artist), "팀입니다")

# 07. 멜론 top100리스트에서 2곡 이상 랭크된 가수는 몇 팀인가요?

top100_artist1 = []
result = []

def rank_list(song_dict):
    artist = song_dict["artist"]
    return artist


top100_artist1 = list(map(rank_list, song_list))  # 가수 이름 총 목록

result = Counter(top100_artist1)
rank_sum = 0
print("2곡 이상 랭크된 가수는")
for artist1, value in result.items():
    if value >= 2:
        print(artist1)
        rank_sum += 1
print("총 ", rank_sum)


# 08. 멜론 top100리스트에서 방탄소년단의 좋아요 총 합은?
def filter_fn8(song_dict):
    return song_dict["artist"] == "방탄소년단"


bts_sum = 0
for song_dict in filter(filter_fn8, song_list):
    bts_sum += song_dict["like"]
print(f"방탄소년단의 좋아요 총 합은: {bts_sum}")

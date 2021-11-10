import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 02. 멜론 top100 리스트에서 '곡명'단어 수 top10출력
"""곡명을 출력하기 위해서 정렬을 진행한 title을 뽑고 싶어 새로운 def로 또 다시 정렬을 하고..등등 만들어 봤었습니다
그 과정에서 잘 이뤄지지 않아 일단은 단어 수만 출력하도록 만들었습니다"""

# print('"곡명" 단어수로 TOP10 곡명 출력')


# def map_fn2(s):
#     return s["title"]


# a = list(map(map_fn2, song_list))
# # print(a)


# def sort_fn2(a):
#     return len(a.split())


# sorted_song_list = list(sorted(a, reverse=True, key=sort_fn2))

# for sl in sorted_song_list[:10]:
#     print(sl)


new_song_list = []


def map_fn2(song_dict):
    return len(song_dict["title"].split(" "))


a = list(map(map_fn2, song_list))
new_song_list = list(map(map_fn2, song_list))
new_song_list = sorted(new_song_list, reverse=True)

print("top곡수")
for song_dict in new_song_list[:10]:
    print("띠리링 곡수", song_dict)

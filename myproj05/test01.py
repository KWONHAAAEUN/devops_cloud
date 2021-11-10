import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


# 정렬을 하려면 각 값들끼리 대소비교가 가능해야한다
# for song_dict in sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수):
#     print("[{like}]{title}{artist}".format(**song_dict))

sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)

for song_dict in sorted_song_list[:10]:
    print("[{like}]{title}{artist}".format(**song_dict))

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 02. 멜론 top100 리스트에서 '곡명'단어 수 top10출력


# def s(song_dict):
#     return song_dict["title"]

# sorted_song_list = sorted(len(song_list["title"].split(" ")), key=s)

# for s in sorted_song_list[:10]:
#     print(f"곡명 단어수 top10{sorted_song_list}")

# sorted_song_list = []


# def map_fn1(song_dict):
#     sorted_song_list = sorted(len(song_dict["title"].split(" ")))
#     return "top10의 단어수는", song_dict["title"], sorted_song_list


# def s(song_dict):
#     a = len(song_dict["title"].split(" "))
#     return a.sort(reverse=False)  # title단어 수를 계산하는 부분


# for song_dict in map(s, song_list):
#     print(song_dict["title"])


# def map_fn2(song_dict):
#     return len(song_dict["title"].split(" "))


# sorted_song_list = []
# sorted_song_list = sorted(song_list, reverse=False, key=map_fn2)

# for song_dict in map(map_fn2, sorted_song_list):
#     print("단어수 top10", song_dict["title"], "의 곡 단어 수는", sorted_song_list[:10])

# a = []


# def map_fn2(song_dict):
#     return len(song_dict["title"].split(" "))

# for song_dict in map(map_fn2, song_list):
#     a = song_dict


# sorted_song_list = list(sorted(a, reverse=True, key=map_fn2))

# for s in sorted_song_list[:10]:
#     print(s)

new_song_list = []


def map_fn2(song_dict):
    return len(song_dict["title"].split(" "))


new_song_list = list(map(map_fn2, song_list))
new_song_list = sorted(new_song_list, reverse=True)


for song_dict in new_song_list[:10]:
    print(f"top10 단어 수: {new_song_list}")

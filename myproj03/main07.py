import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 가수별 곡 수
top100_artist = []
result = []

for song in song_list:
    top100_artist.append(song["artist"])

# 리스트 중복 제거
for value in top100_artist:
    if value not in result:
        result.append(value)

for value in result:
    count_song = top100_artist.count(value)
    print(f"{value}가수의 곡 수는{count_song}개 입니다")

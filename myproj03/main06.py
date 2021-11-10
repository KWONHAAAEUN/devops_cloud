import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 01.방탄소년단 곡명 출력
for song in song_list:
    if song["artist"] == "방탄소년단":
        print(song["title"])


# 02.곡명에 "가을"이 들어가는 것만
for song in song_list:
    if "가을" in song["title"]:
        print(song["title"])


# 03.좋아요가 200000개가 넘는 곡 수는?
count_like = 0
for song in song_list:
    if int(song["like"]) > 200000:
        count_like += 1
print(f"좋아요가 200,000이 넘는 곡 수는 {count_like}개")

# 04.가수별 곡 수
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

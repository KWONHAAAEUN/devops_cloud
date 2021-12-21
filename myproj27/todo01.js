// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`

const { melon_data: song_array } = require("./melon_data");

song_array.sort((song_array1, song_array2) => song_array2.like - song_array1.like);

for (const song of song_array) {
    console.log("[", song.like, "]", song.title);
}
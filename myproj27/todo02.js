// TOOD: #2 방탄소년단의 곡명만 출력
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용

const { melon_data: song_array } = require("./melon_data");

// element는 순회하는 배열의 인자값
// index는 그 인자값의 인덱스
// array는 현재 배열
var result = song_array.filter(function (element) {
    return element.artist == "방탄소년단";
});

for (const song of result) {
    console.log(song.artist, song.title, song.like);
}
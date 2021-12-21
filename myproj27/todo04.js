// TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

// element는 순회하는 배열의 인자값
// index는 그 인자값의 인덱스
// array는 현재 배열
var result = song_array.filter(function (element) {
    return element.like >= 200000;
});

for (const song of result) {
    console.log("[", song.like, "]", song.title, song.artist);
}
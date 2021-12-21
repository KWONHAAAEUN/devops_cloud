// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

// element는 순회하는 배열의 인자값
// index는 그 인자값의 인덱스
// array는 현재 배열
var result = song_array.filter(function (element) {
    return element.like >= 200000;
});

result.sort(function (result1, result2) {
    return result1.title < result2.title ? -1 : result1.name > result2.name ? 1 : 0;
});

for (const song of result) {
    console.log("[", song.like, "]", song.title, song.artist);
}
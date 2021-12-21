// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.

const { melon_data: song_array } = require("./melon_data");

var result = song_array.filter(function (element) {
    return element.artist == "방탄소년단"
});

var song = result.map(function (element) {
    return element.like
});

// accumulator 이전 el에 대한 리턴값
// currentValue 현재 처리 중인 배열 el
// 0은 initialValue로 초기 accumulator의 값 지정
const sum = song.reduce(function (accumulator, currentValue) {
    return accumulator + currentValue;
}, 0);

console.log('방탄소년단의 좋아요 총 합은:', sum)

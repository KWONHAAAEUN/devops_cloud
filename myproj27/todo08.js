// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const { melon_data: song_array } = require("./melon_data");

var song = song_array.map(function (element) {
    return element.title
});

const result = song.filter(word => word.includes('사랑'))

console.log(result)
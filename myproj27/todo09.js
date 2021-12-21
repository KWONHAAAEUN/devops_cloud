// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

const { melon_data: song_array } = require("./melon_data");

var result = song_array.filter(function (element) {
    return element.like >= 200000;
});

var song = result.map(function (element) {
    return element.title
});

console.log(song)

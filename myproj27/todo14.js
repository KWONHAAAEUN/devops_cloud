// TODO: #14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은?
// Array의 filter와 reduce를 활용해주세요.

const { melon_data: song_array } = require("./melon_data");

var result = song_array.filter(function (element) {
    return element.artist == "방탄소년단"
});

var song = result.map(function (element) {
    return element.like
});

var min = song.reduce((previous, current) => { return previous > current ? current : previous; });

var low_song = result.filter(function (element) {
    return element.like == min
});

var low_title = low_song.map(function (element) {
    return element.title
});

console.log('방탄소년단 곡 중에 좋아요 수가 가장 적은 곡명은', low_title)
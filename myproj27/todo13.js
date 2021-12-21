// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.

const { melon_data: song_array } = require("./melon_data");

var result = song_array.filter(function (element) {
    return element.artist == "방탄소년단"
});

var song = result.map(function (element) {
    return element.like
});

var max = song.reduce((previous, current) => { return previous > current ? previous : current; });

var high_song = result.filter(function (element) {
    return element.like == max
});

var high_title = high_song.map(function (element) {
    return element.title
});

console.log('방탄소년단 곡 중에 좋아요 수가 가장 큰 곡명은', high_title)
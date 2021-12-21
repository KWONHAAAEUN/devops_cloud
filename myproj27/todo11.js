// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용

const { melon_data: song_array } = require("./melon_data");

var song = song_array.map(function (element) {
    return element.artist
});

const set = new Set(song);

console.log(set.size);
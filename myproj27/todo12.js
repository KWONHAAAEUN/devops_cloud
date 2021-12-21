// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set

const { melon_data: song_array } = require("./melon_data");

const singer = song_array.map(function (song) {
    return song.artist
})

function getCount(array) { return array.reduce((pv, cv) => { pv[cv] = (pv[cv] || 0) + 1; return pv; }, {}); }
myset = getCount(singer)

song_list = (Object.values(myset));

song_list = song_list.filter(function (item) {
    return item !== 1;
});

console.log(song_list.length)
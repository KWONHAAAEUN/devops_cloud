// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

const { melon_data: song_array } = require("./melon_data");

var song = song_array.map(function (element) {
    let obj2 = element.title.split(" ").length
    return element.title.concat('/', obj2);
});

// 템플릿 리터럴도 생각해보기~!
console.log(song)

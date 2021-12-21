const { melon_data: song_array } = require("./melon_data");

// TODO: list 오름차순으로 정렬

// song_array.sort((song_array1, song_array2) => song_array1.like - song_array2.like);

// const song = song_array.sort(
//     (song_array1, song_array2) => {
//         return song_array1.like - song_array2.like;
//     }
// );

for (const song of song_array) {
    song.sort((song1, song2) => song1.like - song2.like);
    console.log(song.like, song.title);
}
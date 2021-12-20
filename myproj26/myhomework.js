const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];

function shuffleArray(animal_names) {
    animal_names.sort(() => Math.random() - 0.5);
}

shuffleArray(animal_names);

begin_time = Math.floor(+ new Date() / 1000);

let ok_counter = 0;

const random_name = animal_names.slice(0, 5);

for (i = 0; i < random_name.length; i++) {
    console.log(random_name[i]);
    const { question } = require("readline-sync");
    const name = question(">>> ")
    if (name == random_name[i]) {
        ok_counter += 1;
        console.log("정확합니다")
    } else {
        console.log("오타가 있어요")
    }
}

end_time = Math.floor(+ new Date() / 1000);
now_time = end_time - begin_time
console.log(`${ok_counter}번 성공하셨습니다`)
console.log(`총${now_time}초가 걸리셨어요`)

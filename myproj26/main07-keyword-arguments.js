
function mysum3(x, y, z) {
    return x + y * 10 + z * 100;
}

// mysum3(1,2,3)

// js에는 없는 문법
//mysum3(x=1,y=2,z=3)

// 파이썬의 keywird arguments와
// 비슷하게 사용하는 코드

const { x, y, z } = { x: 1, y: 2, z: 3 }

function mysum3(x, y, z) {
    return x + y * 10 + z * 100;
}

mysum3({ x: 1, y: 2, z: 3 });


const people = [
    { name: 'Tom', age: 10, region: 'Seoul' },
    { name: 'Steve', age: 12, region: 'Pusan' }
];

// for (const person of people) {
//     console.log(person.name, person.age);
// }

for (const { name, age } of people) {
    console.log(name, age)
}
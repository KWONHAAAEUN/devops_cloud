// function base_10(fn) {
//     function wrap(x, y) {
//         return fn(x, y) + 10;
//     }
//     return wrap;
// }
// function mysum(x, y) {
//     return x + y;
// }

// mysum = base_10(base_10(mysum));

// console.log(mysum(1, 2));


// arrow function 버전으로 바꾸기
const base_10 = (fn) => (x, y) => fn(x, y) + 10;
    // const wrap=(x, y) => fn(x, y) + 10;
    // return wrap;

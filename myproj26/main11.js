// 1번 방법
// const fs = require("fs");

// fs.readdir("c:/Dev", function (err, files) {
//     if (err) {
//         console.error(err);
//     }
//     else {
//         console.log(files);
//     }
// });

// 2번 방법 Promise 정상처리와 에러처리 나눠서 1번은 if문으로 한 경우
// const fs = require("fs");
// const fsPromises = fs.promises;

// fsPromises.readdir("c:/Dev")
//     .then(files => console.log("loaded:", files))
//     .catch(error => console.error(error));

// console.log("ENDED");

// 3번 방법 await 사용
const fs = require("fs");
const fsPromises = fs.promises;

// await는 promise 문법에 대한 축약
// await는 async 안에서만 사용 가능
async function main() {
    try {
        const files = await fsPromises.readdir("c:/Dev");
        console.log("loded:", files);
    }
    catch (error) {
        console.error(error);
    }
}

main();
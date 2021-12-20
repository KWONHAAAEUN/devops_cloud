const mysum = () => {
    x, y
    return
}

const mysum2 = (x, y) => { x, y };
console.log(mysum2(1, 2));

const mysum3 = (x, y) => {
    return { x, y };
};
console.log(mysum3(1, 2));

// 내가 반환할 x,y가 객체로 되면 좋겠어!! ()로 묶어주자: 2번의 해결법
const mysum4 = (x, y) => ({ x, y });
console.log(mysum4(1, 2));

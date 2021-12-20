
// Array
// const [name] = ["Tom", 10, "Seoul"];
// // Tom만 name에 저장

// const [, age,] = ["Tom", 10, "Seoul"];

// // heigth는 undefined
// const [name, age, region, heigth] = ["Tom", 10, "Seoul"];

// // 값 할당에 실패했을 때 적용되는 디폴트 값
// const [name, age, region, heigth = 140] = ["Tom", 10, "Seoul"];

// 디폴트 값을 함수 호출로 지정
function get_default_height() {
    console.log("get_default_height 함수를 호출했습니다");
    return 140;
}
const [name, age, region, heigth = get_default_height()] = ["Tom", 10, "Seoul"];
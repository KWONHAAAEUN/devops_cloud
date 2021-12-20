
const get_default_value = () => {
    console.log("get_default_value() 함수 호출")
    return 10;
}

// const get_default_value = () => 10;
//아래 두줄 위와 같은 코드
// const get_default_value=()=>{
//     return 10;
// }

// function get_default_value(){
//     return 10;

// }
function hello(name, age = get_default_value()) {
    console.log(`안녕 나는 ${name}이야 ${age}살이지`);
}

hello("Tom");
hello("Steve", 14);
hello("John");
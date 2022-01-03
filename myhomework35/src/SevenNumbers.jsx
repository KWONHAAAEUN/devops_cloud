import { useReducer } from 'react';
//버튼 3개
//  - GENERATE_NUMBERS : 새로운 numbers를 랜덤하게 뽑아서 numbers에 적용
//  - SHUFFLE_NUMBERS : 기존 numbers를 순서를 랜덤하게 섞습니다. 순서만 바꿀 뿐.
//  - SHUFFLE_COLORS : 기존 colors의 순서를 랜덤하게 섞습니다. 순서만 바꿀 뿐.
function reducer(prevState, action) {
  const { type } = action;
  if (type === 'GENERATE_NUMBERS') {
    let randomnumber = [];
    for (var i = 1; i <= 7; i += 1) {
      let lottonum = Math.floor(Math.random() * 45) + 1;
      if (randomnumber.indexOf(lottonum) === -1) {
        randomnumber.push(lottonum);
      } else {
        i--;
      }
    }
    randomnumber.sort(
      (randomnumber1, randomnumber2) => randomnumber1 - randomnumber2,
    );
    return { ...prevState, numbers: randomnumber };
  } else if (type === 'SHUFFLE_NUMBERS') {
    let shufflenumbers = [];
    shufflenumbers = prevState.numbers.sort(() => Math.random() - 0.5);
    return { ...prevState, numbers: shufflenumbers };
  } else if (type === 'SHUFFLE_COLORS') {
    let shufflencolors = [];
    shufflencolors = prevState.colors.sort(() => Math.random() - 0.5);
    return { ...prevState, colors: shufflencolors };
  }
}

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
    numbers: [0, 0, 0, 0, 0, 0, 0],
    colors: [
      '#1B62BF',
      '#1755A6',
      '#37A647',
      '#F29F05',
      '#F23838',
      'purple',
      'pink',
    ],
  });

  return (
    <div>
      <h2>7개의 숫자</h2>
      {state.numbers.map((numbers, index) => {
        return (
          <div
            style={{ ...defaultStyle, backgroundColor: state.colors[index] }}
          >
            {numbers}
          </div>
        );
      })}
      <hr />
      <button onClick={() => dispatch({ type: 'GENERATE_NUMBERS' })}>
        새로운 수 뽑기
      </button>
      <button onClick={() => dispatch({ type: 'SHUFFLE_NUMBERS' })}>
        랜덤 섞기
      </button>
      <button onClick={() => dispatch({ type: 'SHUFFLE_COLORS' })}>
        색 섞기
      </button>
    </div>
  );
}
const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
  margin: '1rem',
};
export default SevenNumbers;

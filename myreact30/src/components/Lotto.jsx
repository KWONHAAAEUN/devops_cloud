// 1) 로또 번호 예지 컴포넌트 (App과는 별도의 컴포넌트)
//  - <button>예지</button> 클릭하면
//  - 랜덤하게 숫자 7개를 뽑아서
//  - 오름차순으로 정렬해서
//  - 숫자를 보여줍니다.
//  - 각 숫자는 원 안에 스타일링되어 표현되어야 합니다.

import React, { memo } from 'react';
function Lotto({ color }) {
  let number = [];
  for (var i = 1; i <= 7; i += 1) {
    let lottonum = Math.floor(Math.random() * 44) + 1;
    if (number.indexOf(lottonum) === -1) {
      number.push(lottonum);
    } else {
      i--;
    }
  }

  number.sort((number1, number2) => number1 - number2);

  // <div class="num_box">
  //   <span class="num ball"></span>
  // </div>;

  const Ball = memo(({ number }) => {
    let background;
    if (number < 10) {
      background = 'red';
    } else if (number < 20) {
      background = 'orange';
    } else if (number < 30) {
      background = 'yellow';
    } else if (number < 40) {
      background = 'blue';
    } else {
      background = 'green';
    }

  return (
    <div className="Lotto" style={{ ...style, backgroundColor: color }}>
      {number}
    </div>
  );
}

const style = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  margin: '1rem',
  userSelect: 'none',
};

export default Lotto;

//.toLocaleString()

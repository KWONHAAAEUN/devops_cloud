// import Ball from "../components/Ball"

// function PageLotto() {
//     let number = [];
//     for (var i = 1; i <= 7; i += 1) {
//         let lottonum = Math.floor(Math.random() * 44) + 1;
//         if (number.indexOf(lottonum) === -1) {
//         number.push(lottonum);
//         } else {
//         i--;
//         }
//     }

//     number.sort((number1, number2) => number1 - number2);

//     // <div class="num_box">
//     //   <span class="num ball"></span>
//     // </div>;

//     return (
//         <div className="Lotto" style={{ ...style, backgroundColor: color }}>
//         {number}
//         </div>
//     );
//     }

// export default PageLotto;

import Ball from '../components/Ball';
import React, { Component } from 'react';

function getWinNumbers() {
  // 1~ 45가 들어있는 배열 생성
  const candidate = Array(45)
    .fill()
    .map((v, i) => i + 1);
  const shuffle = [];
  // 1~45를 랜덤하게 섞기
  while (candidate.length > 0) {
    shuffle.push(
      candidate.splice(Math.floor(Math.random() * candidate.length), 1)[0],
    );
  }
  // shuffle의 마지막 수를 보너스 숫자로
  const bonusNumber = shuffle[shuffle.length - 1];
  // shuffle의 0~5번째 수를 오름차순 정렬하여 당첨 숫자로
  const winNumbers = shuffle.splice(0, 6).sort((p, c) => p - c);
  return [...winNumbers, bonusNumber];
}

class PageLotto extends Component {
  state = {
    winNumbers: getWinNumbers(), // 당첨 숫자
    winBalls: [],
    bonus: null, // 보너스공
    redo: false,
  };

  render() {
    const { winBalls, bonus, redo } = this.state;
    return (
      <>
        <div>당첨 숫자</div>
        <div id="결과창">
          {winBalls.map((v) => (
            <Ball key={v} number={v} />
          ))}
        </div>
        <div>보너스</div>
        {bonus && <Ball number={bonus} />}
        {redo && <button onClick={this.onClickRedo}>한 번 더!</button>}
      </>
    );
  }
}

export default PageLotto;

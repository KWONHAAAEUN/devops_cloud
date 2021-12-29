import { useState } from "react";

function makeLottoNumbers() {
  let lnumber = [];
  for (var i = 1; i <= 7; i += 1) {
    let lottonum = Math.floor(Math.random() * 45) + 1;
    if (lnumber.indexOf(lottonum) === -1) {
      // 인덱스가 존재하지 않으면 -1을 반환
      lnumber.push(lottonum);
    } else {
      i--; // 중복 값이 나타났을 때 i를 감소시켜주기 위해
    }
  }
  return lnumber.sort((lnumber1, lnumber2) => lnumber1 - lnumber2);
}

function PageLotto() {
  const [numbers, setNumbers] = useState([]);

  const handleClick = () => {
    setNumbers(makeLottoNumbers());
  };

  // const Ball = memo(({ number }) => {
  //   let background;
  //   if (number < 10) {
  //     background = 'red';
  //   } else if (number < 20) {
  //     background = 'orange';
  //   } else if (number < 30) {
  //     background = 'yellow';
  //   } else if (number < 40) {
  //     background = 'blue';
  //   } else {
  //     background = 'green';
  // }

  return (
    <div>
      <h2>Lotto</h2>
      {numbers.map((number) => {
        return <div style={style}>{number}</div>;
      })}
      <button onClick={handleClick}>예지</button>
    </div>
  );
}

const style = {
  width: "50px",
  height: "50px",
  display: "inline-block",
  textAlign: "center",
  margin: "1rem",
  fontSize: "2rem",
  borderRadius: "50px",
  backgroundColor: "yellow",
};

export default PageLotto;

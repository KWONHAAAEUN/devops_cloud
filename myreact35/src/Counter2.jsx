import { useState } from 'react';

// { type: "PLUS", amount: 1 }
// { type: "MINUS", amount: 1 }
function reducer(action, prevState) {
  // 순수함수로서 구현이 되어야한다
  // 같은 값의 인자가 주어지면, 항상 같은 값을 리턴해야 하고
  // 인자 외의 다른 어떤 값, 어떤 통신을 해서도 안된다.=>순수함수이기 때문
  const { type, amount } = action;
  if (type === 'PLUS') {
    return prevState + amount;
  } else if (type === 'MINUS') {
    return prevState - amount;
  }
  return prevState;
}

function reducer_color(action, prevState) {
  const { type, color } = action;
  if (type === 'CHANGE_COLOR') {
    return color;
  }
  return prevState;
}

function Counter2() {
  // TODO: color와 value
  const [value, setValue] = useState(0);
  const [color, setColor] = useState('red');

  const handlePlus = () => {
    const action = { type: 'PLUS', amount: 1 };
    setValue((prevValue) => {
      // reducer 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
      return reducer(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: 'MINUS', amount: 1 };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handleChange1 = () => {
    const action = { type: 'CHANGE_COLOR', color: 'green' };
    setColor((prevValue) => {
      return reducer_color(action, prevValue);
    });
  };
  const handleChange2 = () => {
    const action = { type: 'CHANGE_COLOR', color: 'blue' };
    setColor((prevValue) => {
      return reducer_color(action, prevValue);
    });
  };
  const handleChange3 = () => {
    const action = { type: 'CHANGE_COLOR', color: 'red' };
    setColor((prevValue) => {
      return reducer_color(action, prevValue);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
      <button onClick={handleChange1}>green</button>
      <button onClick={handleChange2}>blue</button>
      <button onClick={handleChange3}>red</button>
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
};

export default Counter2;

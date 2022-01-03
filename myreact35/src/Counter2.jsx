import { useState } from 'react';

// { type: "PLUS", amount: 1 }
// { type: "MINUS", amount: 1 }
function dispatch(action, prevState) {
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

function Counter2() {
  // TODO: color와 value
  const [value, setValue] = useState(0);

  const handlePlus = () => {
    const action = { type: 'PLUS', amount: 1 };
    setValue((prevValue) => {
      // dispatch 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
      return dispatch(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: 'MINUS', amount: 1 };
    setValue((prevValue) => {
      return dispatch(action, prevValue);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>
      {value}
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
    </div>
  );
}

export default Counter2;

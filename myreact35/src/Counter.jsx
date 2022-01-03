import { useState } from 'react';

function Counter({ initialValue }) {
  // 상탯값 정의
  const [value, setValue] = useState(initialValue);

  // 상탯값 변경하는 함수들
  const handlePlus = () => {
    // setValue(value + 1); // 비동기 세상
    // setValue(value + 2);

    // setValue((prevValue) => prevValue + 1);
    // setValue((prevValue) => prevValue + 1);
    setValue((prevValue) => prevValue + 1);
  };

  const handleMinus = () => {
    setValue((prevValue) => prevValue - 1);
  };
  // 보여지는 것들을 정의
  return (
    <div>
      <h2>Counter</h2>
      {value}
      <hr />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
    </div>
  );
}

export default Counter;

import { useState } from 'react';

function reducer(action, prevState) {
  const { type, amount, color } = action;
  if (type === 'PLUS') {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === 'MINUS') {
    return { ...prevState, value: prevState.value - amount };
  } else if (type === 'Color') {
    return { ...prevState, color };
  }
  return prevState;
}

function Counter3() {
  // const [value, setValue] = useState(0);
  // const [color, setColor] = useState('red');
  const [state, setState] = useState({ value: 0, color: 'red' });
  const { value, color } = state;

  const handlePlus = () => {
    // setValue(value + 1);
    // setValue((prevValue) => prevValue + 1);
    const action = { type: 'PLUS', amount: 1 };
    setState((prevState) => {
      // ...prevState,
      // value: prevState.value + 1,
      return reducer(action, prevState);
    });
  };

  const handleMinus = () => {
    // setValue(value - 1);
    // setValue((prevValue) => prevValue - 1);
    const action = { type: 'MINUS', amount: 1 };
    setState((prevState) => {
      // ...prevState,
      // value: prevState.value - 1,
      return reducer(action, prevState);
    });
  };

  const handleChangeColor1 = () => {
    // setColor('green');
    // setColor(() => 'green');
    const action = { type: 'Color', color: 'green' };
    setState((prevState) => {
      // ...prevState,
      // color: 'green',
      return reducer(action, prevState);
    });
  };

  const handleChangeColor2 = () => {
    // setColor('blue');
    // setColor(() => 'blue');
    const action = { type: 'Color', color: 'blue' };
    setState((prevState) => {
      // ...prevState,
      // color: 'blue',
      return reducer(action, prevState);
    });
  };

  const handleChangeColor3 = () => {
    // setColor('red');
    // setColor(() => 'red');
    const action = { type: 'Color', color: 'red' };
    setState((prevState) => {
      // ...prevState,
      // color: 'red',
      return reducer(action, prevState);
    });
  };

  return (
    <div>
      <h2>Counter</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
      <button onClick={handleChangeColor1}>녹색</button>
      <button onClick={handleChangeColor2}>파랑</button>
      <button onClick={handleChangeColor3}>빨강</button>
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

export default Counter3;

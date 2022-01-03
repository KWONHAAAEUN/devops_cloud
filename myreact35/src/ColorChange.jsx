import { useState } from 'react';

function dispatch(action, prevState) {
  const { type, color } = action;
  if (type === 'CHANGE_COLOR') {
    return color;
  }
  return prevState;
}

function ColorChange() {
  const [color, setColor] = useState('red');
  const handleChange1 = () => {
    const action = { type: 'CHANGE_COLOR', color: 'green' };
    setColor((prevValue) => {
      return dispatch(action, prevValue);
    });
  };
  const handleChange2 = () => {
    const action = { type: 'CHANGE_COLOR', color: 'blue' };
    setColor((prevValue) => {
      return dispatch(action, prevValue);
    });
  };
  const handleChange3 = () => {
    const action = { type: 'CHANGE_COLOR', color: 'red' };
    setColor((prevValue) => {
      return dispatch(action, prevValue);
    });
  };
  return (
    <div>
      <h2>ColorChange</h2>
      {color}
      <hr />
      <button onClick={handleChange1}>버튼1</button>
      <button onClick={handleChange2}>버튼2</button>
      <button onClick={handleChange3}>버튼3</button>
    </div>
  );
}
export default ColorChange;

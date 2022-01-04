// useState 버전

import Circle from 'Circle';
import { useReducer, useState } from 'react';
import { shuffle_array, zip } from 'utils';

const INITIAL_STATE = {
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
};

const get_lotto_numbers = () =>
  [...Array(45).keys()]
    .map((index) => index + 1)
    .sort(() => Math.random() - Math.random())
    .slice(0, 7)
    .sort((number1, number2) => number1 - number2);

const ACTION_TYPES = {
  GENERATE_NUMBERS: 'GENERATE_NUMBERS',
  SHUFFLE_NUMBERS: 'SHUFFLE_NUMBERS',
  SHUFFLE_COLORS: 'SHUFFLE_COLORS',
};

// 순수 함수
function reducer(prevState, action) {
  // 새로운 상탯값을 계산해서 리턴합니다.

  const { type } = action;

  if (type === ACTION_TYPES.GENERATE_NUMBERS) {
    return {
      ...prevState,
      numbers: get_lotto_numbers(),
    };
  } else if (type === ACTION_TYPES.SHUFFLE_NUMBERS) {
    return {
      ...prevState,
      numbers: shuffle_array(prevState.numbers),
    };
  } else if (type === ACTION_TYPES.SHUFFLE_COLORS) {
    return {
      ...prevState,
      colors: shuffle_array(prevState.colors),
    };
  }

  return prevState;
}

function SevenNumbers2({ title }) {
  // const [state, setState] = useState(INITIAL_STATE);
  const [state, dispatch] = useReducer(reducer, INITIAL_STATE);

  const generateNumbers = () => {
    // 의도 : numbers 항목을 새로운 배열로 변경하겠다.
    const action = { type: ACTION_TYPES.GENERATE_NUMBERS };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  const shuffleNumbers = () => {
    const action = { type: ACTION_TYPES.SHUFFLE_NUMBERS };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  const shuffleColors = () => {
    const action = { type: ACTION_TYPES.SHUFFLE_COLORS };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  return (
    <div>
      {title && <h2>{title}</h2>}
      {zip(state.numbers, state.colors).map(([number, color]) => (
        <Circle number={number} backgroundColor={color} />
      ))}
      <hr />
      <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
      <button onClick={shuffleNumbers}>SHUFFLE_NUMBERS</button>
      <button onClick={shuffleColors}>SHUFFLE_COLORS</button>
      <hr />
      <pre>{JSON.stringify(state, null, 4)}</pre>
    </div>
  );
}

export default SevenNumbers2;

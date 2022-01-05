// import { useReducer } from 'react';
import { useState } from 'react';
import './Counter.css';

function Counter() {
  const [value, setValue] = useState(0);

  const handlePlus = () => {
    setValue(value + 1);
  };
  const handleMinus = () => {
    setValue(value - 1);
  };
  return (
    <div>
      <div className="counter" style={{ backgroundColor: 'red' }}>
        {value}
      </div>
      <hr />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
    </div>
  );
}

// function reducer(prevState, action) {
//   const { type, amount } = action;
//   if (type === 'PLUS') {
//     return { ...prevState, value: prevState.value + amount };
//   } else if (type === 'MINUS') {
//     return { ...prevState, value: prevState.value - amount };
//   }
// }

// function Counter() {
//   const [state, dispatch] = useReducer(reducer, { value: 0 });

//   return (
//     <div>
//       <div className="counter" style={{ backgroundColor: 'red' }}>
//         {state.value}
//       </div>
//       <button onClick={() => dispatch({ type: 'PLUS', amount: 1 })}>+</button>
//       <button onClick={() => dispatch({ type: 'MINUS', amount: 1 })}>-</button>
//     </div>
//   );
// }

export default Counter;

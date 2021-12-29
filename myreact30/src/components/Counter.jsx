import { useState } from 'react';

function Counter({ initial, color }) {
  // 속성 값을 초기 값으로 참조하여 상탯값 value를 생성
  const [value, setValue] = useState(initial);

  const handleClick = () => {
    setValue(value + 1);
  };

  const handleContextMenu = (e) => {
    // context menu의 기본 동작을 막는다
    e.preventDefault();
    setValue(value - 1);
  };

  return (
    <div
      // 스타일에 bg색만 지정
      style={{ ...style, backgroundColor: color }} // {{ userSelect: 'none' }} // 클릭시에 선택되는 것처럼 파랗게 되는 것을 없앰
      onClick={handleClick}
      onContextMenu={handleContextMenu} // 상황에 맞는 메뉴 우클릭도 가능하게
    >
      {value}
    </div>
  );
}

// 스타일의 기본을 지정할 때 사용
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

export default Counter;

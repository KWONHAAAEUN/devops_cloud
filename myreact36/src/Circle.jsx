import 'Circle.css';

function Circle({ number, backgroundColor, onClick, onContextMenu }) {
  return (
    <div
      className="circle"
      style={{ backgroundColor }}
      onClick={onClick}
      onContextMenu={onContextMenu}
    >
      {number}
    </div>
  );
}

export default Circle;

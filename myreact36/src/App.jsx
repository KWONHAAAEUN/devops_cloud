import SevenNumbers1 from 'SevenNumbers1';
import SevenNumbers2 from 'SevenNumbers2';

function App() {
  return (
    <div>
      <SevenNumbers1 title="useState 버전" />
      <hr />
      <SevenNumbers2 title="useReducer 버전" />
    </div>
  );
}

export default App;

import PageAbout from './pages/PageAbout';
import PageCounter from './pages/PageCounter';
import TopNav from './components/TopNav';
import { useState } from 'react';
import PageLotto from './pages/PageLotto';
import PageYoutube from './pages/PageYoutube';

function App() {
  const [pageName, setPageName] = useState('about');
  // const [lottoList] = useState([]);

  // const changePageName = (pageName) => {
  //   setPageName(pageName); //=== 'about' ? 'counter' : 'about');
  // };

  // const [lottoName, setLottoName] = useState('lotto');

  // const lottoList = (lottoName) => {
  //   setLottoName(lottoName);
  // };
  return (
    <div>
      <h1>하은이의 리액트</h1>
      {/* <button onClick={changePageName}>페이지 토글</button> */}
      <TopNav changePageName={setPageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
      {pageName === 'lotto' && <PageLotto />}
      {pageName === 'youtube' && <PageYoutube />}
    </div>
  );
}
export default App;

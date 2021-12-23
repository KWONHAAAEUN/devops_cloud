import { useState } from 'react';
import initialsongList from './data/melon_data.json';
import './MelonTop100.css';
// 전역 변수: 바뀌지 않는 데이터
// initial로 초기값 설정

function MelonTop100() {
  const [songList, setSongList] = useState([]);

  const handleClick = () => {
    setSongList(initialsongList);
  };

  return (
    <div>
      <h1>멜론 top 100</h1>
      <button onClick={handleClick}>로딩</button>
      <ul className="songList">
        <ul>
          {songList.map((song) => {
            return (
              <li>
                {song.rank}
                {song.title}
                {song.like}
              </li>
            );
          })}
          <li>제목1</li>
          <li>제목2</li>
          <li>제목3</li>
        </ul>
      </ul>
    </div>
  );
}

export default MelonTop100;

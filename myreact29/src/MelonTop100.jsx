import { useState } from 'react';
import { Button as BootstrapButton } from 'react-bootstrap';
import { Button as AntButton } from 'antd';
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
      <BootstrapButton variant="success" onClick={handleClick}>
        로딩
      </BootstrapButton>

      <AntButton type="primary" onClick={handleClick}>
        로딩
      </AntButton>
      <ul className="songList">
        <ul>
          {songList.map((song) => {
            return (
              <li key={song.song_no}>
                {song.rank}
                {song.title}
                {song.like}
              </li>
            );
          })}
        </ul>
      </ul>
    </div>
  );
}

export default MelonTop100;

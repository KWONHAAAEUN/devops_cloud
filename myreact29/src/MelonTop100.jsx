import { useState } from 'react';
import { Button as BootstrapButton } from 'react-bootstrap';
import { Button as AntdButton } from 'antd';
import Axios from 'axios';
import initialsongList from './data/melon_data.json';
import './MelonTop100.css';

// 전역 변수: 바뀌지 않는 데이터
// initial로 초기값 설정

function MelonTop100() {
  const [songList, setSongList] = useState([]);

  const handleClick1 = () => {
    setSongList(initialsongList);
  };

  const handleClick2 = () => {
    const url = 'https://antigravity-daejeon-2021.herokuapp.com/api/melon/';
    Axios.get(url)
      .then((response) => {
        const { data } = response;
        setSongList(data);
        // console.log('응답을 받았습니다.');
        // console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleClick3 = () => {
    setSongList([]);
  };

  return (
    <div>
      <h1>멜론 top 100</h1>
      <p>코딩요정 다녀감ㅋ</p>
      <BootstrapButton variant="success" onClick={handleClick1}>
        파일 로딩
      </BootstrapButton>

      <AntdButton type="primary" onClick={handleClick2}>
        서버 로딩
      </AntdButton>

      <AntdButton type="dashed" onClick={handleClick3}>
        클리어
      </AntdButton>

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

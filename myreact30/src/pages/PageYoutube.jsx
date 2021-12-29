// import { useCallback, useEffect, useState } from 'react';
// import styles from '../app.module.css';
// import VideoList from '../components/video_list';

// function PageYoutube({ youtube }) {
//   const [videos, setVideos] = useState([]);
//   const [selectedVideo, setSelectedVideo] = useState(null);

//   const selectVideo = (video) => {
//     setSelectedVideo(video);
//   };

//   const search = useCallback(
//     (query) => {
//       setSelectedVideo(null);
//       youtube.search(query).then((videos) => setVideos(videos));
//     },
//     [youtube],
//   );
//   useEffect(() => {
//     youtube.mostPopular().then((videos) => setVideos(videos));
//   }, [youtube]);
//   return (
//     // <div>
//     // {selectedVideo}
//     // </div>
//     <div calssName={styles.list}>
//       <VideoList
//         videos={videos}
//         onVideoClick={selectVideo}
//         display={selectedVideo ? 'list' : 'grid'}
//       />
//     </div>
//   );
// }

// export default PageYoutube;

import { Input } from 'antd';
import { useState } from 'react';
import { List, Avatar } from 'antd';
import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';
import { Tag } from 'antd';

function PageYoutube() {
  const [query, setQuery] = useState('');
  const [songList, setSongList] = useState([]);

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQuery(value);
  };

  const handlePressEnter = () => {
    console.group('handlePressEnter');
    console.log(`검색어 ${query}로 검색합니다.`);
    console.groupEnd();

    const url = 'https://www.googleapis.com/youtube/v3';

    Axios({
      url: url,
      adapter: jsonpAdapter,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      .then((response) => {
        // ALBUMCONTENTS, ARTISTCONTENTS
        const {
          data: { SONGCONTENTS: searchedSongList },
        } = response;

        console.group('멜론 검색결과');
        console.log(response);
        console.log(searchedSongList);
        console.groupEnd();

        setSongList(searchedSongList);
      })
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.error(error);
        console.groupEnd();
      });
  };

  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      검색어 : {query}
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
      {songList.map((song) => {
        return (
          <div>
            <img src={song.ALBUMIMG} />
            {song.SONGNAME} by {song.ARTISTNAME}
          </div>
        );
      })}
    </div>
  );
}

export default PageYoutube;

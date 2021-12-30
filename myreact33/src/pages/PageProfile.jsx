import { useState } from 'react';
import Axios from 'axios';

const { useEffect } = require('react');

function PageProfile() {
  const [profileList, setProfileList] = useState([]);
  const [error, setError] = useState(null);
  const handleRefresh = () => {
    setError(null); // setError의 값을 null로 변경하여 오류가 저장되었던 것을 비워줌
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const newNameList = response.data.map((profile) => ({
          uniqueId: profile.unique_id,
          name: profile.name,
          role: profile.role,
          mbti: profile.mbti,
          instagramUrl: profile.instagram_url,
          profileImageUrl: profile.profile_image_url,
        }));
        setProfileList(newNameList);
      })
      // reponse는 axios 객체
      // response.data => 응답 내용
      .catch((error) => {
        setError(error); // error가 생기면 setError에 값을 저장함
      });
  };
  const [userNum, setUserNum] = useState('bts-jin');

  const handleClear = () => {
    setProfileList([]);
  };

  useEffect(() => handleRefresh(), []);

  return (
    <div>
      <h1>Profile List</h1>
      <button onClick={handleClear}>클리어</button>
      <button onClick={handleRefresh}>새로고침</button>
      {profileList.length === 0 && <h3>등록된 프로필이 없습니다</h3>}
      {error && (
        <h3>조회 시에 오류가 발생했습니다. 잠시 후 다시 시도해주세요</h3>
      )}
      {/* 선택적 랜더링을 통해 error가 발생하면 메세지를 내보냄 */}
      {profileList.map((bts) => {
        return (
          <div key={bts.uniqueId}>
            <h2>{bts.uniqueId}</h2>
            <ul>
              <li>{bts.name}</li>
              <li>{bts.role}</li>
              <li>{bts.mbti}</li>
              <li>{bts.instagramUrl}</li>
              <img src={bts.profileImageUrl} alt="" />
            </ul>
          </div>
        );
      })}
    </div>
  );
}
export default PageProfile;

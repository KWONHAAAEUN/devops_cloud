import { useState } from 'react';
import Axios from 'axios';

const { useEffect } = require('react');

function PageProfile() {
  const [profileList, setProfileList] = useState([]);
  const [filteredList, setFilteredList] = useState([]);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState('');

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
        setFilteredList(newNameList);
      })
      // reponse는 axios 객체
      // response.data => 응답 내용
      .catch((error) => {
        setError(error); // error가 생기면 setError에 값을 저장함
      });
  };

  useEffect(() => handleRefresh(), []);

  const [userNum, setUserNum] = useState('bts-jin');

  const handleChange = (e) => {
    const value = e.target.value;
    console.log(value);
    setQuery(value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      // Enter 키를 입력했습니다.
      console.log('ENTER');
      // const value = e.target.value;
      // setQuery(value);
      const profile1 = profileList.filter((member) => {
        if (query.length === 0) {
        }
        return (
          member.name.includes(query) ||
          member.role.includes(query) ||
          member.mbti.includes(query)
        );
      });
      setFilteredList(profile1);
    }
  };

  const handleClear = () => {
    setFilteredList([]);
  };

  return (
    <div>
      <h1>Profile List</h1>
      <input
        type="text"
        placeholder="검색어를 입력해주세요."
        onKeyPress={handleKeyPress}
        onChange={handleChange}
      />
      <button onClick={handleClear}>클리어</button>
      <button onClick={handleRefresh}>새로고침</button>
      {filteredList.length === 0 && <h3>등록된 프로필이 없습니다</h3>}
      {error && (
        <h3>조회 시에 오류가 발생했습니다. 잠시 후 다시 시도해주세요</h3>
      )}
      {/* 선택적 랜더링을 통해 error가 발생하면 메세지를 내보냄 */}
      {filteredList.map((bts) => {
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

import PageLotto from "./pages/PageLotto";
// import ProfileCard from "./pages/ProfileCard";
// import profiles from "./data/profiles.json";
import ProfileCard from "./pages/ProfileCard";
// import Nav from "./components/Nav";
import { useState } from "react";
// import changePage from "./ProfileCard";
import Axios from "axios";

const { useEffect } = require("react");

function App() {
  // const [userNum, setuserNum] = useState(profiles[0].user);

  const [profileList, setProfileList] = useState([]);
  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        // reponse는 axios 객체
        // response.data => 응답 내용
        setProfileList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);
  const [userNum, setUserNum] = useState("bts-jin"); // 페이지 넘기기 용도
  return (
    <>
      {profileList.map((profile, index) => {
        if (userNum == profile.unique_id) {
          return (
            <div key={profile.unique_id} className={`user${index % 4}`}>
              <ProfileCard
                profile_image_url={profile.profile_image_url}
                user={profile.unique_id}
                name={profile.name}
                role={profile.role}
                mbti={profile.mbti}
                instagram_url={profile.instagram_url}
                changePage={setProfileList}
              >
                {profileList.map((_profile) => {
                  return (
                    <a
                      onClick={() => setUserNum(_profile.unique_id)}
                      className={userNum === _profile.unique_id ? "on" : ""}
                    />
                  );
                })}
              </ProfileCard>
            </div>
          );
        }
      })}
    </>
  );

  //   return (
  //     <div>
  //       {profileList.map((bts) => {
  //         return (
  //           <>
  //             {bts.name}
  //             {bts.role}
  //             {bts.mbti}
  //             {bts.instagram_url}
  //             {bts.profile_image_url}
  //           </>
  //         );
  //       })}
  //     </div>
  //   );
  // }
}
export default App;

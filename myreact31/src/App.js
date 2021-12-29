import PageLotto from "./pages/PageLotto";
// import ProfileCard from "./pages/ProfileCard";
import profiles from "./data/profiles.json";
import ProfileCard from "./pages/ProfileCard";
// import Nav from "./components/Nav";
import { useState } from "react";
// import changePage from "./ProfileCard";
import Axios from "axios";

// const { useState, useEffect } = require("react");

function App() {
  const [userNum, setuserNum] = useState(profiles[0].user);

  return (
    <>
      {profiles.map((profile, index) => {
        if (userNum == profile.user) {
          return (
            <div className={`user${index % 4}`}>
              <ProfileCard
                img={`/profile-images/user${index + 1}.jpg`}
                user={profile.user}
                name={profile.name}
                role={profile.role}
                facebook_url={profile.facebook_url}
                email={profile.email}
                changePage={setuserNum}
              >
                {profiles.map((profile) => {
                  return (
                    <a
                      onClick={() => setuserNum(profile.user)}
                      className={userNum === profile.user ? "on" : ""}
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
  //   const [profileList, setProfileList] = useState([]);
  //   useEffect(() => {
  //     Axios.get(
  //       "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
  //     )
  //       .then((response) => {
  //         // reponse는 axios 객체
  //         // response.data => 응답 내용
  //         setProfileList(response.data);
  //       })
  //       .catch((error) => {
  //         console.error(error);
  //       });
  //   }, []);

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

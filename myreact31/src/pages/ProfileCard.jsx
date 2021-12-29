// import ProfileImage from "../public/profile-images/haeun.jpg";
import "./ProfileCard.css";
// import profile from "../data/profile";
// import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faStickyNote } from "@fortawesome/free-solid-svg-icons";
import { faFacebook } from "@fortawesome/free-brands-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";
import { Children } from "react/cjs/react.production.min";

library.add(faFacebook);

function ProfileCard({
  children,
  img,
  user,
  name,
  role,
  facebook_url,
  email,
  changePage,
}) {
  //   const [profileList, setProfileList] = useState([]);
  //   const handleClick = () => {
  //     setProfileList(profile);
  //   };
  //   {
  //     profile.map((e) => {
  //       return (
  //         <div>
  //           name={e.name}
  //           role={e.role}
  //           facebook_url={e.facebook_url}
  //           email={e.email}
  //           <button onClick={handleClick}>클릭</button>
  //         </div>
  //       );
  //     });
  //   }

  return (
    <div>
      <h2>Profile Card</h2>
      <section>
        <nav class="menu">
          <a href="#">
            <FontAwesomeIcon icon={faBars} />
          </a>
          <a href="#">
            <FontAwesomeIcon icon={faStickyNote} />
          </a>
        </nav>
        <article class="profile">
          <img src={img} />

          <h1>{name}</h1>
          <h2>{role}</h2>

          <a href="#" class="btnView">
            VIEW MORE
          </a>
        </article>
        <ul class="contact">
          <li>
            <FontAwesomeIcon icon={faFacebook} />{" "}
            {/* <FontAwesomeIcon icon="faFacebookF" /> */}
            {facebook_url}
          </li>
          <li>
            <i class="fas fa-envelope"></i>
            <span>{email}</span>
          </li>
        </ul>

        <nav className="others">{children}</nav>
      </section>
    </div>
  );
}

export default ProfileCard;

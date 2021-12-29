function Nav({ changePageName }) {
  return (
    <ul>
      <li>
        <a onClick={() => changePageName("member1")}>member1</a>
      </li>
      <li>
        <a onClick={() => changePageName("member2")}>member2</a>
      </li>
      <li>
        <a onClick={() => changePageName("member3")}>member3</a>
      </li>
      <li>
        <a onClick={() => changePageName("member4")}>member4</a>
      </li>
    </ul>
  );
}

export default Nav;

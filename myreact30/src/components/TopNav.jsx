function TopNav({ changePageName }) {
  return (
    <ul>
      <li>
        <a onClick={() => changePageName('about')}>About</a>
      </li>
      <li>
        <a onClick={() => changePageName('counter')}>Counter</a>
      </li>
      <li>
        <a onClick={() => changePageName('lotto')}>Lotto</a>
      </li>
      <li>
        <a onClick={() => changePageName('youtube')}>Youtube</a>
      </li>
    </ul>
  );
}

export default TopNav;

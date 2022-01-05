function ReviewClick() {
  const new_review = () => console.log('클릭');
  return (
    <div>
      <button onClick={new_review}>New Review</button>
    </div>
  );
}

export default ReviewClick;

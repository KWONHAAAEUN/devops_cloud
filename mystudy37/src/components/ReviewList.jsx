import { useState } from 'react';
import './ReviewList.css';

const INITIAL_STATE = [
  { content: '리뷰1' },
  { content: '리뷰2' },
  { content: '리뷰3' },
];

function Reviewlist() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);

  const removeReview = (reviewIndex) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter((_, index) => index !== reviewIndex),
    );
  };
  return (
    <div className="review-list">
      <h2>ReviewList</h2>

      {reviewList.map((review, index) => (
        <div onClick={() => removeReview(index)}>{review.content}</div>
      ))}
    </div>
  );
}

export default Reviewlist;

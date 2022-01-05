import { useState } from 'react';
import './ReviewList.css';
import Review from './Review';
import ReviewForm from './ReviewForm';
import ReviewClick from './ReviewClick';

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

      <ReviewClick />
      {/* <ReviewForm /> */}

      {reviewList.map((review, index) => (
        // <div onClick={() => removeReview(index)}>{review.content}</div>
        <Review review={review} onClick={() => removeReview(index)} />
      ))}
    </div>
  );
}

export default Reviewlist;

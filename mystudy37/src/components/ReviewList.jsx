import { useState } from 'react';
import './ReviewList.css';
import Review from './Review';
import ReviewForm from './ReviewForm';
import useFieldValues from 'hook/useFieldValues';
import Star from './Star';

const INITIAL_STATE = [
  { review: '첫번째 리뷰', star: '2' },
  { review: '두번째 리뷰', star: '3' },
  { review: '세번째 리뷰', star: '1' },
];

function Reviewlist() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);

  const [fieldValues, handleChange] = useFieldValues({
    star: '',
    review: '',
  });

  const removeReview = (reviewIndex) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter((_, index) => index !== reviewIndex),
    );
  };

  const review = { ...fieldValues };
  const appendReview = () => {
    console.log('새로운 리뷰 저장');
    setReviewList((prevReviewList) => [...prevReviewList, review]);
  };

  return (
    <div className="review-list">
      <h2>ReviewList</h2>

      <ReviewForm
        handleChange={handleChange}
        fieldValues={fieldValues}
        handleSubmit={appendReview}
      />

      {/* <ReviewClick /> */}
      {/* <ReviewForm /> */}
      <Star />

      {reviewList.map((review, index) => (
        // <div onClick={() => removeReview(index)}>{review.content}</div>
        <Review review={review} onClick={() => removeReview(index)} />
      ))}
    </div>
  );
}

export default Reviewlist;

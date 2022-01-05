function Review({ review, onClick }) {
  return (
    <div
      className="bg-white-200 
        hover:bg-green-400 m-1 p-1 
        rounded-lg text-lg 
        border-green-200 border-2
        hover:border-green-500
        hover:scale-105 cursor-pointer"
      onClick={onClick}
    >
      {review.star}
      {review.review}
    </div>
  );
}
export default Review;

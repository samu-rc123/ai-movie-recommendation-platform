import { useState } from "react";
import API from "../services/api";

function RecommendationForm({ onSubmit, loading}) {

  const [userId, setUserId] = useState("");
  const [movie, setMovie] = useState("");
  const [review, setReview] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      user_id: Number(userId),
      movie,
      review
    });
  };
  const handleMovieChange = async (e) => {

    const value = e.target.value;
  
    setMovie(value);
  
    if (value.length < 2) {
      setSuggestions([]);
      return;
    }
  
    try {
  
      const response =
        await API.get(
          `/movies/search/${value}`
        );
  
      setSuggestions(
        response.data
      );
  
    } catch (error) {
  
      console.log(error);
  
    }
  };
  return (
    <form
      onSubmit={handleSubmit}
      className="bg-gray-900 p-6 rounded-xl mb-8"
    >

<div className="grid gap-4">

{/* User ID */}
<input
  className="p-3 rounded-lg bg-gray-800"
  placeholder="User ID"
  value={userId}
  onChange={(e) =>
    setUserId(e.target.value)
  }
/>

{/* Movie Name + Suggestions */}
<div className="relative">

  <input
    className="p-3 rounded-lg bg-gray-800 w-full"
    placeholder="Movie Name"
    value={movie}
    onChange={handleMovieChange}
  />

  {suggestions.length > 0 && (

    <div
      className="
      absolute
      z-50
      w-full
      bg-gray-800
      border
      border-gray-700
      rounded-lg
      overflow-hidden
      mt-1
      "
    >

      {suggestions.map(
        (item, index) => (

          <div
            key={index}
            className="
            p-3
            hover:bg-gray-700
            cursor-pointer
            "
            onClick={() => {

              setMovie(item);
              setSuggestions([]);

            }}
          >
            {item}
          </div>

        )
      )}

    </div>

  )}

</div>

{/* Review */}
<textarea
  className="p-3 rounded-lg bg-gray-800"
  rows="4"
  placeholder="Write a review..."
  value={review}
  onChange={(e) =>
    setReview(e.target.value)
  }
/>

{/* Button */}
<button
  disabled={loading}
  className="
    bg-blue-600
    hover:bg-blue-700
    p-3
    rounded-lg
    font-bold
    disabled:bg-gray-700
    disabled:cursor-not-allowed
  "
>
  {loading
    ? "Generating Recommendations..."
    : "Get Recommendations"}
</button>

</div>
    </form>
  );
}

export default RecommendationForm;
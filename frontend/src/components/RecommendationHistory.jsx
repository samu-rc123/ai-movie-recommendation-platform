function RecommendationHistory({
    history
  }) {
  
    if (
      history.length === 0
    ) {
      return null;
    }
  
    return (
  
      <div
        className="
        bg-gray-900
        border
        border-gray-800
        rounded-xl
        p-6
        mb-8
        "
      >
  
        <h2
          className="
          text-2xl
          font-bold
          mb-4
          "
        >
          Recent Searches
        </h2>
  
        <div
          className="
          flex
          flex-wrap
          gap-3
          "
        >
  
          {
            history.map(
              (
                movie,
                index
              ) => (
  
                <span
                  key={index}
                  className="
                  bg-purple-600
                  px-4
                  py-2
                  rounded-full
                  text-sm
                  "
                >
                  {movie}
                </span>
  
              )
            )
          }
  
        </div>
  
      </div>
  
    );
  }
  
  export default RecommendationHistory;
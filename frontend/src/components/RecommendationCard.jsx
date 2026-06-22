function RecommendationCard({ movie }) {
  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-lg hover:scale-105 transition">

      <h2 className="text-2xl font-bold text-white mb-4">
        {movie.title}
      </h2>
      <p className="text-gray-300 mt-3">
        Adjusted Score:
        {" "}
        {movie.adjusted_score}
      </p>
      <div className="flex gap-3 mb-4 flex-wrap">

        <span className="bg-purple-600 px-3 py-1 rounded-full text-sm">
          Adjusted: {movie.adjusted_score}
        </span>

        <span className="bg-blue-600 px-3 py-1 rounded-full text-sm">
          Score: {movie.final_score}
        </span>

        <span
          className={`px-3 py-1 rounded-full text-sm ${
            movie.sentiment_score > 0.7
              ? "bg-green-600"
              : "bg-red-600"
          }`}
        >
          Sentiment: {movie.sentiment_score}
        </span>

      </div>

      <div className="space-y-2">
        {(movie.reason || []).map((r, index) => (
          <div
            key={index}
            className="bg-gray-800 rounded-lg px-3 py-2 text-sm"
          >
            ✓ {r}
          </div>
        ))}
      </div>

    </div>
  )
}

export default RecommendationCard
import { useState } from "react";

import API from "./services/api";

import RecommendationForm
from "./components/RecommendationForm";

import RecommendationCard
from "./components/RecommendationCard";
import MetricsDashboard
from "./components/MetricsDashboard";
import RecommendationHistory
from "./components/RecommendationHistory";
import { saveAs } from "file-saver";

function App() {

  const [results, setResults] =
    useState([]);
  const [reviewSentiment, setReviewSentiment] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const submitRecommendation = async (payload) => {

    try {
  
      setLoading(true);
      setError("");
  
      const response = await API.post(
        "/recommend-with-review",
        payload
      );
      setReviewSentiment(
        response.data.review_sentiment
      );
  
      setResults(
        response.data.recommendations
      );
      const newHistory = [

        payload.movie,
      
        ...history.filter(
          item =>
            item !== payload.movie
        )
      
      ].slice(0, 5);
      
      setHistory(newHistory);
      
      localStorage.setItem(
        "movieHistory",
        JSON.stringify(newHistory)
      );
      } catch (err) {
      setError(
        "Failed to fetch recommendations."
      );
      } finally {
        setLoading(false);
    }
  };
  const [history, setHistory] = useState(() => {

    const saved =
      localStorage.getItem(
        "movieHistory"
      );
  
    return saved
      ? JSON.parse(saved)
      : [];
  
  });
  const downloadReport = async () => {

    const response = await API.post(
      "/report",
      {
        movie: history[0],
        review_sentiment: reviewSentiment,
        recommendations: results
      },
      {
        responseType: "blob"
      }
    );
  
    saveAs(
      response.data,
      "recommendation_report.pdf"
    );
  };
  return (
    <div className="min-h-screen bg-gray-950 text-white">

      <div className="max-w-6xl mx-auto p-8">

        <h1
          className="text-5xl font-bold text-center mb-10"
        >
          🎬 AI Movie Recommendation Platform
        </h1>
        <MetricsDashboard />
        <RecommendationHistory
        history={history}
        />

        <RecommendationForm
          onSubmit={submitRecommendation}
          loading={loading}
        />

        
        {
  loading && (
    <div
      className="
      bg-blue-600
      p-4
      rounded-lg
      mb-6
      animate-pulse
      "
    >
      Finding recommendations...
    </div>
  )
}
        {
  error && (
    <div
      className="
      bg-red-600
      p-4
      rounded-lg
      mb-6
      "
    >
      {error}
    </div>
  )
}
        {reviewSentiment && (
        <div
          className="bg-gray-900 border border-gray-800 rounded-xl p-6 mb-8"
        >
          <h2
            className="text-2xl font-bold mb-4"
          >
            Review Analysis
          </h2>

          <div className="flex items-center gap-4">

            <span
              className={`px-4 py-2 rounded-full font-bold ${
                reviewSentiment.label === "POSITIVE"
                  ? "bg-green-600"
                  : "bg-red-600"
              }`}
            >
              {reviewSentiment.label}
            </span>

            <span className="text-lg">
              Confidence:
              {" "}
              {(reviewSentiment.score * 100).toFixed(2)}%
            </span>

          </div>
        </div>
        )}
      
      <div
  className="grid md:grid-cols-2 lg:grid-cols-3 gap-6"
>
  {results.map((movie) => (
    <RecommendationCard
      key={movie.title}
      movie={movie}
    />
  ))}
</div>

{results.length > 0 && (
  <div className="flex justify-center">
    <button
      onClick={downloadReport}
      className="
      bg-green-600
      hover:bg-green-700
      px-6
      py-3
      rounded-lg
      font-bold
      mt-8
      "
    >
      Download Report
    </button>
  </div>
)}


      </div>

    </div>
  );
}

export default App;
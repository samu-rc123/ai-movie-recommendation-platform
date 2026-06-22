function MetricsDashboard() {
    return (
      <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 mb-8">
  
        <h2 className="text-3xl font-bold mb-6">
          Model Performance
        </h2>
  
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
  
          <div className="bg-gray-800 p-5 rounded-xl">
            <h3 className="font-bold text-xl mb-3">
              Content-Based
            </h3>
  
            <p>Movies Indexed: 4806</p>
            <p>TF-IDF Features: 5000</p>
          </div>
  
          <div className="bg-gray-800 p-5 rounded-xl">
            <h3 className="font-bold text-xl mb-3">
              Collaborative Filtering
            </h3>
  
            <p>Algorithm: SVD</p>
            <p>RMSE: 0.8793</p>
          </div>
  
          <div className="bg-gray-800 p-5 rounded-xl">
            <h3 className="font-bold text-xl mb-3">
              Sentiment Analysis
            </h3>
  
            <p>Model: DistilBERT</p>
            <p>Accuracy: 87.2%</p>
          </div>
  
        </div>
  
      </div>
    );
  }
  
  export default MetricsDashboard;
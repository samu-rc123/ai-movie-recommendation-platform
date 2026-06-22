# AI Movie Recommendation Platform

An end-to-end AI-powered movie recommendation system that combines content-based filtering, collaborative filtering, and sentiment analysis to generate personalized movie recommendations.

## Features

* Content-Based Filtering (TF-IDF)
* Collaborative Filtering (SVD)
* Hybrid Recommendation Engine
* DistilBERT Sentiment Analysis
* Explainable AI Recommendations
* Review-Aware Ranking
* Search Autocomplete
* Recommendation History

## Tech Stack

### Frontend

* React
* Tailwind CSS
* Axios

### Backend

* FastAPI
* Scikit-Learn
* Surprise
* Transformers
* Pandas
* NumPy

## Model Performance

* TF-IDF Features: 5000
* Movies Indexed: 4806
* SVD RMSE: 0.8793
* DistilBERT Accuracy: 87.2%

## Project Architecture

```text
React Frontend
      ↓
FastAPI Backend
      ↓
Hybrid Recommendation Engine
 ├── Content-Based Filtering
 ├── Collaborative Filtering (SVD)
 └── Sentiment Analysis
      ↓
Explainable Recommendations
```

## API Endpoints

* `POST /recommend`
* `POST /recommend-with-review`
* `POST /sentiment`
* `POST /sentiment/aggregate`

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Future Improvements

* TMDB Poster Integration
* User Authentication
* Recommendation Feedback Loop
* Embedding-Based Recommendations
* LLM-Generated Explanations

## Screenshots
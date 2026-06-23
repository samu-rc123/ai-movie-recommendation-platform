# AI-Powered Movie Recommendation Platform

## Overview

An end-to-end AI-powered Movie Recommendation Platform that combines Content-Based Filtering, Collaborative Filtering, Sentiment Analysis, and Explainable AI to deliver personalized movie recommendations.

The platform is deployed as a full-stack application with a React frontend, FastAPI backend, Hugging Face model hosting, and cloud deployment on Vercel and Render.

---

## Live Demo

Frontend: https://ai-movie-recommendation-platform.vercel.app/

Backend API: https://ai-movie-recommendation-platform.onrender.com/docs

---

## Key Features

### Content-Based Recommendation

* TF-IDF vectorization on movie metadata
* Cosine similarity-based recommendation engine
* Real-time recommendation generation

### Collaborative Filtering

* SVD (Singular Value Decomposition) model trained on MovieLens ratings
* Personalized rating prediction
* User-specific recommendation scoring

### Hybrid Recommendation System

* Combines:

  * Content Similarity
  * Collaborative Filtering
  * Sentiment-Aware Ranking
* Produces more relevant recommendations than individual methods

### Explainable AI

Each recommendation includes human-readable explanations such as:

* Strong content similarity
* Predicted user preference
* Positive audience sentiment

### Sentiment-Aware Ranking

* Fine-tuned DistilBERT sentiment analysis pipeline
* Audience review sentiment aggregation
* Sentiment-adjusted recommendation scores

### Search & Recommendation History

* Tracks previously searched movies
* Stores recommendation history
* Improves user experience and exploration

### PDF Report Generation

* Export recommendation reports
* Useful for sharing and offline analysis

---

## System Architecture

Frontend (React + Vite)
↓
FastAPI Backend
↓
Hybrid Recommendation Engine
├── TF-IDF Content Filtering
├── SVD Collaborative Filtering
└── Sentiment-Aware Ranking
↓
Hugging Face Model Repository

---

## Tech Stack

### Frontend

* React
* Vite
* Axios

### Backend

* FastAPI
* Python

### Machine Learning

* Scikit-Learn
* Surprise Library (SVD)
* Transformers
* DistilBERT

### Deployment

* Vercel
* Render
* Hugging Face Hub

### Data

* MovieLens Dataset
* TMDB Metadata

---

## Engineering Optimizations

### Model Storage Optimization

Initially, recommendation similarity matrices and trained models were stored locally, leading to deployment memory constraints.

To overcome cloud resource limitations:

* Migrated trained models to Hugging Face Hub
* Implemented lazy loading of recommendation models
* Removed large precomputed similarity matrices
* Generated TF-IDF representations dynamically
* Reduced memory consumption for cloud deployment

This enabled successful deployment on free-tier infrastructure while maintaining recommendation quality.

---

## Future Improvements

* TMDB Poster Integration
* User Authentication
* Docker Containerization
* Redis Recommendation Caching
* Recommendation Analytics Dashboard
* CI/CD with GitHub Actions

---

## Author

Samrat Roy Choudhury

Mechanical Engineering, Jadavpur University

Aspiring Machine Learning Engineer | Software Engineer | Data Scientist

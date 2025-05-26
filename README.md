# 📚 Book Recommendation System

This repository contains a web-based Book Recommendation System that suggests books based on user preferences using content-based filtering techniques. Built with Python and Flask, it uses precomputed machine learning artifacts to deliver fast and personalized recommendations.

## 🔍 Features

- 📖 Recommends similar books using cosine similarity
- 📊 Displays a list of popular books
- 🧠 Uses pre-trained data models for instant predictions
- 🌐 Simple and responsive web interface

## 🏗️ Project Structure

├── app.py # Main Flask app
├── templates/ # HTML templates for the frontend
├── books.pkl # Metadata of available books
├── popular.pkl # Popular books data
├── pt.pkl # Book-user matrix (pivot table)
├── similarity_score.pkl # Precomputed similarity scores
├── requirements.txt # Python dependencies
├── Procfile # For Heroku deployment
├── .gitignore
└── README.md


## 💡 How It Works

- **User Input**: The user selects a book title from the homepage.
- **Similarity Calculation**: The app looks up similar books using cosine similarity from `similarity_score.pkl`.
- **Recommendation Output**: It fetches metadata (author, image, rating) from `books.pkl` and displays the top results.
- **Popular Section**: Displays top-rated and frequently-read books from `popular.pkl`.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PriyankaSharma0925/book-recommendation-system.git
   cd book-recommendation-system

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser.

☁️ Deployment (Heroku)
This app is ready to be deployed to Heroku. Simply push the repo to Heroku with a valid Procfile.

bash
Copy
Edit
heroku create book-recommender
git push heroku main

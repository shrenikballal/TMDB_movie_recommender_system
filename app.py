import os
import requests
import pickle
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load movies and similarity data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# List of movie titles for the dropdown
movies_list = movies['title'].values

# Store TMDB API key in environment variables for security
API_KEY = os.getenv('TMDB_API_KEY', 'YOUR_API_KEY_HERE')

def fetch_poster(movie_id):
    """
    Fetch the movie poster from TMDB using the movie ID.
    """
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        poster_path = data.get('poster_path')
        
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"  # Placeholder if no poster

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/300x450?text=No+Image"  # Return placeholder on error

def recommend(movie):
    """
    Recommend movies based on similarity.
    """
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_poster = []
    
    for i in distances[1:6]:  # Top 5 recommendations (excluding the input movie itself)
        movie_id = movies.iloc[i[0]]["id"]
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    
    return recommended_movie_names, recommended_movie_poster

@app.route('/', methods=['GET', 'POST'])
def index_page():
    """
    Handle the index route to display movie recommendations.
    """
    recommended_movies = []
    recommended_posters = []

    if request.method == 'POST':
        selected_movie = request.form.get('selected_movie')
        recommended_movie_names, recommended_movie_poster = recommend(selected_movie)
        
        # Combine movie names and posters into a list of dictionaries
        recommended_movies_with_posters = [
            {'name': movie, 'poster': poster} 
            for movie, poster in zip(recommended_movie_names, recommended_movie_poster)
        ]
        
        return render_template('index.html', movies=movies_list, selected=selected_movie, recommended_movies=recommended_movies_with_posters)

    return render_template('index.html', movies=movies_list)

if __name__ == "__main__":
    app.run(debug=True)

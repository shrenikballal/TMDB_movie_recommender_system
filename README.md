# 🎬 TMDB Movie Recommender System

A content-based movie recommendation engine that suggests top-rated movies similar to a user's selection. The project utilizes Machine Learning (Cosine Similarity) to compute item-to-item similarities based on movie metadata and features a real-time web interface built with Flask and integrated with the TMDB API to fetch dynamic movie posters.

---

## 🌟 Features

- **Content-Based Recommendations:** Recommends the top 5 most similar movies based on textual and structural metadata matching.
- **Dynamic Poster Fetching:** Real-time integration with The Movie Database (TMDB) API to retrieve high-quality, live movie posters.
- **Graceful Error Handling:** Automated fallback to sleek placeholder images if a network timeout occurs or a movie lacks a poster asset.
- **Clean Flask Web Interface:** Simple, responsive dropdown interface for quick selections and seamless, immediate feedback.

## 🛠️ Tech Stack & Architecture

- **Data Processing & ML:** Python, Pandas, NumPy, Scikit-Learn (Cosine Similarity)
- **Model Serialization:** Pickle (for storing pre-computed dataframes and similarity matrices)
- **Web Framework:** Flask (Python)
- **External Integration:** TMDB API via `requests`
- **Development Workspace:** Jupyter Notebook (`TMDB_Movie_Recommender.ipynb`)

---

## 🚀 Getting Started

Follow these steps to set up the project environment on your local machine.

### Prerequisites

You will need a TMDB API Key to dynamically render movie posters. 
1. Head over to [The Movie Database (TMDB)](https://www.themoviedb.org/) and create a free account.
2. Navigate to your account settings to request an **API Key (v3 auth)**.

### Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shrenikballal/TMDB_movie_recommender_system.git](https://github.com/shrenikballal/TMDB_movie_recommender_system.git)
   cd TMDB_movie_recommender_system
   ```

2. Generate the Artifacts (If needed):
Run through the TMDB_Movie_Recommender.ipynb notebook to preprocess the dataset and generate the serialized tracking matrices. Ensure the following files are saved directly into your root directory:
- movies.pkl
- similarity.pkl

3. Install Dependencies:
   ```bash
   pip install flask pandas requests
   ```
4. Set up Environment Variables:
   - On Windows (Command Prompt):
   ```bash
   set TMDB_API_KEY=your_actual_tmdb_api_key_here
   ```
   - On MacOS / Linux:
   ```bash
   export TMDB_API_KEY="your_actual_tmdb_api_key_here"
   ```
5. Run the Application:
   ```bash
   python app.py
   ```

### 🔮 How It Works
```
[ User Input ] ➔ [ Fetch Movie Index ] ➔ [ Check Similarity Matrix ]
                                                   ↓
[ Display Web UI ] 🗂️ [ Fetch Posters via TMDB ] 🗂️ [ Extract Top 5 Closest Vector Matches ]
```

1. Vectorization & Cosine Similarity: In the Jupyter notebook, text attributes (like genres, keywords, cast, and crew) are combined, tokenized, and transformed into vector spaces. Cosine similarity calculations compute an angle-based metric between vectors to determine relative contextual closeness.
2. Data Persistence: The processed movie titles data frame (`movies.pkl`) and the pre-computed mathematical similarity array matrix (`similarity.pkl`) are stored using Python's `pickle` library for instant deployment memory tracking.
3. Flask Architecture: When a user selects a target title via  `app.py`, the index is referenced, distances are sorted in reverse fashion, and the top 5 match indices are extracted.
4. API Integration: The script loops through the recommended IDs, fires an asynchronous network payload to `api.themoviedb.org`, extracts the matching `poster_path`, and securely serves it alongside the title.

# %%
from sqlalchemy import create_engine
import pandas as pd

# Replace with your actual path to the .sqlite file
engine = create_engine('sqlite:///D:\Others\Movie Recommender\movie_db.sqlite')

# Test the connection: read a table
df = pd.read_sql('SELECT * FROM Movies m', engine)
print(df.head())


# %%
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///D:\Others\Movie Recommender\movie_db.sqlite')
# Load necessary tables
ratings = pd.read_sql('SELECT * FROM Ratings', engine)
movies = pd.read_sql('SELECT * FROM Movies', engine)
genres = pd.read_sql('SELECT * FROM Genres', engine)
movie_genres = pd.read_sql('SELECT * FROM MovieGenres', engine)

# Merge for enriched movie data
movie_data = movies.merge(movie_genres, on='movie_id').merge(genres, on='genre_id')
full_data = ratings.merge(movie_data, on='movie_id')

# %%
user_id = 1  # You can change this to any user_id from your Users table

# Get this user's rated movies
user_ratings = full_data[full_data['user_id'] == user_id]

# Get user's favorite genres
fav_genres = (
    user_ratings.groupby('genre_name')['rating']
    .mean()
    .sort_values(ascending=False)
)

print("User's favorite genres:\n", fav_genres)


# %%
top_genre = fav_genres.index[0]  # pick the top genre

# Movies the user hasn’t rated yet
unrated = full_data[~full_data['movie_id'].isin(user_ratings['movie_id'])]

# Filter for top genre
recommend_pool = unrated[unrated['genre_name'] == top_genre]

# Recommend top-rated movies from this genre
recommendations = (
    recommend_pool.groupby(['movie_id', 'title'])['rating']
    .mean()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

print(f"\n🎬 Top movie recommendations for User {user_id} based on genre '{top_genre}':")
print(recommendations)


# %%
user_id = 1
user_ratings = full_data[full_data['user_id'] == user_id]

print(user_ratings[['title', 'genre_name', 'rating']])


# %%
action_movies = full_data[full_data['genre_name'] == 'Action']
print(action_movies[['title']].drop_duplicates())


# %%
seen_movie_ids = user_ratings['movie_id'].unique()
unseen_actions = action_movies[~action_movies['movie_id'].isin(seen_movie_ids)]

print(unseen_actions[['title', 'rating']].dropna().sort_values('rating', ascending=False).head())




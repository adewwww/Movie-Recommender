# Movie-Recommender
 # Movie Recommender Engine 🎬

A simple recommendation system built using Python, SQLite, SQLAlchemy, and pandas.

## Features
- Connects to a local movie database
- Recommends movies based on user preferences
- Uses genre and ratings logic

## How to Run

```bash
pip install -r requirements.txt
python main.py

```

## 📦 movie_db.sqlite

This is the SQLite database used in the project.  
Download it via the "View Raw" button and use it in Python or DBeaver.

Example connection in Python:
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///movie_db.sqlite')

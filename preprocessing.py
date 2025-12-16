import pandas as pd
import ast

def load_and_preprocess(path):
    movies = pd.read_csv(path)
    movies = movies[['title', 'overview', 'genres', 'keywords']]
    movies.dropna(inplace = True)

    def parse(text):
        return " ".join([i['name'] for i in ast.literal_eval(text)])

    movies['genres'] = movies['genres'].apply(parse)
    movies['keywords'] = movies['keywords'].apply(parse)

    movies['content'] = (
        movies['overview'] + " " +
        movies['genres'] + " " +
        movies['keywords']
    )

    return movies
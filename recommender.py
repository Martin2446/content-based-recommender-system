from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import load_and_preprocess

movies = load_and_preprocess("data/tmdb_5000_movies.csv")

vectorizer = TfidfVectorizer(stop_words = 'english', max_features=5000)
tfidf_matrix = vectorizer.fit_transform(movies['content'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movies(title, top_n = 10):
    idx = movies[movies['title'] == title].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key = lambda x: x[1], reverse = True)
    scores = scores[1:top_n+1]
    indices = [i[0] for i in scores]
    return movies['title'].iloc[indices]

def recommend_for_user(liked_movies, top_n = 10):
    indices = movies[movies['title'].isin(liked_movies)].index
    user_vector = tfidf_matrix[indices].mean(axis = 0)
    similarity = cosine_similarity(user_vector, tfidf_matrix)[0]
    movie_indices = similarity.argsort()[::-1][:top_n]
    return movies['title'].iloc[movie_indices]
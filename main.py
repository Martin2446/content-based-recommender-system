from recommender import recommend_movies

recommendations = recommend_movies("Brave")

for movie in recommendations:
    print(f"- {movie}")
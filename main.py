from recommender import recommend_movies, recommend_for_user

print("Similar movies to 'The Dark Knight':")
print(recommend_movies("The Dark Knight"))

print("\n Recommendations for user who likes Inception and Interstellar:")
# print(recommend_for_user(["Inception", "Interstellar"]))
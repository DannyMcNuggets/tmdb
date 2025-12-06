import requests
import pandas as pd

headers = {
    "accept": "application/json",
    "Authorization": "Bearer TOKEN" #not putting my token in public
}

# tv genres
tv_url = "https://api.themoviedb.org/3/genre/tv/list"
tv_response = requests.get(tv_url, headers=headers)
tv_data = tv_response.json()
tv_df = pd.DataFrame(tv_data["genres"])

# movie genres
movie_url = "https://api.themoviedb.org/3/genre/movie/list"
movie_response = requests.get(movie_url, headers=headers)
movie_data = movie_response.json()
movie_df = pd.DataFrame(movie_data["genres"])

genres_df = pd.concat([tv_df, movie_df])
genres_df = genres_df.drop_duplicates(subset="id").sort_values("id")

# renaming for further work with dataset.csv
genres_df = genres_df.rename(columns={
    "id": "id_genre",
    "name": "genre_name"
}) 

genres_df.to_csv("genres.csv", index=False)




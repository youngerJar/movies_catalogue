import requests
API_TOKEN ="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNzBkMjQzYTk0YTc1NjMxOGY1N2IyMjE4YzRjYWJhOSIsInN1YiI6IjYyOWIxYmZhZDQ2NTM3MDA2NGQ1MTU2MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.reHbRfbHTG495nuPKO_dS9dBkll2Qu0-nAhpm1PAGcM"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()
  
def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type='popular'):
    movie_types=['popular', 'top_rated', 'upcoming']
    if not list_type in movie_types:
        list_type='popular'
    data = get_movies_list(list_type)
    return data["results"][:how_many]
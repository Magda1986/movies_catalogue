#from nturl2path import url2pathname
import requests

# funkcja zwraca pełną listę popularnych filmów, "Authorization" - token autoryzacyjny
def get_popular_movies(list_type):
    api_key = "6fff7883f182efb5650e7d40ba60ee3b"
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    url = endpoint + "?api_key=" + api_key
    # api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmZmNzg4M2YxODJlZmI1NjUwZTdkNDBiYTYwZWUzYiIsInN1YiI6IjYyZGU2MzdhZWE4NGM3MTRlNTg3OTljYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UM4-UJjMj00nFCFVOnhxjONbpX8LSffMqbR9VD1SLG8"
    # headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url)
    return response.json()

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmZmNzg4M2YxODJlZmI1NjUwZTdkNDBiYTYwZWUzYiIsInN1YiI6IjYyZGU2MzdhZWE4NGM3MTRlNTg3OTljYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UM4-UJjMj00nFCFVOnhxjONbpX8LSffMqbR9VD1SLG8"

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

# funkcja zwraca kompletny/działający adres URL do obrazka, poster_api_path-ścieżka do plakatu , size-rozmiar
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

# funkcja modyfikuje sownik zawierający film
def get_movie_info(movie):
    return {"id" : movie["id"],
            "title" : movie["title"],
            "poster_url" : get_poster_url(movie["poster_path"])}

# Funkcja pobiera filmy - 20 i traktuje powyszą funkcją
def get_movies(how_many=20, list_type="popular"):
    all_movies = get_popular_movies(list_type)["results"][:how_many]
    return [get_movie_info(movie) for movie in all_movies]

#print(get_movies())

def get_api_from_tmdb(endpoint):
    url_adres = f"https://api.themoviedb.org/3/{endpoint}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmZmNzg4M2YxODJlZmI1NjUwZTdkNDBiYTYwZWUzYiIsInN1YiI6IjYyZGU2MzdhZWE4NGM3MTRlNTg3OTljYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UM4-UJjMj00nFCFVOnhxjONbpX8LSffMqbR9VD1SLG8"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url_adres, headers=headers)
    response.raise_for_status()
    return response.json()


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmZmNzg4M2YxODJlZmI1NjUwZTdkNDBiYTYwZWUzYiIsInN1YiI6IjYyZGU2MzdhZWE4NGM3MTRlNTg3OTljYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UM4-UJjMj00nFCFVOnhxjONbpX8LSffMqbR9VD1SLG8"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response_json = response.json()
    response_json["poster_url"] = get_poster_url(response_json["backdrop_path"], size="w780")
    return response_json


def get_single_movie_cast(movie_id, how_many=4):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response_json = response.json()["cast"][:how_many]
    for actor in response_json:
        actor["profile_url"] = get_poster_url(actor["profile_path"], size="w185")
    return response_json    
import requests

# funkcja zwraca pełną listę popularnych filmów, "Authorization" - token autoryzacyjny
def get_popular_movies():
    api_key = "6fff7883f182efb5650e7d40ba60ee3b"
    endpoint = f"https://api.themoviedb.org/3/movie/popular"
    url = endpoint + "?api_key=" + api_key
    # api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmZmNzg4M2YxODJlZmI1NjUwZTdkNDBiYTYwZWUzYiIsInN1YiI6IjYyZGU2MzdhZWE4NGM3MTRlNTg3OTljYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UM4-UJjMj00nFCFVOnhxjONbpX8LSffMqbR9VD1SLG8"
    # headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url)
    return response.json()

# funkcja zwraca kompletny/działający adres URL do obrazka, poster_api_path-ścieżka do plakatu , size-rozmiar
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

# funkcja modyfikuje sownik zawierający film
def get_movie_info(movie):
    return {"title" : movie["title"],
    "poster_url" : get_poster_url(movie["poster_path"])}

# Funkcja pobiera filmy i traktuje powyszą funkcją
def get_movies(how_many=20):
    all_movies = get_popular_movies()["results"][:how_many]
    return [get_movie_info(movie) for movie in all_movies]

#print(get_movies())





from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)

list_type = {
        "Popular": "popular", "Top Rated ": "top_rated", "Upcoming": "upcoming", "Now playing": "now_playing"
    }

# strona gwna aplikacji, lista movies zawiera filmy w naszej bibliot
# @app.route("/")
# def homepage():
#     #movies = ["Top Gun", "Tom Gun Maverick", "Mission Impossible","Vanilla Sky", "Jack Reacher", "Rain Man", "Ludzie honoru", "Jerry Maguire"]
#     movies = tmdb_client.get_movies(how_many=8)
#     return render_template("homepage.html", movies=movies)

@app.route("/")
def listpage():
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in list_type.values():
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, list_types=list_type.items(), current_list=selected_list)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    details["cast"] = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details)


# Poniszy zapis umozliwia uruchamić aplikację bezpośrednio w edytorze, klikając przycisk “Play” w prawym górnym rogu okna
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

# strona gwna aplikacji, lista movies zawiera filmy w naszej bibliotece
@app.route("/")
def homepage():
    movies = ["Top Gun", "Tom Gun Maverick", "Mission Impossible","Vanilla Sky", "Jack Reacher", "Rain Man", "Ludzie honoru", "Jerry Maguire"]
    return render_template("homepage.html", movies=movies)


# Poniszy zapis umozliwia uruchamić aplikację bezpośrednio w edytorze, klikając przycisk “Play” w prawym górnym rogu okna
if __name__ == "__main__":
    app.run(debug=True)

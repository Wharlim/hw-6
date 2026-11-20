from Movies import Movies
import sys


def search_movie(movies, string):
    # search for a movie by a string in the title, so it goes through the list of movies and gets it
    list_of_movies = []
    for movie in movies:
        if string.lower() in movie.get_movie_title().lower():
            list_of_movies.append(movie)
    return list_of_movies

def main():
    if (len(sys.argv)!= 2):
        print("Usage: python3 find_movie.py <title>")
        return
    movie_title = sys.argv[1]

    movies = []

    with open("movies.tsv", "r") as infile:
        header = infile.readline()
        for line in infile:
            fields = line.removesuffix("\n").split("\t")
            genres = (fields[2].split("|"))
            movies.append(Movies(fields[0], fields[1], genres, ratings={}))

    list_of_movies = search_movie(movies, movie_title)
    for movie in list_of_movies:
        print(f"Movie ID: {movie.movie_id}, Title: {movie.title}, Genres: {movie.genres}")


if __name__ == "__main__":
    main()
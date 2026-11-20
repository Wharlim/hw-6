#mostly ai
from Movies import Movies
import sys

MIDPOINT = 2.75

def similarity_score(movie1, movie2):
    ratings1 = {user: r - MIDPOINT for user, r in movie1.get_ratings().items()}
    ratings2 = {user: r - MIDPOINT for user, r in movie2.get_ratings().items()}

    dot = 0
    for user in ratings1:
        if user in ratings2:
            dot += ratings1[user] * ratings2[user]

    norm1 = sum(r ** 2 for r in ratings1.values()) ** 0.5
    norm2 = sum(r ** 2 for r in ratings2.values()) ** 0.5
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot / (norm1 * norm2)

def main():
    if (len(sys.argv)!= 2):
        print("Usage: python3 similar_movies.py <movie_id>")
        return
    movie_id = sys.argv[1]

    movies = {}

    with open("movies.tsv", "r") as infile:
        infile.readline()
        for line in infile:
            fields = line.removesuffix("\n").split("\t")
            genres = fields[2].split("|")
            movies[fields[0]] = Movies(fields[0], fields[1], genres, ratings={})

    with open("ratings.tsv", "r") as infile:
        infile.readline()
        for line in infile:
            user_id, mid, rating = line.removesuffix("\n").split("\t")[:3]
            if mid in movies:
                movies[mid].ratings[user_id] = float(rating)

    movie_to_find = movies.get(movie_id)
    if movie_to_find is None:
        print(f"Movie with ID {movie_id} not found.")
        return

    results = []
    for movie in movies.values():
        if movie.movie_id != movie_id:
            score = similarity_score(movie_to_find, movie)
            results.append((score, movie.movie_id, movie.title))

    results.sort(key=lambda r: r[0], reverse=True)

    print(f"Movies similar to {movie_to_find.title}:")
    print("sim\tmovie_id\ttitle")
    for score, mid, title in results[:10]:
        print(f"{score:.3f}\t{mid}\t{title}")

if __name__ == "__main__":
    main()

from Movies import Movies
import sys

"""this is my implementation, without ai, just inline suggestions from github 

"""

def similarity(ratings1, ratings2):
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
    movies = {}

    with open("movies.tsv", "r") as infile:
        header = infile.readline()
        for line in infile:
            fields = line.removesuffix("\n").split("\t")
            genres = (fields[2].split("|"))
            movies[int(fields[0])] = Movies(int(fields[0]), fields[1], genres, ratings={})

    # so now i already have a list of movies, now i need store a dictionary of ratings for each movie. 


    with open("ratings.tsv", "r") as infile:
        header = infile.readline()
        for line in infile:
            fields = line.removesuffix("\n").split("\t")
            movie_id = int(fields[1])
            if movie_id in movies:
                movies[movie_id].ratings[int(fields[0])] = float(fields[2]) - 2.75

    movie_to_find = int(sys.argv[1])
    target_movie = movies.get(movie_to_find)

    results = []
    for movie in movies.values():
        if movie.movie_id != target_movie.movie_id:
            similarity_score = similarity(target_movie.ratings, movie.ratings)
            results.append((similarity_score, movie.movie_id, movie.title))

    sorted_results = sorted(results, key=lambda x: x[0], reverse=True)

    count = 0
    for score, movie_id, title in sorted_results:
        print(f"Similarity score between {target_movie.title} and {title}: {score:.3f}")
        count += 1
        if count >= 10:
            break


if __name__ == "__main__":
    main()

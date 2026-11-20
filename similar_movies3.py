# I store the ratings in a dictionary of dictionaries: ratings[movie_id] maps
# each user who rated that movie to their rating minus 2.75. Most users have
# rated only a few movies, so this keeps just the ratings that exist, and a
# missing user counts as 0. It also makes one movie's ratings quick to look up
# when comparing it with every other movie.
# this solution is entirely AI

import sys


def read_titles():
    titles = {}
    with open("movies.tsv") as infile:
        infile.readline()
        for line in infile:
            fields = line.removesuffix("\n").split("\t")
            titles[fields[0]] = fields[1]
    return titles


def read_ratings(titles):
    ratings = {movie_id: {} for movie_id in titles}
    with open("ratings.tsv") as infile:
        infile.readline()
        for line in infile:
            fields = line.removesuffix("\n").split("\t")
            user_id, movie_id, rating = fields[0], fields[1], fields[2]
            ratings[movie_id][user_id] = float(rating) - 2.75
    return ratings


def length(movie_ratings):
    return sum(r ** 2 for r in movie_ratings.values()) ** 0.5


def similarity(ratings1, ratings2):
    dot = 0
    for user in ratings1:
        if user in ratings2:
            dot += ratings1[user] * ratings2[user]

    lengths = length(ratings1) * length(ratings2)
    if lengths == 0:
        return 0
    return dot / lengths


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 similar_movies.py <movie_id>")
        return

    movie_id = sys.argv[1]
    titles = read_titles()
    if movie_id not in titles:
        print(f"Movie with ID {movie_id} not found.")
        return
    ratings = read_ratings(titles)

    results = []
    for other_id in titles:
        if other_id != movie_id:
            score = similarity(ratings[movie_id], ratings[other_id])
            results.append((score, other_id, titles[other_id]))
    results.sort(key=lambda result: result[0], reverse=True)

    print(f"Movies similar to {titles[movie_id]}:")
    print("sim\tmovie_id\ttitle")
    for score, other_id, title in results[:10]:
        print(f"{score:.3f}\t{other_id}\t{title}")


if __name__ == "__main__":
    main()
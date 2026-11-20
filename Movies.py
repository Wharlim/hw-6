class Movies:
    def __init__(self, movie_id, title, genres, ratings):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres
        self.ratings = ratings

    def __str__(self):
        return f"Movie ID: {self.movie_id}, Title: {self.title}, Genres: {self.genres}, Ratings: {self.ratings}"

    def get_movie_title(self):
        return self.title
    def get_ratings(self):
        return self.ratings

    def set_ratings(self, ratings):
        self.ratings = ratings

    



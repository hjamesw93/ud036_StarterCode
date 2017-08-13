import media
import fresh_tomatoes


def init():
    movies = [media.Movie('Toy Story'), media.Movie('A bug\'s life')]

    fresh_tomatoes.open_movies_page(movies)

init()

import json
import media
import fresh_tomatoes


def main():
    """
    Loads movie data from json included movies.json file and creates Movie objects, appending to movies list.
    Calls open_movies_page function from fresh tomatoes, passing movies list as parameter.
    """

    movies = []

    # Load movie data from json file
    data = open('assets/data/movies.json', 'r')
    movie_list = json.loads(data.read())

    # Create new Movie object for each movie listed in json file
    for movie_data in movie_list:
        movie = media.Movie()

        movie\
            .set_title(movie_data['title'])\
            .set_poster_image_url(movie_data['poster_image_url'])\
            .set_trailer_youtube_id(movie_data['trailer_youtube_id'])\
            .set_trailer_youtube_url(movie_data['trailer_youtube_url'])

        movies.append(movie)

    fresh_tomatoes.open_movies_page(movies)

    # Cleanup - close movie data file
    data.close()

main()

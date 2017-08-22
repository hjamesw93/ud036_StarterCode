class Movie:
    """
    Defines the structure of a Movie object to be consumed by
    fresh_tomatoes.py. 'Setter' functions return self to facilitate function
    chaining.
    """

    def __init__(self):
        """
        Movie constructor. Takes no additional parameters to enforce use of
        setter functions
        """
        self.title = ""
        self.poster_image_url = ""
        self.trailer_youtube_id = ""
        self.trailer_youtube_url = ""

    def set_title(self, title):
        """
        Set the movie title
        :param title:
        :return self:
        """
        self.title = title
        return self

    def set_poster_image_url(self, poster_image_url):
        """
        Set the poster image url
        :param poster_image_url:
        :return self:
        """
        self.poster_image_url = poster_image_url
        return self

    def set_trailer_youtube_id(self, trailer_youtube_id):
        """
        Set the YouTube video id for the movie trailer
        :param trailer_youtube_id:
        :return:
        """
        self.trailer_youtube_id = trailer_youtube_id
        return self

    def set_trailer_youtube_url(self, trailer_youtube_url):
        """
        Set the YouTube video url for the movie trailer
        :param trailer_youtube_url:
        :return:
        """
        self.trailer_youtube_url = trailer_youtube_url
        return self

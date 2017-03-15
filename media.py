#  Define the Movie class which gives us the basic format of each
#  movie instance upon initalization.
class Movie():
    def __init__(self, movie_title, box_art, trailer_link):
        self.title = movie_title
        self.poster_image_url = box_art
        self.trailer_youtube_url = trailer_link

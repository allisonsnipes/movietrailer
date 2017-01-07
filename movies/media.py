#dont forget importing the webbrowser

import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    #triple quotes allows us to make documentation for a class
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

import webbrowser
# Create Movie class to create multiple instances
class Movie():
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Initialize and create space in memory with defining __init__
    # self is the object being created. Running called kung_fu_panda, the __init__
    # Initialize these title, storyline, image trailer as arguments to __init__
    # function.
    # function inside the class Movie get called.
    def __init__(self, movie_title, movie_storyline, poster_image,
    trailer_youtube):
        # Remember several information inside our class
        # Initialize varialbes
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

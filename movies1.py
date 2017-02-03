import webbrowser


class movies:
    def __init__(self,movie_title,poster_image,movie_storyline,trailer_youtube):
        self.title=movie_title
        self.poster_image_url=poster_image
        self.storyline=movie_storyline
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailor_youtube_url)
    

import webbrowser

# Create the class Movie to store all information we need for a movie:
# title, storyline, postal image url and youtube trailer url, and also
# a show_trailer method to open the trailer link for us
class Movie():
	def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

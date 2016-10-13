import media
import fresh_tomatoes

# Create a bunch of movies I like
demolition = media.Movie("Demolition",
					"A successful investment banker struggles after losing his wife in a tragic car crash. With the help of a customer service rep and her young son, he starts to rebuild, beginning with the demolition of the life he once knew.",
					"https://upload.wikimedia.org/wikipedia/en/d/da/Demolition_poster.jpg",
					"https://youtu.be/3UnSXelOJo0")

artificial_intelligence = media.Movie("Artifictial Intelligence",
					"A highly advanced robotic boy longs to become \"real\" so that he can regain the love of his human mother.",
					"https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
					"https://youtu.be/_19pRsZRiz4")

twelve_angry_men = media.Movie("12 Angry Men",
					"A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.",
					"https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
					"https://youtu.be/fSG38tk6TpI")

sully = media.Movie("Sully",
					"The story of Chesley Sullenberger, an American pilot who became a hero after landing his damaged plane on the Hudson River in order to save the flight's passengers and crew.",
					"https://upload.wikimedia.org/wikipedia/en/8/82/Sully_xxlg.jpeg",
					"https://youtu.be/mjKEXxO2KNE")

amy = media.Movie("Amy",
				  "Archival footage and personal testimonials present an intimate portrait of the life and career of British singer/songwriter Amy Winehouse.",
				  "https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/Amy_Movie_Poster.jpg/330px-Amy_Movie_Poster.jpg",
				  "https://youtu.be/_2yCIwmNuLE")

forty_five_years = media.Movie("45 Years",
							   "A married couple preparing to celebrate their wedding anniversary receives shattering news that promises to forever change the course of their lives.",
							   "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/45_Years_%28poster%29.jpg/330px-45_Years_%28poster%29.jpg",
							   "https://youtu.be/Tg5cpiX18TA")

song_of_the_sea = media.Movie("Song of the Sea",
							  "Ben, a young Irish boy, and his little sister Saoirse, a girl who can turn into a seal, go on an adventure to free the faeries and save the spirit world.",
							  "https://upload.wikimedia.org/wikipedia/en/4/4f/Song_of_the_Sea_%282014_film%29_poster.jpg",
							  "https://youtu.be/6Jxc7WkC674")

our_little_sister = media.Movie("Our Little Sister",
								"A story that revolves around three sisters who live in their grandmother's home and the arrival of their thirteen-year-old half sister.",
								"https://upload.wikimedia.org/wikipedia/en/4/4b/Our_Little_Sister_poster.jpeg",
								"https://youtu.be/NtTeSQFce2A")

the_great_gatsby = media.Movie("The Great Gatsby",
							   "A writer and wall street trader, Nick, finds himself drawn to the past and lifestyle of his millionaire neighbor, Jay Gatsby.",
							   "https://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",
							   "https://youtu.be/rARN6agiW7o")

# The complete movies list
movies_list = [demolition, artificial_intelligence, twelve_angry_men, sully,
			   amy, forty_five_years, song_of_the_sea, our_little_sister, 
			   the_great_gatsby]

# Render the movie website with the fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies_list)

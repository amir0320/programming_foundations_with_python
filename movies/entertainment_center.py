import media
import fresh_tomatoes

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

movies_list = [demolition, artificial_intelligence, twelve_angry_men]

fresh_tomatoes.open_movies_page(movies_list)

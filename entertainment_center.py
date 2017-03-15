import media
import fresh_tomatoes

#  Create new instances of the Movie class for each movie
moana = media.Movie("Moana",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                    "https://youtu.be/LKFuXETZUsI")

zootopia = media.Movie("Zootopia",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/e/ea/Zootopia.jpg/220px-Zootopia.jpg",
                       "https://youtu.be/jWM0ct-OLsM")

deadpool = media.Movie("Deadpool",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://youtu.be/ONHBaC-pfsk")
dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "https://images-na.ssl-images-amazon.com/images/I/51XVZYDA0ZL.jpg",
                              "https://youtu.be/l13yPhimE3o")
walle = media.Movie("WALL-E",
                     "http://www.gstatic.com/tv/thumb/movieposters/174374/p174374_p_v8_ab.jpg",
                     "https://youtu.be/vbLNOFbsRow")

#  Place all our movies into an array
movies = [moana, zootopia, deadpool, dumb_and_dumber, walle]

#  Pass the movies array to the open_movies_page function to create the page
fresh_tomatoes.open_movies_page(movies)

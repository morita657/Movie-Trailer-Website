import fresh_tomatoes
import media
# Save each movie information in the memory
# Use Movie class from media.py file to create multiple instances
kung_fu_panda = media.Movie("Kung Fu Panda",
"A panda who learned Kung Fu",
"https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-K\
ungfupanda.jpg",
"https://www.youtube.com/watch?v=PXi3Mv6KMzY",
)

jurassic_park = media.Movie("Jurassic Park ",
"Dinasours in an island",
"https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
"https://www.youtube.com/watch?v=Bim7RtKXv90")

mask = media.Movie("The Mask",
"A guy got a magical mask",
"https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/The_Mask_%28film%29_pos\
ter.jpg/220px-The_Mask_%28film%29_poster.jpg",
"https://youtu.be/hOqVRwGVUkA")


lion_king = media.Movie("The Lion King",
"King of lion in Savanna",
"https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg\
/220px-The_Lion_King_poster.jpg",
"https://www.youtube.com/watch?v=4sj1MT05lAA")

ghostbusters = media.Movie("Ghostbusters",
"Guys buster the bunch of ghosts",
"https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Ghostbusters_2016_film_p\
oster.png/220px-Ghostbusters_2016_film_poster.png",
"https://www.youtube.com/watch?v=w3ugHP-yZXw")

ip_man = media.Movie("Ip Man",
"The father of Wing Chun",
"https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Ipmanposter02.jpg/220px\
-Ipmanposter02.jpg",
"https://www.youtube.com/watch?v=1AJxXQ7xojE")

# Store the movies in array
movies = [kung_fu_panda, jurassic_park, mask, lion_king, ghostbusters, ip_man]

# Fire open_movies_page function with movies argument from fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)

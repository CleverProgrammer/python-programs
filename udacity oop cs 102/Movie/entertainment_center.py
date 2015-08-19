import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.co/watch?v=-9ceBgWV8io")

#print (avatar.storyline)
#avatar.show_trailer()

bourne_ultimatum = media.Movie("Disturbance",
                              "Elite government agent turned fugitive",
                              "https://lh6.googleusercontent.com/-WDTSBS4bBsE/AAAAAAAAAAI/AAAAAAAADfI/8HrU_a4zNBs/photo.jpg",
                              "https://www.youtube.com/watch?v=5X7hD7YdeRU&list=UUdLGaaCfWku4cVx6L2_DO0w")
#print (bourne_ultimatum.storyline)
#bourne_ultimatum.show_trailer()

movies = [toy_story, avatar, bourne_ultimatum]
fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)








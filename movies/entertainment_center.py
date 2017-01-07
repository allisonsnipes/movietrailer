import fresh_tomatoes
#use contents of prev media file -- good practice to keep my class def in one file and use class from another file

#class can have data and method
#when create an instance of a class "like our movies" the class constructor gets called, like the __inuit__ functino
#and we initialize all the data for the instance, the constructor uses the keyword self
#self is each movie variable
#all of the variables assosiated with the variables are called instance variables
#the functions inside of the class that have an instance and have the first arguement as self are instance methods

import media

#media is the name of prev python file and movie is the class defined in the file

happy_feet = media.Movie("Happy Feet", "A story of a peguin and music", "http://vignette1.wikia.nocookie.net/happyfeet/images/b/b9/Happy-Feet-2-For-Your-Consideration.png/revision/latest?cb=20140329154717", "https://www.youtube.com/watch?v=s0liQAocT9s")
#print(happy_feet.storyline)
#happy_feet.show_trailer()

sausage_party = media.Movie("Sausage Party", "The untold story of food", "http://i2.wp.com/matthewliedke.areavoices.com/files/2016/08/sausagepartymovie.jpg?fit=640%2C320", "https://www.youtube.com/watch?v=Evw9HMnYEmY")
#print(sausage_party.storyline)
#sausage_party.show_trailer()

twentyeight_days_later = media.Movie("28 Days Later", "Zombie Apocolaspe", "https://i.ytimg.com/vi/e1gv_SFRZEc/hqdefault.jpg", "https://www.youtube.com/watch?v=HEkJAaGhJhQ")
#print(twentyeight_days_later.storyline)
#twentyeight_days_later.show_trailer()

dont_breathe = media.Movie("Don't Breathe", "Psychological Thriller", "https://images-na.ssl-images-amazon.com/images/M/MV5BZGI5ZTU2M2YtZWY4MC00ZDFhLTliYTItZTk1NjdlN2NkMzg2XkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=76yBTNDB6vU")
#print(dont_breathe.storyline)
#dont_breathe.show_trailer()

suicide_squad = media.Movie("Suicide Squad", "Squad Goals", "https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_(film)_Poster.png", "https://www.youtube.com/watch?v=CmRih_VtVAs")
#print(suicide_squad.storyline)
#suicide_squad.show_trailer()

dead_snow = media.Movie("Dead Snow", "Zombies from WWII come back alive", "https://authorcamilson.files.wordpress.com/2015/08/917nulomggl-_sl1500_.jpg", "https://www.youtube.com/watch?v=R19KagZyU40")
#print(dead_snow.storyline)
#dead_snow.show_trailer()

#an array is a list
#movies is the arguement
movies = [happy_feet, sausage_party, twentyeight_days_later, dont_breathe, suicide_squad, dead_snow]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

#this allows us to use documentation from a particular class

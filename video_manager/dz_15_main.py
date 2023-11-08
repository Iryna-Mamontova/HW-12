import os
import string
import media_player
import films_workers

os.mkdir('film_player/film_storage')
os.chdir('film_player/film_storage')
for letter in string.ascii_uppercase:
  os.mkdir(letter)
os.chdir('..')

film_1 = films_workers.Film('Harry Potter')
film_2 = films_workers.Film('It')
film_3 = films_workers.Film('One plus one')
film_4 = films_workers.Film('Friends')
film_5 = films_workers.Film('How I met your mother')
film_4.get_film_address()
print(film_1.title)

film_6 = media_player.Player('Some link')
film_6.play('Some link')


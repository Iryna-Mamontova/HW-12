import os
import string
import shutil
import awards
from films_data import films_titles
import def_sorting_awards

os.mkdir('Harry Potter')
os.chdir('Harry Potter')
for film in films_titles["results"]:
    f_title = film["title"].replace(': ', '_').replace(' ', '_')
    os.mkdir(f_title)
    os.chdir(f_title)
    for letters in string.ascii_uppercase:
      os.mkdir(letters)
    def_sorting_awards.sorting_awards(film["imdb_id"])
    os.chdir('..')

   
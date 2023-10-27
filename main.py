import films_data
import os
import string
import shutil

# shutil.rmtree('Harry Potter')

os.mkdir('Harry Potter')
os.chdir('Harry Potter')
for film in films_data.films_titles["results"]:
    f_title = film["title"].replace(': ', '_')
    os.mkdir(f_title)
    os.chdir(f_title)
    for letters in string.ascii_uppercase:
      os.mkdir(letters)
    os.chdir('..')
    
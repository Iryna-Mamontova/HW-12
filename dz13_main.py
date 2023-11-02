from ganres import ganres
from films_data_13 import films_data
import csv
import os
import json

dict_ganres = json.loads(ganres)

for genre in dict_ganres['results']:
  os.mkdir(genre['genre'])

films_data_short = []
for film in films_data:
  films_data_short.append({'title': film['title'],
                           'year': film['year'],
                           'rating': film['rating'],
                           'type': film['type'],
                           'genres':[genr['genre'] for genr in film['gen']]
                          })

for dir_name in os.listdir():
   for film in films_data_short:
    if dir_name in film['genres']:
      os.chdir(dir_name)
      if os.path.isfile('file_info.csv'):
         with open('file_info.csv', 'a', newline='') as file_info_obj:
           writer = csv.writer(file_info_obj)
           writer.writerow(film.values())
      else:
        with open ('file_info.csv', 'w', newline='') as file_info_obj:
          writer = csv.DictWriter(file_info_obj, fieldnames= ['title', 'year', 'rating', 'type', 'genres'])
          writer.writeheader()
          writer.writerow(film)
      os.chdir('..')
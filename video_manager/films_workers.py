import shutil
import os
import string

class Film:
  def __init__(self, title, description = None, storage_address = None, running_time = 0, country = None, imdb = 0.0):
   self.title = title
   self.description = description
   self.storage_address = storage_address
   self.running_time = running_time
   self.country = country
   self.imdb = imdb

  @classmethod
  def upload_file(cls):
    for letter in string.ascii_uppercase:
      if cls.title.startswith(letter):
         os.chdir('film_player/film_storage/' + letter)
         with open(cls.title.replace(' ', '_') + '.txt', 'w') as film_name_obj:
          pass
        #  shutil.move(os.path.abspath(cls.title.replace(' ', '_') + '.txt'), letter)
         os.chdir('film_player/film_storage/')

  def get_film_address(self):
    os.chdir('film_player/film_storage/' + self.title[0])
    self.storage_address = os.path.abspath(self.title.replace(' ', '_') + '.txt')
    print(self.storage_address)
    os.chdir('film_player')
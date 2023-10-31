import os
import string
import shutil
import def_award_list

def sorting_awards(imdb):
  for name_award in def_award_list.award_list(imdb):
    if os.path.isfile(name_award['award_name'] + '.txt'):
      name_award_obj = open(name_award['award_name']+'.txt', 'a')
      name_award_obj.write(name_award['award'] + '\n')
      name_award_obj.close()
    else: 
      name_award_obj = open(name_award['award_name']+'.txt', 'w')
      name_award_obj.write(name_award['award'] + '\n')
      name_award_obj.close()

  aw_list = list(os.walk('.'))
  for awards_file in aw_list[0][2]:
    for letter in string.ascii_uppercase:
      if awards_file.startswith(letter):
         shutil.move(os.path.abspath(awards_file), letter)
         
import awards
def award_list(id):
  list_name = []
  for film in awards.films_awards:
    for mv in film['results']:
      if mv['movie']['imdb_id'] == id:
        list_name.append({'type': mv['type'],
                      'award_name': mv['award_name'],
                      'award': mv['award']
                      })
  list_name = list(sorted(list_name, key = lambda fil_aw: fil_aw['award_name']))
  return list_name
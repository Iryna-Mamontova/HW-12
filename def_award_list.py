import awards
def award_list(id):
  list_name = []
  for film in awards.films_awards[0]['results']:
    if film['movie']['imdb_id'] == id:
      list_name.append({'type': film['type'],
                      'award_name': film['award_name'],
                      'award': film['award']
                      })
  list_name = list(sorted(list_name, key = lambda fil_aw: fil_aw['award_name']))
  return list_name
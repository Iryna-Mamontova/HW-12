class Player:
  def __init__(self, video_link):
   self.name = ''
   self.video_link = video_link
   self.duration = 0


  def play(self, film_adr):
    print(film_adr is self.video_link)

  def pause(self):
    pass
    
  def save_last_time(self):
    pass
    
  def change_quality(self):
    pass
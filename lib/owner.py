class Owner:
  def __init__(self, name):
    self.name = name
    self.movie_owners = []

  def movies(self):
    return [movie_owner.movie for movie_owner in self.movie_owners]
  
  def __repr__(self):
    return f'<Owner name={self.name}>'
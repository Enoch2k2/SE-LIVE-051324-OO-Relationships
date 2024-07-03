class Movie:
  def __init__(self, title):
    self.title = title
    self.movie_owners = []
    
  def owners(self):
    return [movie_owner.owner for movie_owner in self.movie_owners]

  def __repr__(self):
    return f'<Movie title={self.title}>'
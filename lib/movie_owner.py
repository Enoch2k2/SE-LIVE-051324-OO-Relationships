# MovieOwner belongs to an owner
# MovieOwner belongs to a movie

class MovieOwner:
  all = []

  def __init__(self, owner, movie, rating):
    self.owner = owner
    self.movie = movie
    self.rating = rating
    # code chaining - telling the story of code
    self.owner.movie_owners.append(self)
    self.movie.movie_owners.append(self)

    MovieOwner.all.append(self)

  def __repr__(self):
    return f'<MovieOwner owner={self.owner.name} movie={self.movie.title} rating={self.rating}>'
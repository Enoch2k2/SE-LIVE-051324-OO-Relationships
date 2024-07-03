from movie_owner import MovieOwner
from movie import Movie
from owner import Owner

import ipdb

bob = Owner(name="Bob")
sarah = Owner(name="Sarah")

star_wars = Movie(title="Star Wars")
fast_and_the_furious = Movie(title="Fast and the Furious")

movie_owner_1 = MovieOwner(owner=bob, movie=star_wars, rating=7)
movie_owner_2 = MovieOwner(owner=sarah, movie=star_wars, rating=10)
movie_owner_3 = MovieOwner(owner=bob, movie=fast_and_the_furious, rating=9)

ipdb.set_trace()


# how does the relationship class (aka join / through class) store both of the objects that is being related! Always a belongs to! self.attribute = object
# one to many of the relationship objects (owner to movie_owner)
# one to many of the related object through the relationship objects, example: from owner to movie, have to go through movie owner.
import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist1 = Artist('The Bug Club')
artist_repository.save(artist1)
artist2 = Artist('The Beatles')
artist_repository.save(artist2)

album1 = Album('Pure Particles', 'indie', artist1)
album_repository.save(album1)
album2 = Album('Magical Mystery Tour', 'rock', artist2)
album_repository.save(album2)

# album_repository.delete_all()
# artist_repository.delete_all()

# results = album_repository.select_one(1)
# results = artist_repository.select_one(1)

# results = artist_repository.select_all()
results = album_repository.select_all()


print(results.__dict__)

pdb.set_trace()
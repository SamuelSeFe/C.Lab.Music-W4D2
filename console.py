import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album1 = Album('Pure Particles', 'indie', 'The Bug Club')
album_repository.save(album1)
album2 = Album('Magical Mystery Tour', 'rock', 'The Beatles')
album_repository.save(album2)

artist1 = Artist('The Bug Club')
artist_repository.save(artist1)
artist2 = Artist('The Beatles')
artist_repository.save(artist2)

# album_repository.delete_all()
# artist_repository.delete_all()







for task in result:
    print(task.__dict__)

pdb.set_trace()
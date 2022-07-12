from db_music.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def select_all():
    albums = []

    sql = "SELECT * FROM albums"

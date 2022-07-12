from db_music.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository

# def select_all():
#     artists = []

#     sql = "SELECT * FROM artists"
#     artists = run_sql(sql)

#     for row in artists:
#         album = album_repository.select_all(row['id'])
#         artist = Artist(row['name'], album, row['id]'])
#         artists.append(artist)
#     return artists


def save(artist):
    sql = """
        INSERT INTO artists (name)
        VALUES (%s)
        RETURNING *
    """

    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select_one(id):
    artist = []
    sql = 'SELECT * FROM artists WHERE id=%s'
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist


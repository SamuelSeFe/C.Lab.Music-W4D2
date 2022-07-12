from db_music.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    albums = run_sql(sql)

    for row in albums:
        # artist = artist_repository.select_all(row['id'])
        album = Album(row['title'], row['genre'], row['artist'], row['id]'])
        albums.append(album)
    return albums

def save(album):
    sql = """
        INSERT INTO albums (title, genre, artist_id)
        VALUES (%s, %s, %s)
        RETURNING *
    """

    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select_one(id):
    albums = None
    sql = 'SELECT * FROM albums WHERE id=%s'
    values = [id]
    albums = run_sql(sql, values)
    if albums:
        result = albums[0]
        artist = artist_repository.select_one(result['id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album
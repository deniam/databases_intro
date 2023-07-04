"""
when I call #all on the AlbumRepostory
I get all albums back in the list"""

def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
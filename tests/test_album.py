from lib.album import Album
"""
When I construct an Album
with the fileds id, title, release_year and artist_id
They are reflected in instance properties
"""
def test_constructions_with_fileds():
    album = Album(1, "I Put A Spell On You", 2020, 4)
    assert album.id == 1
    assert album.title == "I Put A Spell On You"
    assert album.release_year == 2020
    assert album.artist_id == 4

"""
When construct two Albums with the same fields
and they are equal
"""
def test_equality():
    album1 = Album(1, "I Put A Spell On You", 2020, 4)
    album2 = Album(1, "I Put A Spell On You", 2020, 4)
    assert album1 == album2

"""
When I construct an Album
And I format it to a string
then it comes in a friendly format
"""

def test_formatting():
    album = Album(1, "I Put A Spell On You", 2020, 4)
    assert str(album) == "Album(1, I Put A Spell On You, 2020, 4)"
"""

8-7. Album: Write a function called make_album() that builds a dictionary

describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 

Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 

If the calling line includes a value for the number of songs, add that value to the album's dictionary. Make at least one new function call that includes the number of songs on an album.

"""

def make_album(artist_name, album_title, song_count = None):

    album_details = {}

    album_details['artist_name'] = artist_name

    album_details['album_title'] = album_title

    if song_count:
        album_details['song_count'] = song_count

    return album_details



album1 = make_album("artist1", "album1", 11)

print(album1)

album2 = make_album("artist2", "album2", 7)

print(album2)

album3 = make_album("artist3", "album3")

print(album3)



"""
8-8. User Albums: Start with your program from Exercise 8-7. 

Write a while loop that allows users to enter an album's artist and title. 

Once you have that information, call make_album() with the user's input and print the dictionary that's created. 

Be sure to include a quit value in the while loop.

"""

def make_album(artist_name, album_title, song_count = None):

    album_details = {}

    album_details['artist_name'] = artist_name

    album_details['album_title'] = album_title

    if song_count:
        album_details['song_count'] = song_count

    return album_details


str_continue_program = "Y"

music_album_detail = {}

while str_continue_program.upper() == "Y":

    artist_name = input("Enter the name of the artist: ")

    album_title = input("Enter the title of the album: ")

    song_count = int(input("Enter the song count, (type -1 if song count is not known): "))

    if song_count < 1:
        music_album_detail = make_album(artist_name, album_title)
    else:
        music_album_detail = make_album(artist_name, album_title, song_count)

    print(music_album_detail)

    str_continue_program = input("Enter 'Y' if you would like to continue: ")

    
        
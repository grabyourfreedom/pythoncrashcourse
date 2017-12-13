# Let us have you enter the album you like
# Program to make music album


def make_album(artist_name, album_title, number_of_tracks=0):
    album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_tracks > 0:
        album['tracks'] = number_of_tracks
    return album


def print_album(album):
    for key, value in album.items():
        print(key.title() + ": " + str(value).title())
    print()
    return


enter_input = True
while enter_input:
    title = input("Enter the title of the album: ")
    artist = input("Enter artist name: ")
    tracks = input("Enter number of tracks: ")
    tracks = int(tracks)
    album = make_album(artist, title, tracks)
    print_album(album)

    enter_more = input("Do you want to continue [y/n]: ")
    enter_input = False
    if enter_more.lower() == 'y':
        enter_input = True

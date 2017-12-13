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


krishna = make_album("Dr. K J Yesudas", "Krishna Leela Tharangini")
print_album(krishna)

krishna = make_album("Dr. K J Yesudas", "Krishna Leela Tharangini", 7)
print_album(krishna)
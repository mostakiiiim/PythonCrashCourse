def make_album(name, title, song_number=None):
    album={
        'artist_name': name,
        'album_title': title
        }
    if song_number:
        album['song_no.'] = song_number
    print(album) 

make_album(input('Enter artist name'), input('Enter album name'), input('Enter Song no.'))


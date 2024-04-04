import lyricsgenius
genius = lyricsgenius.Genius("jPnYlXn0YEF4xJLJJJ0V2fngWTmyK4c9scfIxFMpofO4-aKIWJ8t9f_11oCeZCLj")

async def search_lyrics(song_title, artist_name):
    try:
        # Search for the lyrics
        song = genius.search_song(song_title, artist_name)
        if song:
            return song.lyrics
        else:
            return f"Lyrics for '{song_title}' by {artist_name} not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


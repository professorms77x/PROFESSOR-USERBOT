import lyricsgenius
genius = lyricsgenius.Genius("jPnYlXn0YEF4xJLJJJ0V2fngWTmyK4c9scfIxFMpofO4-aKIWJ8t9f_11oCeZCLj")
async def search_lyrics(song_title, artist_name):
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            return song.lyrics
        else:
            return f"ʟʏʀɪᴄꜱ ꜰᴏʀ '{song_title}' ʙʏ {artist_name} ɴᴏᴛ ꜰᴏᴜɴᴅ..."
    except Exception as e:
        return f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {str(e)}"


from Song import Song

for line in open("songextraction/songs.txt"):
    song = Song(artist="Grateful Dead", title=line)
    lyr = song.lyricwikia()
    if lyr is not None:
        with open("songs/"+line.replace("\n","")+".txt","w") as f:
            f.write(lyr)

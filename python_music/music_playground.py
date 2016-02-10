# Playing with Music
from glob import glob
from pydub import AudioSegment

playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("*.mp3")]
# print(playlist_songs)
# first_song = playlist_songs.pop(0)
# first_song = first_song[:5000]  # milliseconds to seconds
# second_song = playlist_songs.pop(0)
# second_song = second_song[31000:41000]  # milliseconds to seconds
# playlist = first_song + second_song
# playlist_length = len(playlist) / (1000 * 60)
# # lets save it!
# out_f = open("playlist.mp3", 'wb')
#
# playlist.export(out_f, format='mp3')

song = playlist_songs.pop(1)
ten_seconds = 10 * 1000
first_10_seconds = song[:ten_seconds]
last_5_seconds = song[-5000:]
beginning = first_10_seconds + 6
end = last_5_seconds - 3
without_the_middle = beginning + end
with_style = beginning.append(end, crossfade=1500)
do_it_over = with_style * 2
awesome = do_it_over.fade_in(2000).fade_out(3000)
awesome.export("mashup.mp3", format="mp3")

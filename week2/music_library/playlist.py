import json
from song import Song


def load():
    file_name = "data.txt"
    file_read = open(file_name)
    json_temp = json.load(file_read)
    playlist1 = Playlist(json_temp['name'])
    for song in json_temp["songs"]:
        title = song['title']
        artist = song['artist']
        rating = song['rating']
        bitrate = song['bitrate']
        album = song['album']
        length = song['length']
        song1 = Song(title, artist, album, length, bitrate)
        if rating is not None:
            song1.rate(rating)
        playlist1.add_song(song1)
    return playlist1


def sec_to_min(secs):
    m, s = divmod(secs, 60)
    return "%02d:%02d" % (m, s)


class Playlist:
    LOW_BITRATE = 128

    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def delete_song(self, song_name):
        for song in self.playlist:
            if song_name == song.title:
                self.playlist.remove(song)

    def total_length(self):
        sum = 0
        for song in self.playlist:
            sum += song.length
        return sum

    def remove_disrated(self, rating):
        for song in self.playlist:
            if song.rating <= rating:
                self.playlist.remove(song)

    def remove_bad_quality(self):
        for song in self.playlist:
            if song.bitrate < self.LOW_BITRATE:
                self.playlist.remove(song)

    def show_artists(self):
        artists = []
        for song in self.playlist:
            if song.artist not in artists:
                artists.append(song.artist)
        return artists

    def __str__(self):
        res = ""
        for song in self.playlist:
            res += "{} {} - {}\n".format(song.artist, song.title, sec_to_min(song.length))
        return res

    def save(self, file_name):
        songs = []

        for song in self.playlist:
            songs.append(song.__dict__)

        with open(file_name, 'w') as outfile:
            json.dump({"name": self.playlist, "songs": songs}, outfile)

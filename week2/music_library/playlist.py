import json


def sec_to_min(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


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
            res = "{} {} - {}\n".format(song.artist, song.title, sec_to_min(song.length))
        return res

    def save(self, file_name):
        with open('data.txt', 'w') as outfile:
            json.dump({"name": "self.playlist", "songs":[{"title": "song.title", "artist":song.artist, "album": song.album, "rating": song.rating, "length": song.length}]})

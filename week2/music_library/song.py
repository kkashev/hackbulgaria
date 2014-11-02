class Song:
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title, artist, album, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = None
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if rating >= self.MIN_RATING and rating <= self.MAX_RATING:
            self.rating = rating
        else:
            raise ValueError

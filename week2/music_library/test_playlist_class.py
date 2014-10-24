from playlist import Playlist
from song import Song
import unittest


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.test_playlist = Playlist("Rocking songs")

    def test_init_playlist(self):
        self.assertEqual(self.test_playlist.name, "Rocking songs")

    def test_add_song(self):
        test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 320)
        self.test_playlist.add_song(test_song)
        self.assertIn(test_song, self.test_playlist.playlist)

    def test_remove_song(self):
        test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 320)
        self.test_playlist.delete_song(test_song)
        self.assertNotIn(test_song, self.test_playlist.playlist)

    def test_total_length(self):
        test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 320)
        test_song2 = Song("Fuck me", "Metallica", "Rock it", 4, 100, 256)
        self.test_playlist.add_song(test_song)
        self.test_playlist.add_song(test_song2)
        self.assertEqual(280, self.test_playlist.total_length())

    def test_remove_disrated(self):
        test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 320)
        self.test_playlist.add_song(test_song)
        test_song.rate(5)
        self.test_playlist.remove_disrated(5)
        self.assertNotIn(test_song, self.test_playlist.playlist)

    def test_remove_bad_quality(self):
        test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 64)
        self.test_playlist.add_song(test_song)
        self.assertIsNot(test_song, self.test_playlist.remove_bad_quality())

    def test_show_artists(self):
        test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 64)
        test_song1 = Song("BlaBla", "Metallica", "Black in black", 4, 180, 64)
        test_song2 = Song("Take", "Rihanna", "Black in black", 4, 180, 64)
        test_song3 = Song("me", "AC DC", "Black in black", 4, 180, 64)
        test_song4 = Song("Take me", "AC DC", "Black in black", 4, 180, 64)
        self.test_playlist.add_song(test_song)
        self.test_playlist.add_song(test_song1)
        self.test_playlist.add_song(test_song2)
        self.test_playlist.add_song(test_song3)
        self.test_playlist.add_song(test_song4)
        self.assertListEqual(["AC DC", "Metallica", "Rihanna"], self.test_playlist.show_artists())

    def test_str(self):
        test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 64)
        self.test_playlist.add_song(test_song)
        self.assertEqual("AC DC Take me - 3:00", self.test_playlist.__str__(test_song))

if __name__ == '__main__':
    unittest.main()

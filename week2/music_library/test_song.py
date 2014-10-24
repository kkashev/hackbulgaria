from song import Song
import unittest


class TestSong(unittest.TestCase):
    def setUp(self):
        self.test_song = Song("Take me", "AC DC", "Black in black", 4, 180, 320)

    def test_init_song(self):
        self.assertEqual(self.test_song.title, "Take me")
        self.assertEqual(self.test_song.artist, "AC DC")
        self.assertEqual(self.test_song.album, "Black in black")
        self.assertEqual(self.test_song.length, 180)
        self.assertEqual(self.test_song.bitrate, 320)

    def test_rate(self):
        self.test_song.rate(4)
        self.assertEqual(self.test_song.rating, 4)

    def test_rating_out_of_range(self):
        with self.assertRaises(ValueError):
            self.test_song.rate(200)

if __name__ == '__main__':
    unittest.main()

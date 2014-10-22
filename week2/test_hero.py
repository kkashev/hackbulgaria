from hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "Dragon Slayer")

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.nickname, "Dragon Slayer")

    def test_known_as(self):
        self.assertEqual(self.bron_hero.known_as(), "Bron the Dragon Slayer")


if __name__ == '__main__':
    unittest.main()
